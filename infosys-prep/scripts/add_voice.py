"""Add read-aloud (Listen buttons + voice bar) to infosys-prep/website/index.html.

Safe to re-run: any earlier voice block is removed first, so the page never gets two copies.
Usage: python3 infosys-prep/scripts/add_voice.py
"""
import pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
PAGE = HERE.parent / "website" / "index.html"

BAR = """<div id="voicebar" class="voicebar" role="region" aria-label="Read aloud controls">
    <strong>🔊 Read aloud</strong>
    <label>Voice <select id="v-voice" aria-label="English voice"></select></label>
    <label>Speed <select id="v-rate" aria-label="Speech speed"><option value="0.8">Slow</option><option value="1" selected>Normal</option><option value="1.2">Fast</option><option value="1.5">Faster</option></select></label>
    <button id="v-pause" type="button" disabled>Pause</button>
    <button id="v-stop" type="button" disabled>Stop</button>
    <span id="v-status" role="status" aria-live="polite">Press 🔊 Listen on any problem card.</span>
  </div>
  """

html = PAGE.read_text(encoding="utf-8")
# drop any earlier copy
html = re.sub(r'<style id="voice-css">.*?</style>\n?', "", html, flags=re.S)
html = re.sub(r'<div id="voicebar".*?</div>\n  ', "", html, flags=re.S)
html = re.sub(r'<script id="voice-js">.*?</script>\n?', "", html, flags=re.S)

css = (HERE / "voice_tab.css").read_text(encoding="utf-8")
js = (HERE / "voice_tab.js").read_text(encoding="utf-8")
assert "</script>" not in js and "</style>" not in css

assert html.count("</head>") == 1 and html.count("<main>") == 1 and html.count("</body>") == 1
html = html.replace("</head>", '<style id="voice-css">\n' + css + "</style>\n</head>")
html = html.replace("<main>\n  ", "<main>\n  " + BAR, 1)
html = html.replace("</body>", '<script id="voice-js">\n' + js + "</script>\n</body>")
PAGE.write_text(html, encoding="utf-8")
print("voice block added;", len(html), "bytes")
