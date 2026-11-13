// Read-aloud support for the guide: a Listen button on every problem card, using the browser's built-in
// English voices (Web Speech API). Runs after the main script and only touches the DOM it renders.
(function(){
'use strict';
var bar = document.getElementById('voicebar');
if (!bar) return;
var synth = window.speechSynthesis;
var supported = !!synth && typeof window.SpeechSynthesisUtterance === 'function';
var voiceSel = document.getElementById('v-voice'), rateSel = document.getElementById('v-rate');
var pauseBtn = document.getElementById('v-pause'), stopBtn = document.getElementById('v-stop');
var status = document.getElementById('v-status');
if (!supported) {
  bar.querySelectorAll('select,button').forEach(function(e){ e.disabled = true; });
  status.textContent = 'This browser has no speech support, so reading aloud is unavailable. Try Chrome, Edge or Safari.';
  return;
}

// remembered voice and speed (per viewer, optional)
var KEY = 'infosys-voice-v1', pref = {voice: '', rate: '1'};
try { var saved = JSON.parse(localStorage.getItem(KEY) || '{}'); if (saved.voice) pref.voice = saved.voice; if (saved.rate) pref.rate = saved.rate; } catch (e) {}
function savePref() { try { localStorage.setItem(KEY, JSON.stringify(pref)); } catch (e) {} }

var voices = [];
function loadVoices() {
  voices = synth.getVoices().filter(function(v){ return /^en([-_]|$)/i.test(v.lang); });
  voiceSel.replaceChildren();
  if (!voices.length) {
    var o = document.createElement('option'); o.value = ''; o.textContent = 'Default English voice'; voiceSel.append(o); return;
  }
  var chosen = voices.find(function(v){ return v.voiceURI === pref.voice; })
    || voices.find(function(v){ return /^en[-_]IN/i.test(v.lang); })
    || voices.find(function(v){ return v.default; })
    || voices[0];
  voices.forEach(function(v){
    var o = document.createElement('option'); o.value = v.voiceURI; o.textContent = v.name + ' (' + v.lang + ')';
    if (v === chosen) o.selected = true;
    voiceSel.append(o);
  });
}
loadVoices();
if (synth.addEventListener) synth.addEventListener('voiceschanged', loadVoices); else synth.onvoiceschanged = loadVoices;
rateSel.value = pref.rate;
if (rateSel.value !== pref.rate) rateSel.value = '1';

// ---- text for speech ----
function say(t) {
  return t
    .replace(/→|=>|->/g, ' to ')
    .replace(/≤|<=/g, ' is at most ')
    .replace(/≥|>=/g, ' is at least ')
    .replace(/!=|≠/g, ' is not equal to ')
    .replace(/==/g, ' equals ')
    .replace(/&&/g, ' and ')
    .replace(/\|\|/g, ' or ')
    .replace(/O\(/g, 'O of ')
    .replace(/\^/g, ' to the power ')
    .replace(/(\d)\s*%/g, '$1 percent')
    .replace(/%/g, ' mod ')
    .replace(/\*/g, ' times ')
    .replace(/\+/g, ' plus ')
    .replace(/\s-\s/g, ' minus ')
    .replace(/=/g, ' equals ')
    .replace(/</g, ' less than ')
    .replace(/>/g, ' greater than ')
    .replace(/\//g, ' slash ')
    .replace(/[()·]/g, ', ')
    .replace(/[\[\]{}`_~|]/g, ' ')
    .replace(/\s+/g, ' ')
    .replace(/\s+([,.;:!?])/g, '$1')
    .replace(/,+\s*([.;:!?])/g, '$1')
    .replace(/^[,\s]+|,+$/g, '')
    .trim();
}
function chunk(items) {
  var out = [];
  items.forEach(function(item) {
    var text = say(item);
    if (!text) return;
    var sentences = text.match(/[^.!?;]+[.!?;]?/g) || [text];
    var buf = '';
    sentences.forEach(function(s) {
      s = s.trim(); if (!s) return;
      while (s.length > 180) {
        var cut = s.lastIndexOf(',', 180); if (cut < 60) cut = s.lastIndexOf(' ', 180); if (cut < 60) cut = 180;
        if (buf) { out.push(buf); buf = ''; }
        out.push(s.slice(0, cut).trim()); s = s.slice(cut).replace(/^[,\s]+/, '');
      }
      if (buf && buf.length + s.length > 180) { out.push(buf); buf = ''; }
      buf = buf ? buf + ' ' + s : s;
    });
    if (buf) out.push(buf);
  });
  return out;
}
// Sections that are code or raw data are not read aloud.
var SKIP = /^(c\+\+|c|python3?|java|code|sample|sources|mapping|status|how it was checked)$/i;
function cardTitle(card) {
  var t = card.querySelector('summary .t'), h = card.querySelector('h3');
  var txt = t ? t.textContent : h ? h.textContent : '';
  if (/…$/.test(txt)) { var b = card.querySelector('summary .badge'); return 'Item ' + (b ? b.textContent : ''); }
  return txt;
}
function cardItems(card) {
  var parts = [cardTitle(card) + '.'];
  var body = card.querySelector('.body');
  if (body) {
    var skip = false;
    Array.prototype.forEach.call(body.children, function(n) {
      var tag = n.tagName;
      if (tag === 'H4') { var name = n.textContent.trim(); skip = SKIP.test(name); if (!skip) parts.push(name + '.'); return; }
      if (skip || tag === 'A') return;
      if (tag === 'P' && /^From .* in the repo\.?$/i.test(n.textContent.trim())) return;
      if (tag === 'OL') { Array.prototype.forEach.call(n.children, function(li, i){ parts.push('Step ' + (i + 1) + '. ' + li.textContent); }); return; }
      if (tag === 'UL') { Array.prototype.forEach.call(n.children, function(li){ parts.push(li.textContent); }); return; }
      if (tag === 'PRE') { n.textContent.split('\n').forEach(function(l){ if (l.trim()) parts.push(l.trim() + '.'); }); return; }
      parts.push(n.textContent);
    });
  } else {
    // sheet cards: heading, pattern line, solution and check (skip the mapping and status lines)
    Array.prototype.forEach.call(card.children, function(n) {
      if (n.tagName === 'BUTTON' || n.tagName === 'H3') return;
      var t = n.textContent.trim();
      if (/^(External:|Status:)/.test(t)) return;
      parts.push(t);
    });
  }
  return parts;
}

// ---- playback ----
var cur = null;
function stopAll() {
  if (cur) { cur.card.classList.remove('v-speaking'); cur.btn.textContent = '🔊 Listen'; cur.btn.setAttribute('aria-pressed', 'false'); }
  cur = null;
  synth.cancel();
  pauseBtn.disabled = stopBtn.disabled = true;
  pauseBtn.textContent = 'Pause';
  status.textContent = '';
}
function next() {
  var c = cur; if (!c) return;
  if (!c.card.isConnected || c.i >= c.chunks.length) { stopAll(); return; }
  var my = ++c.gen;
  var u = new SpeechSynthesisUtterance(c.chunks[c.i]);
  var v = voices.find(function(x){ return x.voiceURI === voiceSel.value; });
  if (v) { u.voice = v; u.lang = v.lang; } else { u.lang = 'en-US'; }
  u.rate = parseFloat(rateSel.value) || 1;
  u.onend = function() { if (cur === c && c.gen === my) { c.i++; next(); } };
  u.onerror = function(ev) {
    if (cur === c && c.gen === my && ev.error !== 'interrupted' && ev.error !== 'canceled') { status.textContent = 'Speech stopped: ' + ev.error; stopAll(); }
  };
  synth.speak(u);
}
function toggle(card, btn) {
  if (cur && cur.card === card) { stopAll(); return; }
  stopAll();
  var chunks = chunk(cardItems(card));
  if (!chunks.length) { status.textContent = 'Nothing to read on this card.'; return; }
  cur = {card: card, btn: btn, chunks: chunks, i: 0, gen: 0};
  card.classList.add('v-speaking'); btn.textContent = 'Stop'; btn.setAttribute('aria-pressed', 'true');
  pauseBtn.disabled = stopBtn.disabled = false;
  status.textContent = 'Reading: ' + cardTitle(card);
  next();
}
pauseBtn.addEventListener('click', function() {
  if (!cur) return;
  if (synth.paused) { synth.resume(); pauseBtn.textContent = 'Pause'; } else { synth.pause(); pauseBtn.textContent = 'Resume'; }
});
stopBtn.addEventListener('click', stopAll);
function restartChunk() { if (cur) { cur.gen++; synth.cancel(); next(); } }
voiceSel.addEventListener('change', function() { pref.voice = voiceSel.value; savePref(); restartChunk(); });
rateSel.addEventListener('change', function() { pref.rate = rateSel.value; savePref(); restartChunk(); });
document.querySelectorAll('nav.tabs button').forEach(function(b){ b.addEventListener('click', stopAll); });
window.addEventListener('pagehide', function(){ synth.cancel(); });

// ---- Listen buttons on every problem card (cards are rendered lazily, so watch for new ones) ----
function makeBtn(card) {
  var b = document.createElement('button');
  b.type = 'button'; b.className = 'vbtn'; b.textContent = '🔊 Listen'; b.setAttribute('aria-pressed', 'false');
  b.setAttribute('aria-label', 'Listen to this problem');
  b.addEventListener('click', function(e){ e.preventDefault(); e.stopPropagation(); toggle(card, b); });
  ['keydown', 'keyup'].forEach(function(ev){ b.addEventListener(ev, function(e){ if (e.key === ' ' || e.key === 'Enter') e.stopPropagation(); }); });
  return b;
}
function decorate(root) {
  var found = [];
  if (root.matches && (root.matches('details.item') || root.matches('#sh-list .card'))) found.push(root);
  if (root.querySelectorAll) root.querySelectorAll('details.item, #sh-list .card').forEach(function(x){ found.push(x); });
  found.forEach(function(card) {
    if (card.dataset.voice) return;
    card.dataset.voice = '1';
    var b = makeBtn(card);
    var s = card.querySelector('summary'), h = card.querySelector('h3');
    if (s) s.append(b); else if (h) h.after(b);
  });
}
decorate(document);
new MutationObserver(function(muts) {
  muts.forEach(function(m){ m.addedNodes.forEach(function(n){ if (n.nodeType === 1) decorate(n); }); });
}).observe(document.querySelector('main'), {childList: true, subtree: true});
})();
