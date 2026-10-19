/**
 * Codeforces 1200 Memory Sheet & Infosys SP/DSE AI Intelligence
 * Application Core Logic: Voice Narration Coach, Pattern Likeness Index,
 * Exam Prediction Engine, and Batch Ingestion.
 */

(function () {
  'use strict';

  // --- Constants & Storage Keys ---
  const STORAGE_KEYS = {
    QUESTIONS: 'cf_1200_custom_questions_v4',
    COMPLETED: 'cf_1200_completed_v2',
    STARRED: 'cf_1200_starred_v2',
    NOTES: 'cf_1200_personal_notes_v2',
    DISCUSSIONS: 'cf_1200_custom_discussions_v2',
    SOUND: 'cf_1200_sound_pref'
  };

  const TARGET_TOTAL = 1200;

  // --- State ---
  let allQuestions = [];
  let completedMap = {};
  let starredMap = {};
  let notesMap = {};
  let customDiscussionsMap = {};
  let soundEnabled = true;

  let currentView = 'sheet'; // 'sheet' | 'cards' | 'flashcard'
  let currentPage = 1;
  let pageSize = 50;
  let showAllIntuitions = false;

  let filterState = {
    search: '',
    topic: 'all',
    rating: 'all',
    status: 'all',
    infosys: 'all',
    sort: 'default'
  };

  let activeModalQuestion = null;
  let activeCodeLang = 'cpp';
  let activeVoiceQuestion = null;

  // --- DOM Elements ---
  const el = {
    // Header Stats
    statTargetTotal: document.getElementById('statTargetTotal'),
    statCompletedHeader: document.getElementById('statCompletedHeader'),
    statPercentHeader: document.getElementById('statPercentHeader'),
    headerProgressFill: document.getElementById('headerProgressFill'),

    // Dashboard Cards
    statLoadedCount: document.getElementById('statLoadedCount'),
    loadedFractionBadge: document.getElementById('loadedFractionBadge'),
    statCompletedCount: document.getElementById('statCompletedCount'),
    statCompletedBadge: document.getElementById('statCompletedBadge'),
    statRemainingCount: document.getElementById('statRemainingCount'),
    statInfosysHighMatchCount: document.getElementById('statInfosysHighMatchCount'),
    statTopicsActive: document.getElementById('statTopicsActive'),
    statTopicCountBadge: document.getElementById('statTopicCountBadge'),

    // Ratings & Topics
    ratingDistributionBar: document.getElementById('ratingDistributionBar'),
    topicChipsContainer: document.getElementById('topicChipsContainer'),
    clearAllFiltersBtn: document.getElementById('clearAllFiltersBtn'),

    // Global Toolbar
    globalSearchInput: document.getElementById('globalSearchInput'),
    clearSearchBtn: document.getElementById('clearSearchBtn'),
    infosysFilterSelect: document.getElementById('infosysFilterSelect'),
    statusFilterSelect: document.getElementById('statusFilterSelect'),
    ratingFilterSelect: document.getElementById('ratingFilterSelect'),
    sortSelect: document.getElementById('sortSelect'),
    pageSizeSelect: document.getElementById('pageSizeSelect'),

    // View Mode Buttons
    viewModeSheet: document.getElementById('viewModeSheet'),
    viewModeCards: document.getElementById('viewModeCards'),
    viewModeFlashcard: document.getElementById('viewModeFlashcard'),

    // Results Info
    visibleCount: document.getElementById('visibleCount'),
    totalFilterCount: document.getElementById('totalFilterCount'),
    activeFilterDesc: document.getElementById('activeFilterDesc'),
    expandAllIntuitionsBtn: document.getElementById('expandAllIntuitionsBtn'),
    expandAllText: document.getElementById('expandAllText'),
    questionsContainer: document.getElementById('questionsContainer'),
    emptyState: document.getElementById('emptyState'),
    resetFiltersEmptyBtn: document.getElementById('resetFiltersEmptyBtn'),

    // Pagination
    paginationBar: document.getElementById('paginationBar'),
    prevPageBtn: document.getElementById('prevPageBtn'),
    nextPageBtn: document.getElementById('nextPageBtn'),
    pageNumbers: document.getElementById('pageNumbers'),

    // Voice Agent Controller Bar
    voiceAgentBar: document.getElementById('voiceAgentBar'),
    voiceActiveSection: document.getElementById('voiceActiveSection'),
    voiceCurrentProblem: document.getElementById('voiceCurrentProblem'),
    voicePlayPauseBtn: document.getElementById('voicePlayPauseBtn'),
    voicePlayIcon: document.getElementById('voicePlayIcon'),
    voicePlayText: document.getElementById('voicePlayText'),
    voiceStopBtn: document.getElementById('voiceStopBtn'),
    voiceRateSelect: document.getElementById('voiceRateSelect'),

    // Detail Modal Elements
    problemModal: document.getElementById('problemModal'),
    closeProblemModalBtn: document.getElementById('closeProblemModalBtn'),
    modalCloseFooterBtn: document.getElementById('modalCloseFooterBtn'),
    modalStarBtn: document.getElementById('modalStarBtn'),
    modalToggleCompleteBtn: document.getElementById('modalToggleCompleteBtn'),
    modalToggleCompleteText: document.getElementById('modalToggleCompleteText'),

    modalProblemId: document.getElementById('modalProblemId'),
    modalRatingBadge: document.getElementById('modalRatingBadge'),
    modalStatusBadge: document.getElementById('modalStatusBadge'),
    modalInfosysBadge: document.getElementById('modalInfosysBadge'),
    modalProblemTitle: document.getElementById('modalProblemTitle'),
    modalTopicsList: document.getElementById('modalTopicsList'),

    // Modal Voice Controls
    modalListenFullBtn: document.getElementById('modalListenFullBtn'),
    modalListenSummaryBtn: document.getElementById('modalListenSummaryBtn'),
    modalListenIoBtn: document.getElementById('modalListenIoBtn'),
    modalListenDryRunBtn: document.getElementById('modalListenDryRunBtn'),
    modalListenIntuitionBtn: document.getElementById('modalListenIntuitionBtn'),
    modalVoiceStopBtn: document.getElementById('modalVoiceStopBtn'),

    // Tab 1: Summary, I/O & Dry Run
    modalShortDesc: document.getElementById('modalShortDesc'),
    modalInputFormat: document.getElementById('modalInputFormat'),
    modalOutputFormat: document.getElementById('modalOutputFormat'),
    modalSampleInput: document.getElementById('modalSampleInput'),
    modalSampleOutput: document.getElementById('modalSampleOutput'),
    modalDryRunText: document.getElementById('modalDryRunText'),
    modalIntuition: document.getElementById('modalIntuition'),
    modalTimeComplexity: document.getElementById('modalTimeComplexity'),
    modalSpaceComplexity: document.getElementById('modalSpaceComplexity'),
    modalExternalLink: document.getElementById('modalExternalLink'),

    // Tab 2: Infosys Intelligence
    modalIntelRole: document.getElementById('modalIntelRole'),
    modalIntelPred: document.getElementById('modalIntelPred'),
    modalIntelLikeness: document.getElementById('modalIntelLikeness'),
    modalIntelPredScore: document.getElementById('modalIntelPredScore'),
    modalLikenessFill: document.getElementById('modalLikenessFill'),
    modalInfMatchTitle: document.getElementById('modalInfMatchTitle'),
    modalInfMatchSource: document.getElementById('modalInfMatchSource'),
    modalInfMatchStatement: document.getElementById('modalInfMatchStatement'),
    modalInfMatchPattern: document.getElementById('modalInfMatchPattern'),
    modalInfMatchReason: document.getElementById('modalInfMatchReason'),

    // Tab 3: Solution
    modalSolutionSteps: document.getElementById('modalSolutionSteps'),
    modalCodeSnippet: document.getElementById('modalCodeSnippet'),
    copyCodeBtn: document.getElementById('copyCodeBtn'),

    // Tab 4: Discussion & Notes
    modalPersonalNotesInput: document.getElementById('modalPersonalNotesInput'),
    notesSaveIndicator: document.getElementById('notesSaveIndicator'),
    modalCommentsList: document.getElementById('modalCommentsList'),
    addCommentForm: document.getElementById('addCommentForm'),
    commentAuthorInput: document.getElementById('commentAuthorInput'),
    commentTextInput: document.getElementById('commentTextInput'),
    modalDiscussionCount: document.getElementById('modalDiscussionCount'),

    // Infosys Hub Modal
    openInfosysHubBtn: document.getElementById('openInfosysHubBtn'),
    infosysHubModal: document.getElementById('infosysHubModal'),
    closeInfosysHubBtn: document.getElementById('closeInfosysHubBtn'),
    closeInfosysHubFooterBtn: document.getElementById('closeInfosysHubFooterBtn'),
    hubSearchInput: document.getElementById('hubSearchInput'),
    hubItemsList: document.getElementById('hubItemsList'),

    // Batch Ingest
    openBatchImportBtn: document.getElementById('openBatchImportBtn'),
    batchImportModal: document.getElementById('batchImportModal'),
    closeBatchImportModalBtn: document.getElementById('closeBatchImportModalBtn'),
    cancelImportBtn: document.getElementById('cancelImportBtn'),
    processImportBtn: document.getElementById('processImportBtn'),
    batchJsonInput: document.getElementById('batchJsonInput'),
    importFeedbackMsg: document.getElementById('importFeedbackMsg'),
    copyFormatTemplateBtn: document.getElementById('copyFormatTemplateBtn'),

    // Export & Sound
    exportDataBtn: document.getElementById('exportDataBtn'),
    exportCsvBtn: document.getElementById('exportCsvBtn'),
    soundToggleBtn: document.getElementById('soundToggleBtn'),
    soundIcon: document.getElementById('soundIcon'),
    confettiCanvas: document.getElementById('confettiCanvas')
  };

  // --- Initializer ---
  function init() {
    loadPreferences();
    loadData();
    calculateInfosysMatches();
    setupEventListeners();
    setupVoiceAgentCallbacks();
    setupConfetti();
    renderAll();
  }

  function loadPreferences() {
    const savedSound = localStorage.getItem(STORAGE_KEYS.SOUND);
    if (savedSound !== null) {
      soundEnabled = savedSound === 'true';
    }
    updateSoundUI();
  }

  function loadData() {
    const stored = localStorage.getItem(STORAGE_KEYS.QUESTIONS);
    const initial = window.INITIAL_QUESTIONS ? [...window.INITIAL_QUESTIONS] : [];

    if (stored) {
      try {
        const parsed = JSON.parse(stored);
        if (Array.isArray(parsed) && parsed.length >= initial.length) {
          allQuestions = parsed;
        } else {
          // Merge: ensure all initial questions are included
          const qMap = new Map();
          initial.forEach(q => qMap.set(q.id, q));
          if (Array.isArray(parsed)) {
            parsed.forEach(q => qMap.set(q.id, { ...(qMap.get(q.id) || {}), ...q }));
          }
          allQuestions = Array.from(qMap.values());
          saveQuestions();
        }
      } catch (err) {
        allQuestions = initial;
      }
    } else {
      allQuestions = initial;
      saveQuestions();
    }

    try {
      completedMap = JSON.parse(localStorage.getItem(STORAGE_KEYS.COMPLETED) || '{}');
      starredMap = JSON.parse(localStorage.getItem(STORAGE_KEYS.STARRED) || '{}');
      notesMap = JSON.parse(localStorage.getItem(STORAGE_KEYS.NOTES) || '{}');
      customDiscussionsMap = JSON.parse(localStorage.getItem(STORAGE_KEYS.DISCUSSIONS) || '{}');
    } catch (e) {}
  }

  function saveQuestions() {
    try {
      localStorage.setItem(STORAGE_KEYS.QUESTIONS, JSON.stringify(allQuestions));
    } catch (e) {}
  }

  function saveCompletedMap() {
    try {
      localStorage.setItem(STORAGE_KEYS.COMPLETED, JSON.stringify(completedMap));
    } catch (e) {}
  }

  function saveStarredMap() {
    try {
      localStorage.setItem(STORAGE_KEYS.STARRED, JSON.stringify(starredMap));
    } catch (e) {}
  }

  function saveNotesMap() {
    try {
      localStorage.setItem(STORAGE_KEYS.NOTES, JSON.stringify(notesMap));
    } catch (e) {}
  }

  function saveCustomDiscussions() {
    try {
      localStorage.setItem(STORAGE_KEYS.DISCUSSIONS, JSON.stringify(customDiscussionsMap));
    } catch (e) {}
  }

  // --- Infosys Match Calculation Engine ---
  function calculateInfosysMatches() {
    if (!window.InfosysMatcher) return;
    allQuestions.forEach(q => {
      q.matchData = window.InfosysMatcher.matchQuestion(q);
    });
  }

  // --- Web Audio Chime ---
  let audioCtx = null;
  function playSuccessChime() {
    if (!soundEnabled) return;
    try {
      const AudioContextClass = window.AudioContext || window.webkitAudioContext;
      if (!AudioContextClass) return;
      if (!audioCtx) audioCtx = new AudioContextClass();
      if (audioCtx.state === 'suspended') audioCtx.resume();

      const now = audioCtx.currentTime;
      const notes = [523.25, 659.25, 783.99, 1046.50];
      notes.forEach((freq, idx) => {
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(freq, now + idx * 0.08);
        gain.gain.setValueAtTime(0.001, now + idx * 0.08);
        gain.gain.exponentialRampToValueAtTime(0.18, now + idx * 0.08 + 0.02);
        gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.08 + 0.35);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start(now + idx * 0.08);
        osc.stop(now + idx * 0.08 + 0.35);
      });
    } catch (e) {}
  }

  function updateSoundUI() {
    if (el.soundIcon) {
      el.soundIcon.textContent = soundEnabled ? '🔊' : '🔇';
      el.soundToggleBtn.setAttribute('title', soundEnabled ? 'Sound active (click to mute)' : 'Sound muted');
    }
  }

  // --- Confetti ---
  let confettiParticles = [];
  let confettiCtx = null;
  let confettiAnimFrame = null;

  function setupConfetti() {
    if (!el.confettiCanvas) return;
    confettiCtx = el.confettiCanvas.getContext('2d');
    resizeConfettiCanvas();
    window.addEventListener('resize', resizeConfettiCanvas);
  }

  function resizeConfettiCanvas() {
    if (!el.confettiCanvas) return;
    el.confettiCanvas.width = window.innerWidth;
    el.confettiCanvas.height = window.innerHeight;
  }

  function triggerConfetti(originX, originY) {
    const x = originX || window.innerWidth / 2;
    const y = originY || window.innerHeight / 2;
    const colors = ['#6366f1', '#06b6d4', '#10b981', '#f59e0b', '#f97316', '#ef4444'];
    for (let i = 0; i < 40; i++) {
      const angle = Math.random() * Math.PI * 2;
      const speed = Math.random() * 8 + 3;
      confettiParticles.push({
        x: x, y: y,
        vx: Math.cos(angle) * speed,
        vy: Math.sin(angle) * speed - 3,
        size: Math.random() * 7 + 4,
        color: colors[Math.floor(Math.random() * colors.length)],
        rotation: Math.random() * 360,
        rotSpeed: (Math.random() - 0.5) * 12,
        life: 1,
        decay: Math.random() * 0.02 + 0.015
      });
    }
    if (!confettiAnimFrame) updateConfetti();
  }

  function updateConfetti() {
    if (!confettiCtx || !el.confettiCanvas) return;
    confettiCtx.clearRect(0, 0, el.confettiCanvas.width, el.confettiCanvas.height);
    for (let i = confettiParticles.length - 1; i >= 0; i--) {
      const p = confettiParticles[i];
      p.x += p.vx;
      p.y += p.vy;
      p.vy += 0.25;
      p.rotation += p.rotSpeed;
      p.life -= p.decay;
      if (p.life <= 0) {
        confettiParticles.splice(i, 1);
        continue;
      }
      confettiCtx.save();
      confettiCtx.translate(p.x, p.y);
      confettiCtx.rotate((p.rotation * Math.PI) / 180);
      confettiCtx.fillStyle = p.color;
      confettiCtx.globalAlpha = p.life;
      confettiCtx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size * 0.6);
      confettiCtx.restore();
    }
    if (confettiParticles.length > 0) {
      confettiAnimFrame = requestAnimationFrame(updateConfetti);
    } else {
      confettiAnimFrame = null;
    }
  }

  // --- Voice Agent Callbacks & Setup ---
  function setupVoiceAgentCallbacks() {
    if (!window.voiceCoach) return;

    window.voiceCoach.onStateChange = (state) => {
      if (state.isPlaying) {
        el.voiceAgentBar.classList.add('speaking');
        el.voicePlayIcon.textContent = '⏸';
        el.voicePlayText.textContent = 'Pause';
        const sectionName = {
          summary: 'Summary & Scope',
          io: 'Input & Output Specifications',
          dryrun: 'Step-by-Step Dry Run',
          intuition: 'Aha! Intuition & Complexity',
          all: 'Full Audio Lesson'
        }[state.section] || 'Narrating';
        el.voiceActiveSection.textContent = `Reading: ${sectionName}`;
        if (state.question) {
          el.voiceCurrentProblem.textContent = `${state.question.id} • ${state.question.name}`;
          activeVoiceQuestion = state.question;
        }
      } else if (state.isPaused) {
        el.voiceAgentBar.classList.remove('speaking');
        el.voicePlayIcon.textContent = '▶';
        el.voicePlayText.textContent = 'Resume';
        el.voiceActiveSection.textContent = 'Paused';
      } else {
        el.voiceAgentBar.classList.remove('speaking');
        el.voicePlayIcon.textContent = '▶';
        el.voicePlayText.textContent = 'Listen';
        el.voiceActiveSection.textContent = 'Ready for narration';
      }
    };
  }

  // --- Filtering & Sorting ---
  function getFilteredQuestions() {
    return allQuestions.filter(q => {
      // 1. Search
      if (filterState.search) {
        const query = filterState.search.toLowerCase();
        const matchesId = (q.id || '').toLowerCase().includes(query);
        const matchesName = (q.name || '').toLowerCase().includes(query);
        const matchesDesc = (q.shortDescription || '').toLowerCase().includes(query);
        const matchesIntuition = (q.intuition || '').toLowerCase().includes(query);
        const matchesTopic = (q.topics || []).some(t => t.toLowerCase().includes(query));
        const matchesInf = q.matchData && (
          (q.matchData.bestMatch && q.matchData.bestMatch.title.toLowerCase().includes(query)) ||
          q.matchData.matchReason.toLowerCase().includes(query)
        );

        if (!matchesId && !matchesName && !matchesDesc && !matchesIntuition && !matchesTopic && !matchesInf) {
          return false;
        }
      }

      // 2. Topic
      if (filterState.topic !== 'all') {
        const hasTopic = (q.topics || []).some(
          t => t.toLowerCase() === filterState.topic.toLowerCase()
        );
        if (!hasTopic) return false;
      }

      // 3. Rating
      if (filterState.rating !== 'all') {
        const r = q.rating || 0;
        if (filterState.rating === '800-1100' && (r < 800 || r > 1100)) return false;
        if (filterState.rating === '1200-1400' && (r < 1200 || r > 1400)) return false;
        if (filterState.rating === '1500-1700' && (r < 1500 || r > 1700)) return false;
        if (filterState.rating === '1800-2000' && (r < 1800 || r > 2000)) return false;
        if (filterState.rating === '2100+' && r < 2100) return false;
      }

      // 4. Status
      if (filterState.status === 'completed' && !completedMap[q.id]) return false;
      if (filterState.status === 'incomplete' && completedMap[q.id]) return false;
      if (filterState.status === 'starred' && !starredMap[q.id]) return false;

      // 5. Infosys Match Filter
      if (filterState.infosys !== 'all' && q.matchData) {
        if (filterState.infosys === 'sp-high' && q.matchData.spLikeness < 75) return false;
        if (filterState.infosys === 'dse-high' && q.matchData.dseLikeness < 75) return false;
        if (filterState.infosys === 'any-high' && q.matchData.overallLikeness < 60) return false;
        if (filterState.infosys === 'hot-pred' && q.matchData.predictionIndex < 80) return false;
      }

      return true;
    }).sort((a, b) => {
      if (filterState.sort === 'likeness-desc') {
        return ((b.matchData && b.matchData.overallLikeness) || 0) - ((a.matchData && a.matchData.overallLikeness) || 0);
      }
      if (filterState.sort === 'pred-desc') {
        return ((b.matchData && b.matchData.predictionIndex) || 0) - ((a.matchData && a.matchData.predictionIndex) || 0);
      }
      if (filterState.sort === 'rating-asc') return (a.rating || 0) - (b.rating || 0);
      if (filterState.sort === 'rating-desc') return (b.rating || 0) - (a.rating || 0);
      if (filterState.sort === 'name-asc') return (a.name || '').localeCompare(b.name || '');
      return 0;
    });
  }

  function getRatingClass(rating) {
    if (!rating) return 'rating-800';
    if (rating <= 1100) return 'rating-800';
    if (rating <= 1399) return 'rating-1200';
    if (rating <= 1599) return 'rating-1400';
    if (rating <= 1899) return 'rating-1600';
    if (rating <= 2099) return 'rating-1900';
    if (rating <= 2399) return 'rating-2100';
    return 'rating-2400';
  }

  // --- Rendering UI ---
  function renderAll() {
    renderStats();
    renderRatingDistribution();
    renderTopicChips();
    renderQuestionsList();
  }

  function renderStats() {
    const totalLoaded = allQuestions.length;
    const completedCount = allQuestions.filter(q => completedMap[q.id]).length;
    const percent = totalLoaded > 0 ? Math.round((completedCount / TARGET_TOTAL) * 100) : 0;

    el.statCompletedHeader.textContent = completedCount;
    el.statTargetTotal.textContent = TARGET_TOTAL;
    el.statPercentHeader.textContent = `${percent}%`;
    el.headerProgressFill.style.width = `${Math.min(100, (completedCount / TARGET_TOTAL) * 100)}%`;

    el.statLoadedCount.textContent = totalLoaded;
    el.loadedFractionBadge.textContent = `${totalLoaded} / ${TARGET_TOTAL}`;
    el.statCompletedCount.textContent = completedCount;
    el.statCompletedBadge.textContent = `${percent}% of 1200`;
    el.statRemainingCount.textContent = Math.max(0, TARGET_TOTAL - completedCount);

    // Count problems with high Infosys match (>= 75%)
    const highMatchCount = allQuestions.filter(q => q.matchData && q.matchData.overallLikeness >= 75).length;
    el.statInfosysHighMatchCount.textContent = highMatchCount;

    const uniqueTopics = new Set();
    allQuestions.forEach(q => (q.topics || []).forEach(t => uniqueTopics.add(t.toLowerCase())));
    el.statTopicsActive.textContent = uniqueTopics.size;
    el.statTopicCountBadge.textContent = `${uniqueTopics.size} Topics`;
  }

  function renderRatingDistribution() {
    if (!el.ratingDistributionBar) return;
    const bands = [
      { key: '800-1100', label: '800-1100', color: '#9ca3af', min: 800, max: 1100 },
      { key: '1200-1400', label: '1200-1400', color: '#22c55e', min: 1200, max: 1400 },
      { key: '1500-1700', label: '1500-1700', color: '#06b6d4', min: 1500, max: 1700 },
      { key: '1800-2000', label: '1800-2000', color: '#3b82f6', min: 1800, max: 2000 },
      { key: '2100+', label: '2100+', color: '#ef4444', min: 2100, max: 9999 }
    ];

    el.ratingDistributionBar.innerHTML = '';
    bands.forEach(band => {
      const count = allQuestions.filter(q => {
        const r = q.rating || 0;
        return r >= band.min && r <= band.max;
      }).length;

      const pill = document.createElement('div');
      pill.className = `rating-pill-stat ${filterState.rating === band.key ? 'active' : ''}`;
      pill.innerHTML = `
        <span class="rating-dot" style="background-color: ${band.color};"></span>
        <span>${band.label}</span>
        <span class="count">${count}</span>
      `;
      pill.addEventListener('click', () => {
        filterState.rating = filterState.rating === band.key ? 'all' : band.key;
        el.ratingFilterSelect.value = filterState.rating;
        currentPage = 1;
        renderAll();
      });
      el.ratingDistributionBar.appendChild(pill);
    });
  }

  function renderTopicChips() {
    if (!el.topicChipsContainer) return;
    const topicCounts = {};
    allQuestions.forEach(q => {
      (q.topics || []).forEach(t => {
        const norm = t.toLowerCase();
        topicCounts[norm] = (topicCounts[norm] || 0) + 1;
      });
    });

    const sortedTopics = Object.keys(topicCounts).sort((a, b) => topicCounts[b] - topicCounts[a]);
    el.topicChipsContainer.innerHTML = '';

    const allChip = document.createElement('div');
    allChip.className = `topic-chip ${filterState.topic === 'all' ? 'active' : ''}`;
    allChip.innerHTML = `All <span class="count">(${allQuestions.length})</span>`;
    allChip.addEventListener('click', () => {
      filterState.topic = 'all';
      currentPage = 1;
      renderAll();
    });
    el.topicChipsContainer.appendChild(allChip);

    sortedTopics.forEach(top => {
      const chip = document.createElement('div');
      chip.className = `topic-chip ${filterState.topic === top ? 'active' : ''}`;
      chip.innerHTML = `${top} <span class="count">(${topicCounts[top]})</span>`;
      chip.addEventListener('click', () => {
        filterState.topic = filterState.topic === top ? 'all' : top;
        currentPage = 1;
        renderAll();
      });
      el.topicChipsContainer.appendChild(chip);
    });

    const hasFilters = filterState.search || filterState.topic !== 'all' || filterState.rating !== 'all' || filterState.status !== 'all' || filterState.infosys !== 'all';
    el.clearAllFiltersBtn.style.display = hasFilters ? 'inline-block' : 'none';
  }

  function renderQuestionsList() {
    const filtered = getFilteredQuestions();
    const total = filtered.length;

    el.totalFilterCount.textContent = total;
    el.activeFilterDesc.textContent = filterState.infosys !== 'all' ? `Infosys: ${filterState.infosys}` : (filterState.topic !== 'all' ? `Topic: ${filterState.topic}` : '');

    if (total === 0) {
      el.questionsContainer.innerHTML = '';
      el.emptyState.style.display = 'block';
      el.paginationBar.style.display = 'none';
      el.visibleCount.textContent = '0';
      return;
    }

    el.emptyState.style.display = 'none';

    const effectivePageSize = pageSize === 1200 ? total : pageSize;
    const totalPages = Math.ceil(total / effectivePageSize);
    if (currentPage > totalPages) currentPage = totalPages;
    if (currentPage < 1) currentPage = 1;

    const startIndex = (currentPage - 1) * effectivePageSize;
    const endIndex = Math.min(startIndex + effectivePageSize, total);
    const paginated = filtered.slice(startIndex, endIndex);

    el.visibleCount.textContent = `${startIndex + 1}-${endIndex}`;

    if (currentView === 'sheet') {
      renderSheetView(paginated);
    } else if (currentView === 'cards') {
      renderCardsView(paginated);
    } else if (currentView === 'flashcard') {
      renderFlashcardsView(paginated);
    }

    renderPagination(totalPages);
  }

  // --- View Mode 1: Memory Sheet Table ---
  function renderSheetView(questions) {
    el.questionsContainer.className = 'questions-view-sheet';

    let tableHtml = `
      <table class="sheet-table">
        <thead>
          <tr>
            <th class="checkbox-cell" title="Mark Solved">✓</th>
            <th style="width: 32px;">★</th>
            <th style="width: 85px;">ID & Rating</th>
            <th style="width: 140px;">Infosys Match</th>
            <th>Problem Name & Topics</th>
            <th style="width: 40%;">Core Intuition & Short Description</th>
            <th style="text-align: right; width: 160px;">Actions</th>
          </tr>
        </thead>
        <tbody>
    `;

    questions.forEach(q => {
      const isCompleted = !!completedMap[q.id];
      const isStarred = !!starredMap[q.id];
      const ratingClass = getRatingClass(q.rating);
      const discussionCount = getDiscussionCount(q);

      const m = q.matchData || {};
      const matchBadgeClass = m.targetExam === 'DSE' ? 'dse' : 'hot';
      const matchLabel = m.targetExam === 'SP' ? `🔥 SP ${m.spLikeness}%` : (m.targetExam === 'DSE' ? `⚡ DSE ${m.dseLikeness}%` : `🎯 Match ${m.overallLikeness}%`);

      const topicsHtml = (q.topics || [])
        .map(t => `<span class="micro-topic-tag" data-topic="${t}">${t}</span>`)
        .join('');

      tableHtml += `
        <tr class="sheet-row ${isCompleted ? 'completed-row' : ''}" data-id="${q.id}">
          <td class="checkbox-cell">
            <button class="custom-checkbox-btn ${isCompleted ? 'checked' : ''}" data-toggle-complete="${q.id}" title="${isCompleted ? 'Mark incomplete' : 'Mark completed'}">
              ✓
            </button>
          </td>
          <td>
            <button class="star-btn ${isStarred ? 'starred' : ''}" data-toggle-star="${q.id}">
              ${isStarred ? '★' : '☆'}
            </button>
          </td>
          <td>
            <div style="display: flex; flex-direction: column; gap: 3px;">
              <span class="problem-cf-id">${escapeHtml(q.id || 'CF')}</span>
              <span class="rating-badge ${ratingClass}">${q.rating || 800}</span>
            </div>
          </td>
          <td>
            <div style="display: flex; flex-direction: column; gap: 4px;">
              <span class="badge-infosys-match ${matchBadgeClass}" title="${escapeHtml(m.matchReason || '')}">
                ${matchLabel}
              </span>
              <span style="font-size: 0.68rem; font-family: var(--font-mono); color: var(--text-dim);">
                Pred: ${m.predictionIndex || 70}%
              </span>
            </div>
          </td>
          <td>
            <div class="problem-title-cell">
              <div class="problem-link-group">
                <a class="problem-name-link" data-open-detail="${q.id}">
                  ${escapeHtml(q.name || 'Untitled Problem')}
                </a>
                <a href="${q.link || `https://codeforces.com/problemset/problem/${q.contestId}/${q.index}`}" target="_blank" rel="noopener noreferrer" class="cf-direct-icon" title="Open on Codeforces">
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
                </a>
              </div>
              <div class="table-topics-list">${topicsHtml}</div>
            </div>
          </td>
          <td>
            <div class="intuition-preview-container">
              <div class="short-desc-text">
                ${escapeHtml(q.shortDescription || '')}
              </div>
              <div class="intuition-reveal-box ${showAllIntuitions ? '' : 'hidden'}" data-toggle-blur="${q.id}">
                💡 <strong>Intuition:</strong> ${escapeHtml(q.intuition || 'Click for solution details.')}
              </div>
            </div>
          </td>
          <td style="text-align: right;">
            <div class="table-action-btns" style="justify-content: flex-end;">
              <button class="btn-listen-micro" data-listen-q="${q.id}" title="Listen to Voice Agent Dry Run">
                🎙️ Listen
              </button>
              <button class="discussion-counter-badge" data-open-discussion="${q.id}">
                💬 ${discussionCount}
              </button>
              <button class="btn-open-detail" data-open-detail="${q.id}">
                Solution
              </button>
            </div>
          </td>
        </tr>
      `;
    });

    tableHtml += `</tbody></table>`;
    el.questionsContainer.innerHTML = tableHtml;
    attachQuestionInteractions();
  }

  // --- View Mode 2: Cards Grid View ---
  function renderCardsView(questions) {
    el.questionsContainer.className = 'questions-view-cards';

    let cardsHtml = '';
    questions.forEach(q => {
      const isCompleted = !!completedMap[q.id];
      const isStarred = !!starredMap[q.id];
      const ratingClass = getRatingClass(q.rating);
      const discussionCount = getDiscussionCount(q);

      const m = q.matchData || {};
      const matchBadgeClass = m.targetExam === 'DSE' ? 'dse' : 'hot';
      const matchLabel = m.targetExam === 'SP' ? `🔥 SP ${m.spLikeness}%` : (m.targetExam === 'DSE' ? `⚡ DSE ${m.dseLikeness}%` : `🎯 Match ${m.overallLikeness}%`);

      const topicsHtml = (q.topics || [])
        .map(t => `<span class="micro-topic-tag" data-topic="${t}">${t}</span>`)
        .join('');

      cardsHtml += `
        <div class="study-card ${isCompleted ? 'completed' : ''}" data-id="${q.id}">
          <div class="card-top">
            <div class="card-title-group">
              <div style="display: flex; align-items: center; gap: 0.5rem; flex-wrap: wrap;">
                <span class="problem-cf-id">${escapeHtml(q.id)}</span>
                <span class="rating-badge ${ratingClass}">${q.rating || 800}</span>
                <span class="badge-infosys-match ${matchBadgeClass}">${matchLabel}</span>
              </div>
              <div class="card-title" data-open-detail="${q.id}">${escapeHtml(q.name)}</div>
            </div>
            <div style="display: flex; align-items: center; gap: 0.35rem;">
              <button class="star-btn ${isStarred ? 'starred' : ''}" data-toggle-star="${q.id}">
                ${isStarred ? '★' : '☆'}
              </button>
              <button class="custom-checkbox-btn ${isCompleted ? 'checked' : ''}" data-toggle-complete="${q.id}">
                ✓
              </button>
            </div>
          </div>

          <div class="card-topics">${topicsHtml}</div>
          <p class="short-desc-text">${escapeHtml(q.shortDescription || '')}</p>

          <div class="card-intuition-snippet">
            <strong>Aha! Intuition:</strong> ${escapeHtml(q.intuition || '')}
          </div>

          <div class="card-footer">
            <button class="btn-listen-micro" data-listen-q="${q.id}">
              🎙️ Listen Dry Run
            </button>
            <button class="discussion-counter-badge" data-open-discussion="${q.id}">
              💬 <span>${discussionCount}</span>
            </button>
            <button class="btn-open-detail" data-open-detail="${q.id}">
              Full Solution &rarr;
            </button>
          </div>
        </div>
      `;
    });

    el.questionsContainer.innerHTML = cardsHtml;
    attachQuestionInteractions();
  }

  // --- View Mode 3: Active Recall Flashcards ---
  function renderFlashcardsView(questions) {
    el.questionsContainer.className = 'questions-view-flashcards';

    let flashcardsHtml = '';
    questions.forEach(q => {
      const isCompleted = !!completedMap[q.id];
      const ratingClass = getRatingClass(q.rating);
      const m = q.matchData || {};

      flashcardsHtml += `
        <div class="flashcard" data-flashcard-id="${q.id}">
          <div class="flashcard-inner">
            <div class="flashcard-front">
              <div>
                <div class="flashcard-prompt-hint">Memory Sheet Prompt</div>
                <div style="margin: 0.75rem 0; display: flex; align-items: center; justify-content: center; gap: 0.45rem;">
                  <span class="problem-cf-id">${escapeHtml(q.id)}</span>
                  <span class="rating-badge ${ratingClass}">${q.rating || 800}</span>
                  <span class="badge-infosys-match">${m.targetExam || 'SP/DSE'}</span>
                </div>
                <h3 style="color: #fff; font-size: 1.15rem; margin-bottom: 0.75rem;">${escapeHtml(q.name)}</h3>
                <p style="font-size: 0.8rem; color: var(--text-muted); line-height: 1.5;">${escapeHtml(q.shortDescription || '')}</p>
              </div>
              <div class="flashcard-click-flip">Click or tap to reveal intuition ↷</div>
            </div>

            <div class="flashcard-back">
              <div>
                <div class="flashcard-prompt-hint" style="color: #34d399;">Core Pattern & Solution</div>
                <p style="font-size: 0.85rem; color: #e0e7ff; margin-top: 0.75rem; line-height: 1.55;">
                  ${escapeHtml(q.intuition || q.solution || '')}
                </p>
              </div>
              <div style="display: flex; justify-content: space-between; align-items: center; margin-top: auto;">
                <button class="btn-listen-micro" data-listen-q="${q.id}">🎙️ Listen</button>
                <button class="custom-checkbox-btn ${isCompleted ? 'checked' : ''}" data-toggle-complete="${q.id}">✓</button>
                <button class="btn-open-detail" data-open-detail="${q.id}">Deep Dive &rarr;</button>
              </div>
            </div>
          </div>
        </div>
      `;
    });

    el.questionsContainer.innerHTML = flashcardsHtml;
    attachQuestionInteractions();

    document.querySelectorAll('.flashcard').forEach(card => {
      card.addEventListener('click', (e) => {
        if (e.target.closest('button')) return;
        card.classList.toggle('flipped');
      });
    });
  }

  // --- Attach Handlers ---
  function attachQuestionInteractions() {
    document.querySelectorAll('[data-toggle-complete]').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const id = btn.getAttribute('data-toggle-complete');
        toggleCompletion(id, e.clientX, e.clientY);
      });
    });

    document.querySelectorAll('[data-toggle-star]').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const id = btn.getAttribute('data-toggle-star');
        toggleStar(id);
      });
    });

    document.querySelectorAll('[data-open-detail]').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const id = btn.getAttribute('data-open-detail');
        openProblemModal(id, 'tabIntuition');
      });
    });

    document.querySelectorAll('[data-open-discussion]').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const id = btn.getAttribute('data-open-discussion');
        openProblemModal(id, 'tabDiscussion');
      });
    });

    document.querySelectorAll('[data-listen-q]').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const id = btn.getAttribute('data-listen-q');
        const q = allQuestions.find(item => item.id === id);
        if (q && window.voiceCoach) {
          activeVoiceQuestion = q;
          window.voiceCoach.readSection(q, 'all');
        }
      });
    });

    document.querySelectorAll('.micro-topic-tag').forEach(tag => {
      tag.addEventListener('click', (e) => {
        e.stopPropagation();
        const topic = tag.getAttribute('data-topic');
        filterState.topic = topic;
        currentPage = 1;
        renderAll();
      });
    });

    document.querySelectorAll('[data-toggle-blur]').forEach(box => {
      box.addEventListener('click', () => {
        box.classList.toggle('hidden');
      });
    });
  }

  // --- Completion & Star ---
  function toggleCompletion(id, clientX, clientY) {
    completedMap[id] = !completedMap[id];
    saveCompletedMap();

    if (completedMap[id]) {
      playSuccessChime();
      triggerConfetti(clientX, clientY);
    }

    renderStats();
    renderQuestionsList();

    if (activeModalQuestion && activeModalQuestion.id === id) {
      updateModalCompletionState();
    }
  }

  function toggleStar(id) {
    starredMap[id] = !starredMap[id];
    saveStarredMap();
    renderStats();
    renderQuestionsList();

    if (activeModalQuestion && activeModalQuestion.id === id) {
      el.modalStarBtn.classList.toggle('starred', !!starredMap[id]);
      el.modalStarBtn.textContent = starredMap[id] ? '★' : '☆';
    }
  }

  // --- Pagination Render ---
  function renderPagination(totalPages) {
    if (totalPages <= 1) {
      el.paginationBar.style.display = 'none';
      return;
    }
    el.paginationBar.style.display = 'flex';
    el.prevPageBtn.disabled = currentPage === 1;
    el.nextPageBtn.disabled = currentPage === totalPages;

    let pagesHtml = '';
    const maxVisiblePages = 5;
    let startPage = Math.max(1, currentPage - 2);
    let endPage = Math.min(totalPages, startPage + maxVisiblePages - 1);
    if (endPage - startPage < maxVisiblePages - 1) {
      startPage = Math.max(1, endPage - maxVisiblePages + 1);
    }

    if (startPage > 1) {
      pagesHtml += `<button class="page-num" data-page="1">1</button>`;
      if (startPage > 2) pagesHtml += `<span style="color: var(--text-dim);">...</span>`;
    }

    for (let p = startPage; p <= endPage; p++) {
      pagesHtml += `<button class="page-num ${p === currentPage ? 'active' : ''}" data-page="${p}">${p}</button>`;
    }

    if (endPage < totalPages) {
      if (endPage < totalPages - 1) pagesHtml += `<span style="color: var(--text-dim);">...</span>`;
      pagesHtml += `<button class="page-num" data-page="${totalPages}">${totalPages}</button>`;
    }

    el.pageNumbers.innerHTML = pagesHtml;

    el.pageNumbers.querySelectorAll('.page-num').forEach(btn => {
      btn.addEventListener('click', () => {
        currentPage = parseInt(btn.getAttribute('data-page'), 10);
        renderQuestionsList();
        window.scrollTo({ top: el.questionsContainer.offsetTop - 80, behavior: 'smooth' });
      });
    });
  }

  // --- Deep Dive Modal ---
  function openProblemModal(problemId, initialTab = 'tabIntuition') {
    const q = allQuestions.find(item => item.id === problemId);
    if (!q) return;
    activeModalQuestion = q;
    activeVoiceQuestion = q;

    // Header Info
    el.modalProblemId.textContent = q.id;
    el.modalProblemTitle.textContent = q.name || 'Untitled Problem';
    el.modalRatingBadge.className = `badge-cf-rating ${getRatingClass(q.rating)}`;
    el.modalRatingBadge.textContent = q.rating || 'Unrated';

    const m = q.matchData || {};
    el.modalInfosysBadge.textContent = m.targetExam === 'SP' ? `🔥 SP Match: ${m.spLikeness}%` : (m.targetExam === 'DSE' ? `⚡ DSE Match: ${m.dseLikeness}%` : `🎯 Likeness: ${m.overallLikeness}%`);

    el.modalTopicsList.innerHTML = (q.topics || [])
      .map(t => `<span class="micro-topic-tag">${escapeHtml(t)}</span>`)
      .join('');

    el.modalStarBtn.classList.toggle('starred', !!starredMap[q.id]);
    el.modalStarBtn.textContent = starredMap[q.id] ? '★' : '☆';
    updateModalCompletionState();

    // Tab 1: Summary, I/O & Dry Run
    el.modalShortDesc.textContent = q.shortDescription || 'No description provided.';
    el.modalInputFormat.textContent = q.inputFormat || 'Refer to problem statement on Codeforces.';
    el.modalOutputFormat.textContent = q.outputFormat || 'Standard format.';
    el.modalSampleInput.textContent = q.sampleInput || 'Not specified.';
    el.modalSampleOutput.textContent = q.sampleOutput || 'Not specified.';
    el.modalDryRunText.textContent = q.dryRun || (q.intuition ? `Dry Run Logic: ${q.intuition}` : 'Walkthrough available in audio coach.');
    el.modalIntuition.textContent = q.intuition || 'Focus on invariant reduction.';
    el.modalTimeComplexity.textContent = q.timeComplexity || 'O(N)';
    el.modalSpaceComplexity.textContent = q.spaceComplexity || 'O(1)';
    const cfUrl = q.link || (q.contestId && q.index ? `https://codeforces.com/problemset/problem/${q.contestId}/${q.index}` : '#');
    el.modalExternalLink.href = cfUrl;

    // Tab 2: Infosys Intelligence
    el.modalIntelRole.textContent = `Target Exam: ${m.targetExam === 'BOTH' ? 'Infosys SP & DSE' : 'Infosys ' + m.targetExam}`;
    el.modalIntelPred.textContent = `${m.predictionTier || 'HOT 🔥'} (${m.predictionIndex || 90}%)`;
    el.modalIntelLikeness.textContent = `${m.overallLikeness || 85}%`;
    el.modalIntelPredScore.textContent = `${m.predictionIndex || 90}%`;
    el.modalLikenessFill.style.width = `${m.overallLikeness || 80}%`;

    if (m.bestMatch) {
      el.modalInfMatchTitle.textContent = m.bestMatch.title;
      el.modalInfMatchSource.textContent = `${m.bestMatch.role} • ${m.bestMatch.source}`;
      el.modalInfMatchStatement.textContent = m.bestMatch.problemStatement;
      el.modalInfMatchPattern.textContent = m.bestMatch.keyPattern;
      el.modalInfMatchReason.textContent = m.matchReason;
    } else {
      el.modalInfMatchTitle.textContent = "General Infosys Algorithm Problem Pattern";
      el.modalInfMatchSource.textContent = "Infosys Coding Syllabus";
      el.modalInfMatchStatement.textContent = "Matches standard Infosys online assessment questions in this topic.";
      el.modalInfMatchPattern.textContent = "Data structure and algorithmic reasoning.";
      el.modalInfMatchReason.textContent = m.matchReason || "Algorithmic alignment.";
    }

    // Tab 3: Solution & Code
    el.modalSolutionSteps.textContent = q.solution || 'Algorithm breakdown not provided yet.';
    renderModalCode();

    // Tab 4: Discussion & Notes
    el.modalPersonalNotesInput.value = notesMap[q.id] || '';
    renderModalComments();

    switchModalTab(initialTab);
    el.problemModal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function updateModalCompletionState() {
    if (!activeModalQuestion) return;
    const isCompleted = !!completedMap[activeModalQuestion.id];
    el.modalStatusBadge.textContent = isCompleted ? 'Completed ✓' : 'Incomplete';
    el.modalStatusBadge.className = `status-pill ${isCompleted ? 'completed' : ''}`;

    el.modalToggleCompleteBtn.classList.toggle('completed', isCompleted);
    el.modalToggleCompleteText.textContent = isCompleted ? 'Completed (Click to uncheck)' : 'Mark as Completed';
  }

  function renderModalCode() {
    if (!activeModalQuestion) return;
    const codeObj = activeModalQuestion.code || {};
    const snippet = codeObj[activeCodeLang] || '// Code snippet not added yet for this language.';
    el.modalCodeSnippet.textContent = snippet;
    el.modalCodeSnippet.className = `language-${activeCodeLang}`;
  }

  function renderModalComments() {
    if (!activeModalQuestion) return;
    const defaultComments = activeModalQuestion.discussion || [];
    const customComments = customDiscussionsMap[activeModalQuestion.id] || [];
    const combined = [...defaultComments, ...customComments];

    el.modalDiscussionCount.textContent = combined.length;

    if (combined.length === 0) {
      el.modalCommentsList.innerHTML = `
        <div style="font-size: 0.8rem; color: var(--text-dim); text-align: center; padding: 1.5rem;">
          No discussion notes yet. Be the first to share an observation below!
        </div>
      `;
      return;
    }

    el.modalCommentsList.innerHTML = combined.map(c => `
      <div class="comment-card">
        <div class="comment-meta">
          <span class="comment-author">${escapeHtml(c.author || 'Anonymous')}</span>
          <span class="comment-date">${escapeHtml(c.date || 'Recent')}</span>
        </div>
        <div class="comment-body">${escapeHtml(c.text)}</div>
      </div>
    `).join('');
  }

  function getDiscussionCount(q) {
    const def = (q.discussion || []).length;
    const cust = (customDiscussionsMap[q.id] || []).length;
    return def + cust;
  }

  function switchModalTab(tabId) {
    document.querySelectorAll('.modal-tab-btn').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-tab') === tabId);
    });
    document.querySelectorAll('.modal-tab-pane').forEach(pane => {
      pane.classList.toggle('active', pane.id === tabId);
    });
  }

  function closeProblemModal() {
    el.problemModal.classList.remove('active');
    document.body.style.overflow = '';
    activeModalQuestion = null;
  }

  // --- Infosys Intelligence Hub Explorer ---
  function openInfosysHubModal() {
    renderHubItems();
    el.infosysHubModal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeInfosysHubModal() {
    el.infosysHubModal.classList.remove('active');
    document.body.style.overflow = '';
  }

  function renderHubItems(query = '') {
    const db = window.INFOSYS_QUESTION_DB || [];
    const q = query.toLowerCase().trim();

    const filtered = db.filter(item => {
      if (!q) return true;
      return item.title.toLowerCase().includes(q) ||
        item.problemStatement.toLowerCase().includes(q) ||
        item.source.toLowerCase().includes(q) ||
        (item.topics || []).some(t => t.toLowerCase().includes(q));
    });

    if (filtered.length === 0) {
      el.hubItemsList.innerHTML = `<div style="text-align: center; color: var(--text-dim); padding: 2rem;">No Infosys questions match your search.</div>`;
      return;
    }

    el.hubItemsList.innerHTML = filtered.map(item => `
      <div class="hub-item-card">
        <div class="hub-item-top">
          <span class="hub-item-title">${escapeHtml(item.title)}</span>
          <span class="hub-item-role ${item.examType.toLowerCase()}">${item.examType} (${item.year})</span>
        </div>
        <div style="font-size: 0.72rem; color: var(--accent-cyan);">${escapeHtml(item.source)} • Difficulty: ${escapeHtml(item.difficulty)}</div>
        <p class="hub-item-desc">${escapeHtml(item.problemStatement)}</p>
        <div style="font-size: 0.78rem; color: #fdba74; background: rgba(249, 115, 22, 0.08); padding: 0.35rem 0.6rem; border-radius: 4px;">
          <strong>Core Pattern:</strong> ${escapeHtml(item.keyPattern)}
        </div>
      </div>
    `).join('');
  }

  // --- Batch Import Ingestion Engine ---
  function openBatchImportModal() {
    el.batchJsonInput.value = '';
    el.importFeedbackMsg.textContent = '';
    el.importFeedbackMsg.className = 'import-feedback-msg';
    el.batchImportModal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeBatchImportModal() {
    el.batchImportModal.classList.remove('active');
    document.body.style.overflow = '';
  }

  function handleBatchImport() {
    const raw = el.batchJsonInput.value.trim();
    if (!raw) {
      showImportFeedback('Please paste your questions JSON data or list.', 'error');
      return;
    }

    try {
      let parsed = JSON.parse(raw);
      if (!Array.isArray(parsed)) {
        if (typeof parsed === 'object') {
          if (Array.isArray(parsed.questions)) parsed = parsed.questions;
          else parsed = [parsed];
        } else {
          showImportFeedback('Input must be a JSON array of questions.', 'error');
          return;
        }
      }

      if (parsed.length === 0) {
        showImportFeedback('The array contains 0 questions.', 'error');
        return;
      }

      const sanitized = parsed.map((item, idx) => ({
        id: String(item.id || item.problemId || `Q${allQuestions.length + idx + 1}`).trim(),
        contestId: item.contestId || (item.id ? parseInt(item.id) : null),
        index: item.index || (item.id ? item.id.replace(/[0-9]/g, '') : 'A'),
        name: String(item.name || item.title || 'Untitled Problem').trim(),
        rating: parseInt(item.rating, 10) || 800,
        topics: Array.isArray(item.topics) ? item.topics : (item.tags || ['general']),
        shortDescription: item.shortDescription || item.desc || item.summary || 'Summary not provided.',
        inputFormat: item.inputFormat || "Standard input format.",
        outputFormat: item.outputFormat || "Standard output format.",
        sampleInput: item.sampleInput || "Provided in problem statement.",
        sampleOutput: item.sampleOutput || "Provided in problem statement.",
        dryRun: item.dryRun || item.simulation || (item.intuition ? `Dry run simulation: ${item.intuition}` : null),
        intuition: item.intuition || item.approach || item.observation || 'Intuition not provided yet.',
        solution: item.solution || item.steps || 'Solution breakdown not provided.',
        timeComplexity: item.timeComplexity || 'O(N)',
        spaceComplexity: item.spaceComplexity || 'O(1)',
        link: item.link || (item.contestId && item.index ? `https://codeforces.com/problemset/problem/${item.contestId}/${item.index}` : '#'),
        code: item.code || {
          cpp: item.cpp || '// C++ snippet pending',
          python: item.python || '# Python snippet pending'
        },
        discussion: Array.isArray(item.discussion) ? item.discussion : []
      }));

      const mode = document.querySelector('input[name="importMode"]:checked').value;

      if (mode === 'replace') {
        allQuestions = sanitized;
      } else {
        const existingIds = new Set(allQuestions.map(q => q.id));
        sanitized.forEach(q => {
          if (existingIds.has(q.id)) {
            const idx = allQuestions.findIndex(x => x.id === q.id);
            allQuestions[idx] = { ...allQuestions[idx], ...q };
          } else {
            allQuestions.push(q);
            existingIds.add(q.id);
          }
        });
      }

      // Re-run Infosys matcher on imported questions
      calculateInfosysMatches();

      saveQuestions();
      renderAll();
      showImportFeedback(`Successfully imported ${sanitized.length} questions! (Total now: ${allQuestions.length})`, 'success');

      setTimeout(() => {
        closeBatchImportModal();
      }, 1200);

    } catch (err) {
      showImportFeedback(`JSON Parse Error: ${err.message}. Make sure the JSON is valid.`, 'error');
    }
  }

  function showImportFeedback(msg, type) {
    el.importFeedbackMsg.textContent = msg;
    el.importFeedbackMsg.className = `import-feedback-msg ${type}`;
  }

  // --- Export Data Backup ---
  function exportDataBackup() {
    const backup = {
      exportedAt: new Date().toISOString(),
      targetTotal: TARGET_TOTAL,
      questionsCount: allQuestions.length,
      questions: allQuestions,
      completedMap: completedMap,
      starredMap: starredMap,
      personalNotes: notesMap,
      customDiscussions: customDiscussionsMap
    };

    const blob = new Blob([JSON.stringify(backup, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `codeforces_1200_memory_sheet_backup_${new Date().toISOString().slice(0, 10)}.json`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }

  // --- Export CSV Spreadsheet with Infosys Matches ---
  function exportCsvSpreadsheet() {
    const rows = [
      [
        "Problem ID", "Problem Name", "CF Rating", "Topics", "Brief Question Summary",
        "Core Intuition", "Solution Algorithm", "Dry Run Trace", "Time Complexity", "Space Complexity",
        "Nearest Infosys ID", "Nearest Infosys Title", "Target Exam", "Likeliness %", "Prediction Index %",
        "Prediction Tier", "Match Reason", "CF Link"
      ]
    ];

    allQuestions.forEach(q => {
      const m = q.matchData || (window.InfosysMatcher ? window.InfosysMatcher.matchQuestion(q) : {});
      const best = m.bestMatch || {};
      rows.push([
        q.id,
        q.name,
        q.rating,
        (q.topics || []).join('; '),
        q.shortDescription,
        q.intuition,
        q.solution,
        q.dryRun,
        q.timeComplexity,
        q.spaceComplexity,
        best.id || 'N/A',
        best.title || 'N/A',
        m.targetExam || 'SP',
        m.overallLikeness || 0,
        m.predictionIndex || 0,
        m.predictionTier || 'MODERATE',
        m.matchReason || '',
        q.link || ''
      ]);
    });

    const csvContent = rows.map(r => r.map(val => `"${String(val || '').replace(/"/g, '""')}"`).join(',')).join('\r\n');
    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `infosys_cf_dp_matched_master_${new Date().toISOString().slice(0, 10)}.csv`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }

  // --- Setup Event Listeners ---
  function setupEventListeners() {
    // 1. Search Bar
    el.globalSearchInput.addEventListener('input', (e) => {
      filterState.search = e.target.value;
      el.clearSearchBtn.style.display = filterState.search ? 'block' : 'none';
      currentPage = 1;
      renderAll();
    });

    el.clearSearchBtn.addEventListener('click', () => {
      filterState.search = '';
      el.globalSearchInput.value = '';
      el.clearSearchBtn.style.display = 'none';
      currentPage = 1;
      renderAll();
    });

    // 2. Select Filters
    el.infosysFilterSelect.addEventListener('change', (e) => {
      filterState.infosys = e.target.value;
      currentPage = 1;
      renderAll();
    });

    el.statusFilterSelect.addEventListener('change', (e) => {
      filterState.status = e.target.value;
      currentPage = 1;
      renderAll();
    });

    el.ratingFilterSelect.addEventListener('change', (e) => {
      filterState.rating = e.target.value;
      currentPage = 1;
      renderAll();
    });

    el.sortSelect.addEventListener('change', (e) => {
      filterState.sort = e.target.value;
      currentPage = 1;
      renderAll();
    });

    el.pageSizeSelect.addEventListener('change', (e) => {
      pageSize = parseInt(e.target.value, 10);
      currentPage = 1;
      renderAll();
    });

    // 3. Clear All Filters
    const clearFiltersHandler = () => {
      filterState = {
        search: '',
        topic: 'all',
        rating: 'all',
        status: 'all',
        infosys: 'all',
        sort: 'default'
      };
      el.globalSearchInput.value = '';
      el.clearSearchBtn.style.display = 'none';
      el.infosysFilterSelect.value = 'all';
      el.statusFilterSelect.value = 'all';
      el.ratingFilterSelect.value = 'all';
      el.sortSelect.value = 'default';
      currentPage = 1;
      renderAll();
    };

    el.clearAllFiltersBtn.addEventListener('click', clearFiltersHandler);
    el.resetFiltersEmptyBtn.addEventListener('click', clearFiltersHandler);

    // 4. View Mode Switcher
    el.viewModeSheet.addEventListener('click', () => setViewMode('sheet'));
    el.viewModeCards.addEventListener('click', () => setViewMode('cards'));
    el.viewModeFlashcard.addEventListener('click', () => setViewMode('flashcard'));

    // 5. Expand / Collapse intuitions
    el.expandAllIntuitionsBtn.addEventListener('click', () => {
      showAllIntuitions = !showAllIntuitions;
      el.expandAllText.textContent = showAllIntuitions ? 'Hide All Intuitions' : 'Show All Intuitions';
      document.querySelectorAll('.intuition-reveal-box').forEach(box => {
        box.classList.toggle('hidden', !showAllIntuitions);
      });
    });

    // 6. Pagination Prev / Next
    el.prevPageBtn.addEventListener('click', () => {
      if (currentPage > 1) {
        currentPage--;
        renderQuestionsList();
        window.scrollTo({ top: el.questionsContainer.offsetTop - 80, behavior: 'smooth' });
      }
    });

    el.nextPageBtn.addEventListener('click', () => {
      const filtered = getFilteredQuestions();
      const effectivePageSize = pageSize === 1200 ? filtered.length : pageSize;
      const totalPages = Math.ceil(filtered.length / effectivePageSize);
      if (currentPage < totalPages) {
        currentPage++;
        renderQuestionsList();
        window.scrollTo({ top: el.questionsContainer.offsetTop - 80, behavior: 'smooth' });
      }
    });

    // 7. Global Voice Agent Bar Controls
    el.voicePlayPauseBtn.addEventListener('click', () => {
      if (!window.voiceCoach) return;
      if (window.voiceCoach.isPlaying && !window.voiceCoach.isPaused) {
        window.voiceCoach.pause();
      } else if (window.voiceCoach.isPaused) {
        window.voiceCoach.resume();
      } else {
        const targetQ = activeVoiceQuestion || activeModalQuestion || allQuestions[0];
        if (targetQ) window.voiceCoach.readSection(targetQ, 'all');
      }
    });

    el.voiceStopBtn.addEventListener('click', () => {
      if (window.voiceCoach) window.voiceCoach.stop();
    });

    document.querySelectorAll('[data-voice-jump]').forEach(btn => {
      btn.addEventListener('click', () => {
        const sec = btn.getAttribute('data-voice-jump');
        const targetQ = activeVoiceQuestion || activeModalQuestion || allQuestions[0];
        if (targetQ && window.voiceCoach) {
          window.voiceCoach.readSection(targetQ, sec);
        }
      });
    });

    el.voiceRateSelect.addEventListener('change', (e) => {
      if (window.voiceCoach) window.voiceCoach.setRate(e.target.value);
    });

    // 8. Modal Voice Controls
    el.modalListenFullBtn.addEventListener('click', () => {
      if (activeModalQuestion && window.voiceCoach) window.voiceCoach.readSection(activeModalQuestion, 'all');
    });
    el.modalListenSummaryBtn.addEventListener('click', () => {
      if (activeModalQuestion && window.voiceCoach) window.voiceCoach.readSection(activeModalQuestion, 'summary');
    });
    el.modalListenIoBtn.addEventListener('click', () => {
      if (activeModalQuestion && window.voiceCoach) window.voiceCoach.readSection(activeModalQuestion, 'io');
    });
    el.modalListenDryRunBtn.addEventListener('click', () => {
      if (activeModalQuestion && window.voiceCoach) window.voiceCoach.readSection(activeModalQuestion, 'dryrun');
    });
    el.modalListenIntuitionBtn.addEventListener('click', () => {
      if (activeModalQuestion && window.voiceCoach) window.voiceCoach.readSection(activeModalQuestion, 'intuition');
    });
    el.modalVoiceStopBtn.addEventListener('click', () => {
      if (window.voiceCoach) window.voiceCoach.stop();
    });

    // 9. Modal Tabs
    document.querySelectorAll('.modal-tab-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const tab = btn.getAttribute('data-tab');
        switchModalTab(tab);
      });
    });

    // 10. Code Language Switcher
    document.querySelectorAll('.code-tab-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.code-tab-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        activeCodeLang = btn.getAttribute('data-lang');
        renderModalCode();
      });
    });

    // 11. Copy Code
    el.copyCodeBtn.addEventListener('click', () => {
      const code = el.modalCodeSnippet.textContent;
      navigator.clipboard.writeText(code).then(() => {
        const origText = el.copyCodeBtn.querySelector('span').textContent;
        el.copyCodeBtn.querySelector('span').textContent = 'Copied!';
        setTimeout(() => el.copyCodeBtn.querySelector('span').textContent = origText, 1500);
      });
    });

    // 12. Modal Star & Complete
    el.modalStarBtn.addEventListener('click', () => {
      if (activeModalQuestion) toggleStar(activeModalQuestion.id);
    });

    el.modalToggleCompleteBtn.addEventListener('click', (e) => {
      if (activeModalQuestion) toggleCompletion(activeModalQuestion.id, e.clientX, e.clientY);
    });

    el.closeProblemModalBtn.addEventListener('click', closeProblemModal);
    el.modalCloseFooterBtn.addEventListener('click', closeProblemModal);
    el.problemModal.addEventListener('click', (e) => {
      if (e.target === el.problemModal) closeProblemModal();
    });

    // 13. Personal Notes Auto-save
    let notesTimeout = null;
    el.modalPersonalNotesInput.addEventListener('input', (e) => {
      if (!activeModalQuestion) return;
      el.notesSaveIndicator.textContent = 'Saving...';
      clearTimeout(notesTimeout);
      notesTimeout = setTimeout(() => {
        notesMap[activeModalQuestion.id] = e.target.value;
        saveNotesMap();
        el.notesSaveIndicator.textContent = 'Auto-saved ✓';
      }, 400);
    });

    // 14. Discussion Comment Submit
    el.addCommentForm.addEventListener('submit', (e) => {
      e.preventDefault();
      if (!activeModalQuestion) return;

      const author = el.commentAuthorInput.value.trim() || 'Anonymous';
      const text = el.commentTextInput.value.trim();
      if (!text) return;

      if (!customDiscussionsMap[activeModalQuestion.id]) {
        customDiscussionsMap[activeModalQuestion.id] = [];
      }

      customDiscussionsMap[activeModalQuestion.id].push({
        id: 'cd_' + Date.now(),
        author: author,
        date: new Date().toISOString().slice(0, 10),
        text: text
      });

      saveCustomDiscussions();
      el.commentTextInput.value = '';
      renderModalComments();
      renderQuestionsList();
    });

    // 15. Infosys Hub Modal Handlers
    el.openInfosysHubBtn.addEventListener('click', openInfosysHubModal);
    el.closeInfosysHubBtn.addEventListener('click', closeInfosysHubModal);
    el.closeInfosysHubFooterBtn.addEventListener('click', closeInfosysHubModal);
    el.infosysHubModal.addEventListener('click', (e) => {
      if (e.target === el.infosysHubModal) closeInfosysHubModal();
    });
    el.hubSearchInput.addEventListener('input', (e) => {
      renderHubItems(e.target.value);
    });

    // 16. Batch Ingest Handlers
    el.openBatchImportBtn.addEventListener('click', openBatchImportModal);
    el.closeBatchImportModalBtn.addEventListener('click', closeBatchImportModal);
    el.cancelImportBtn.addEventListener('click', closeBatchImportModal);
    el.batchImportModal.addEventListener('click', (e) => {
      if (e.target === el.batchImportModal) closeBatchImportModal();
    });
    el.processImportBtn.addEventListener('click', handleBatchImport);

    el.copyFormatTemplateBtn.addEventListener('click', () => {
      const template = `[
  {
    "id": "1800E2",
    "name": "Unforgivable Curse (hard)",
    "rating": 1400,
    "topics": ["graphs", "greedy"],
    "shortDescription": "Swap chars at distance k or k+1. Determine if s becomes t.",
    "sampleInput": "1\\n6 3\\ntalant\\natlant",
    "sampleOutput": "YES",
    "dryRun": "Indices that reach each other in steps of k and k+1 form connected components...",
    "intuition": "Characters can freely permute in connected components if multiset matches.",
    "solution": "Check immutable positions first, then test if multiset matches.",
    "timeComplexity": "O(n)",
    "spaceComplexity": "O(1)",
    "link": "https://codeforces.com/problemset/problem/1800/E2"
  }
]`;
      navigator.clipboard.writeText(template).then(() => {
        el.copyFormatTemplateBtn.textContent = 'Copied!';
        setTimeout(() => el.copyFormatTemplateBtn.textContent = 'Copy Template', 1500);
      });
    });

    // 17. Export & Sound
    el.exportDataBtn.addEventListener('click', exportDataBackup);
    if (el.exportCsvBtn) {
      el.exportCsvBtn.addEventListener('click', exportCsvSpreadsheet);
    }
    el.soundToggleBtn.addEventListener('click', () => {
      soundEnabled = !soundEnabled;
      localStorage.setItem(STORAGE_KEYS.SOUND, String(soundEnabled));
      updateSoundUI();
    });

    // 18. Keyboard shortcuts
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        if (el.problemModal.classList.contains('active')) closeProblemModal();
        if (el.batchImportModal.classList.contains('active')) closeBatchImportModal();
        if (el.infosysHubModal.classList.contains('active')) closeInfosysHubModal();
      }
      if (e.key === '/' && document.activeElement !== el.globalSearchInput && !document.querySelector('.modal-overlay.active')) {
        e.preventDefault();
        el.globalSearchInput.focus();
      }
    });
  }

  function setViewMode(mode) {
    currentView = mode;
    el.viewModeSheet.classList.toggle('active', mode === 'sheet');
    el.viewModeCards.classList.toggle('active', mode === 'cards');
    el.viewModeFlashcard.classList.toggle('active', mode === 'flashcard');
    renderQuestionsList();
  }

  function escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
