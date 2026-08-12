// ============================================
// CFA Level I Preparation System — Script
// v3.0 — JSON-first question renderer
// ============================================

// =========== STATE ===========
let currentFile = 'home';
const contentBody = document.getElementById('contentBody');
const breadcrumb  = document.getElementById('breadcrumb');
const navTree     = document.getElementById('navTree');
const searchInput = document.getElementById('searchInput');

// Files that contain questions and have a matching .json counterpart
const QUESTION_FILES = new Set([
  'mock-exams/mock-exam-1-am',
  'mock-exams/mock-exam-1-pm',
  'question-bank/questions/01-ethics/standards-i-vii',
  'question-bank/questions/02-quantitative-methods/quantitative-methods-questions',
  'question-bank/questions/03-economics/economics-questions',
  'question-bank/questions/04-financial-statement-analysis/fsa-questions',
  'question-bank/questions/05-corporate-issuers/corporate-issuers-questions',
  'question-bank/questions/06-equity-investments/equity-questions',
  'question-bank/questions/07-fixed-income/fixed-income-questions',
  'question-bank/questions/08-derivatives/derivatives-questions',
  'question-bank/questions/09-alternative-investments/alternative-investments-questions',
  'question-bank/questions/10-portfolio-management/portfolio-management-questions',
]);

// =========== INITIALIZATION ===========
(function init() {
  loadContent('home', document.querySelector('[data-file="home"]'));
  loadDarkModePreference();
})();

// =========== CONTENT LOADING ===========
async function loadContent(file, linkElement, event) {
  if (event) event.preventDefault();

  document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
  if (linkElement) linkElement.classList.add('active');

  currentFile = file;
  contentBody.innerHTML = '<div class="loading">Loading...</div>';

  try {
    if (file === 'home') {
      renderHome();
      breadcrumb.textContent = 'Dashboard';
    } else if (QUESTION_FILES.has(file)) {
      // ── JSON-first path: load questions from structured JSON ──────────────
      await loadQuestionsFromJSON(file);
      breadcrumb.textContent = file.replace(/\//g, ' › ').replace(/-/g, ' ');
    } else {
      // ── Markdown path: for all non-question content (formulas, curriculum, etc.)
      await loadMarkdownContent(file);
      breadcrumb.textContent = file.replace(/\//g, ' › ').replace(/-/g, ' ');
    }

    document.querySelector('.content').scrollTop = 0;

    if (window.innerWidth <= 768) closeSidebar();

  } catch (err) {
    contentBody.innerHTML = `
      <div style="text-align:center;padding:60px 20px;">
        <h2 style="color:var(--orange);">📡 File Not Available Locally</h2>
        <p style="color:var(--text-muted);margin:12px 0;">Could not load: <code>${file}</code></p>
        <p style="color:var(--text-muted);font-size:0.85rem;">This file works on GitHub Pages. The local preview only shows the Dashboard.</p>
        <div style="margin-top:20px;">
          <a class="quick-link" onclick="loadContent('home', this)" style="display:inline-block;">← Back to Dashboard</a>
        </div>
      </div>
    `;
    breadcrumb.textContent = 'Preview Unavailable';
  }
}

// =========== JSON QUESTION LOADER ===========
async function loadQuestionsFromJSON(file) {
  const jsonUrl = `${file}.json`;
  const response = await fetch(jsonUrl);
  if (!response.ok) throw new Error(`JSON not found: ${jsonUrl}`);
  const data = await response.json();
  renderQuestionsFromJSON(data);
}

function renderQuestionsFromJSON(data) {
  const questions = data.questions || [];
  const total = questions.length;

  // ── Progress bar ──────────────────────────────────────────────────────────
  const progressBar = `
    <div class="exam-progress-bar" id="examProgressBar">
      <div class="exam-progress-info">
        <span>🎯 Interactive Exam Practice Mode</span>
        <span class="exam-progress-badge" id="examProgressCount">0 / ${total} Answered</span>
        <span class="exam-score-badge" id="examScoreCount">Score: 0%</span>
      </div>
      <button class="exam-reset-all-btn" onclick="resetAllExamQuestions()">🔄 Reset All</button>
    </div>
  `;

  // ── Page title ────────────────────────────────────────────────────────────
  let html = `${progressBar}<h1>${escHtml(data.title || 'Question Bank')}</h1>`;

  // ── Group questions by section ────────────────────────────────────────────
  const sections = [];
  const sectionMap = {};
  questions.forEach(q => {
    const sec = q.section || 'General';
    if (!sectionMap[sec]) {
      sectionMap[sec] = [];
      sections.push(sec);
    }
    sectionMap[sec].push(q);
  });

  sections.forEach(sec => {
    const qs = sectionMap[sec];
    html += `<h2 class="section-heading">${escHtml(sec)}</h2>`;
    qs.forEach((q, idx) => {
      html += buildQuestionCard(q, idx);
    });
  });

  contentBody.innerHTML = html;

  // ── Run KaTeX on the content ──────────────────────────────────────────────
  if (typeof renderMathInElement === 'function') {
    renderMathInElement(contentBody, {
      delimiters: [
        { left: '$$', right: '$$', display: true },
        { left: '\\(', right: '\\)', display: false },
        { left: '\\[', right: '\\]', display: true }
      ],
      throwOnError: false
    });
  }
}

function buildQuestionCard(q, idx) {
  const diffColor = ['', '#22c55e', '#84cc16', '#eab308', '#f97316', '#ef4444'][q.difficulty] || '#6366f1';
  const diffStars = '★'.repeat(q.difficulty) + '☆'.repeat(5 - q.difficulty);

  const optA = escHtml(q.options.A || '');
  const optB = escHtml(q.options.B || '');
  const optC = escHtml(q.options.C || '');
  const correct = (q.correct || 'A').toUpperCase();

  // Wrong analysis: render bullet list items
  let wrongHtml = '';
  if (q.wrongAnalysis) {
    const lines = q.wrongAnalysis.split('\n').filter(l => l.trim());
    wrongHtml = lines.map(l => `<li>${escHtml(l.replace(/^[-•*]\s*/, ''))}</li>`).join('');
    wrongHtml = `<ul class="wrong-list">${wrongHtml}</ul>`;
  }

  return `
    <div class="interactive-question-card" data-correct="${correct}" id="q-card-${escHtml(q.id)}">
      <div class="q-card-header">
        <span class="q-id-badge">${escHtml(q.id)}</span>
        <span class="q-meta-badge difficulty" style="border-left:3px solid ${diffColor}">
          Difficulty: ${q.difficulty}/5 &nbsp;${diffStars}
        </span>
        <span class="q-meta-badge">⏱️ ${escHtml(q.time || '90s')}</span>
        <span class="q-meta-badge">${escHtml(q.pattern || '')}</span>
        ${q.trap ? `<span class="q-meta-badge trap-badge">⚠️ ${escHtml(q.trap)}</span>` : ''}
        <span class="q-status-badge status-unanswered">UNANSWERED</span>
      </div>

      <div class="q-stem">${escHtml(q.stem || '')}</div>

      <div class="q-options-container">
        ${optA ? `
        <button class="q-option-btn" onclick="selectQuestionOption(this,'A')">
          <span class="opt-letter">A</span>
          <span class="opt-text">${optA}</span>
        </button>` : ''}
        ${optB ? `
        <button class="q-option-btn" onclick="selectQuestionOption(this,'B')">
          <span class="opt-letter">B</span>
          <span class="opt-text">${optB}</span>
        </button>` : ''}
        ${optC ? `
        <button class="q-option-btn" onclick="selectQuestionOption(this,'C')">
          <span class="opt-letter">C</span>
          <span class="opt-text">${optC}</span>
        </button>` : ''}
      </div>

      <div class="q-explanation-box" style="display:none;">
        <div class="exp-header correct-title">
          <span class="exp-icon">✔</span> Correct Answer: Option ${correct}
        </div>
        ${q.explanation ? `
        <div class="exp-section">
          <h4>📖 Detailed Explanation</h4>
          <p>${escHtml(q.explanation)}</p>
        </div>` : ''}
        ${q.wrongAnalysis ? `
        <div class="exp-section">
          <h4>❌ Why the Other Options Are Wrong</h4>
          ${wrongHtml}
        </div>` : ''}
        <div class="exp-footer">
          ${q.lo ? `<span class="lo-tag">📌 ${escHtml(q.lo)}</span>` : ''}
          <button class="q-reset-btn" onclick="resetQuestionCard(this)">🔄 Retry Question</button>
        </div>
      </div>
    </div>
  `;
}

function escHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

// =========== MARKDOWN CONTENT LOADER (non-question files) ===========
async function loadMarkdownContent(file) {
  if (typeof marked === 'undefined') {
    contentBody.innerHTML = '<div style="text-align:center;padding:60px;color:var(--red);"><h2>⚠️ Renderer Not Loaded</h2><p>Failed to load the markdown renderer.</p></div>';
    return;
  }
  const response = await fetch(`${file}.md`);
  if (!response.ok) throw new Error(`File not found: ${file}.md`);
  const markdown = await response.text();
  const html = marked.parse(markdown);
  contentBody.innerHTML = html;

  if (typeof renderMathInElement === 'function') {
    renderMathInElement(contentBody, {
      delimiters: [
        { left: '$$', right: '$$', display: true },
        { left: '\\(', right: '\\)', display: false },
        { left: '\\[', right: '\\]', display: true }
      ],
      throwOnError: false
    });
  }
}

// =========== HOME DASHBOARD ===========
function renderHome() {
  contentBody.innerHTML = `
    <div class="home-dashboard">
      <div class="home-hero">
        <h1>CFA Level I<br>Complete Preparation System</h1>
        <p class="subtitle">12 question files · 629+ original questions · 144 formulas · 222 Learning Outcomes</p>
        <span class="target">🎯 Target: 90%+ Preparation Coverage</span>
      </div>

      <div class="stat-grid">
        <div class="stat-card">
          <div class="stat-number">10/10</div>
          <div class="stat-label">Subjects Covered</div>
        </div>
        <div class="stat-card">
          <div class="stat-number">222</div>
          <div class="stat-label">Learning Outcomes</div>
        </div>
        <div class="stat-card">
          <div class="stat-number">629+</div>
          <div class="stat-label">Original Questions</div>
        </div>
        <div class="stat-card">
          <div class="stat-number">144</div>
          <div class="stat-label">Formulas</div>
        </div>
        <div class="stat-card">
          <div class="stat-number">70+</div>
          <div class="stat-label">Common Traps</div>
        </div>
        <div class="stat-card">
          <div class="stat-number">5</div>
          <div class="stat-label">Difficulty Levels</div>
        </div>
      </div>

      <h2>The Five Pillars</h2>
      <div class="pillar-grid">
        <div class="pillar-card">
          <h3>🔴 Error Bank</h3>
          <p>Every mistake becomes a future question. Personal database of "questions designed to catch me."</p>
        </div>
        <div class="pillar-card">
          <h3>🧩 Pattern Bank</h3>
          <p>Record how questions are constructed. Recognize the pattern when CFA changes numbers or wording.</p>
        </div>
        <div class="pillar-card">
          <h3>⭐ Mastery System</h3>
          <p>"I got 8/10" isn't enough. Prove you can solve it two weeks later under time pressure.</p>
        </div>
        <div class="pillar-card">
          <h3>📊 Readiness Dashboard</h3>
          <p>Confidence through evidence: Curriculum 100%, Concepts 96%, Formulas 93%, Readiness: Strong.</p>
        </div>
        <div class="pillar-card">
          <h3>🛡️ Anti-Overfitting</h3>
          <p>Recurring concepts + reasoning patterns + traps. Not memorizing previous questions.</p>
        </div>
      </div>

      <h2>Quick Navigation</h2>
      <div class="quick-links">
        <a class="quick-link" onclick="loadContent('question-bank/questions/01-ethics/standards-i-vii', this)">📝 Ethics Questions (75)</a>
        <a class="quick-link" onclick="loadContent('question-bank/questions/02-quantitative-methods/quantitative-methods-questions', this)">📐 Quantitative Methods (78)</a>
        <a class="quick-link" onclick="loadContent('question-bank/questions/03-economics/economics-questions', this)">🌍 Economics (65)</a>
        <a class="quick-link" onclick="loadContent('question-bank/questions/04-financial-statement-analysis/fsa-questions', this)">📊 Financial Statement Analysis (57)</a>
        <a class="quick-link" onclick="loadContent('question-bank/questions/05-corporate-issuers/corporate-issuers-questions', this)">🏢 Corporate Issuers (43)</a>
        <a class="quick-link" onclick="loadContent('question-bank/questions/06-equity-investments/equity-questions', this)">📈 Equity Investments (46)</a>
        <a class="quick-link" onclick="loadContent('question-bank/questions/07-fixed-income/fixed-income-questions', this)">💵 Fixed Income (46)</a>
        <a class="quick-link" onclick="loadContent('question-bank/questions/08-derivatives/derivatives-questions', this)">🔀 Derivatives (48)</a>
        <a class="quick-link" onclick="loadContent('question-bank/questions/09-alternative-investments/alternative-investments-questions', this)">🏗️ Alternative Investments (39)</a>
        <a class="quick-link" onclick="loadContent('question-bank/questions/10-portfolio-management/portfolio-management-questions', this)">📋 Portfolio Management (42)</a>
        <a class="quick-link" onclick="loadContent('formula-bank/all-formulas', this)">🔢 Formula Bank (144)</a>
        <a class="quick-link" onclick="loadContent('mock-exams/mock-exam-1-am', this)">📝 Mock Exam 1 — AM Paper (90 Qs)</a>
        <a class="quick-link" onclick="loadContent('mock-exams/mock-exam-1-pm', this)">📝 Mock Exam 1 — PM Paper (90 Qs)</a>
        <a class="quick-link" onclick="loadContent('curriculum/coverage-matrix', this)">📋 Coverage Matrix (222 LOs)</a>
        <a class="quick-link" onclick="loadContent('pattern-library/trap-catalog', this)">⚠️ Trap Catalog (70+)</a>
        <a class="quick-link" onclick="loadContent('dashboard/tracking-system', this)">📊 Readiness Dashboard</a>
        <a class="quick-link" onclick="loadContent('protocols/final-protocols', this)">📅 Final 30-Day Protocol</a>
      </div>

      <h2>Subject Weights</h2>
      <table>
        <thead><tr><th>#</th><th>Subject</th><th>Weight</th><th>Priority</th></tr></thead>
        <tbody>
          <tr><td>1</td><td>Ethical &amp; Professional Standards</td><td>15–20%</td><td>🔴 Tier 1</td></tr>
          <tr><td>2</td><td>Financial Statement Analysis</td><td>11–14%</td><td>🔴 Tier 1</td></tr>
          <tr><td>3</td><td>Equity Investments</td><td>11–14%</td><td>🔴 Tier 1</td></tr>
          <tr><td>4</td><td>Fixed Income</td><td>11–14%</td><td>🔴 Tier 1</td></tr>
          <tr><td>5</td><td>Portfolio Management</td><td>8–12%</td><td>🟡 Tier 2</td></tr>
          <tr><td>6</td><td>Alternative Investments</td><td>7–10%</td><td>🟡 Tier 2</td></tr>
          <tr><td>7</td><td>Quantitative Methods</td><td>6–9%</td><td>🟡 Tier 2</td></tr>
          <tr><td>8</td><td>Economics</td><td>6–9%</td><td>🟡 Tier 2</td></tr>
          <tr><td>9</td><td>Corporate Issuers</td><td>6–9%</td><td>🟡 Tier 2</td></tr>
          <tr><td>10</td><td>Derivatives</td><td>5–8%</td><td>🟢 Tier 3</td></tr>
        </tbody>
      </table>
    </div>
  `;
}

// =========== SIDEBAR ===========
function toggleSidebar() {
  const sidebar = document.getElementById('sidebar');
  const overlay = document.getElementById('sidebarOverlay');
  sidebar.classList.toggle('open');
  overlay.classList.toggle('active');
}

function closeSidebar() {
  const sidebar = document.getElementById('sidebar');
  const overlay = document.getElementById('sidebarOverlay');
  sidebar.classList.remove('open');
  overlay.classList.remove('active');
}

function toggleSection(element) {
  element.classList.toggle('open');
  const sub = element.nextElementSibling;
  if (sub) sub.classList.toggle('open');
}

// =========== SEARCH ===========
function filterNav() {
  const query = searchInput.value.toLowerCase();
  const links = navTree.querySelectorAll('.nav-link');
  const sections = navTree.querySelectorAll('.nav-section');

  links.forEach(link => {
    const text = link.textContent.toLowerCase();
    const li = link.closest('li');
    if (li) li.style.display = text.includes(query) ? '' : 'none';
  });

  sections.forEach(section => {
    const visibleLinks = section.querySelectorAll('.nav-link');
    let hasVisible = false;
    visibleLinks.forEach(l => {
      if (l.closest('li') && l.closest('li').style.display !== 'none') hasVisible = true;
    });
    section.style.display = hasVisible || !query ? '' : 'none';

    if (query && hasVisible) {
      const category = section.querySelector('.nav-category');
      const sub = section.querySelector('.nav-sub');
      if (category && sub) {
        category.classList.add('open');
        sub.classList.add('open');
      }
    }
  });

  if (!query) {
    links.forEach(link => {
      const li = link.closest('li');
      if (li) li.style.display = '';
    });
    sections.forEach(section => { section.style.display = ''; });
  }
}

// =========== DARK MODE ===========
function toggleDarkMode() {
  document.body.classList.toggle('light-mode');
  const isLight = document.body.classList.contains('light-mode');
  localStorage.setItem('cfa-theme', isLight ? 'light' : 'dark');
}

function loadDarkModePreference() {
  if (localStorage.getItem('cfa-theme') === 'light') {
    document.body.classList.add('light-mode');
  }
}

// =========== UTILITY ===========
function scrollToTop() {
  document.querySelector('.content').scrollTo({ top: 0, behavior: 'smooth' });
}

document.addEventListener('keydown', (e) => {
  if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
    e.preventDefault();
    searchInput.focus();
  }
});

document.getElementById('sidebarOverlay').addEventListener('click', closeSidebar);

// =========== INTERACTIVE QUESTION ANSWER ENGINE ===========
function selectQuestionOption(button, selectedOption) {
  const card = button.closest('.interactive-question-card');
  if (!card) return;
  const correctOption  = (card.dataset.correct || 'A').toUpperCase();
  const statusBadge    = card.querySelector('.q-status-badge');
  const explanationBox = card.querySelector('.q-explanation-box');
  const expHeader      = card.querySelector('.exp-header');
  const allButtons     = card.querySelectorAll('.q-option-btn');

  // Disable all options once answered
  allButtons.forEach(btn => btn.disabled = true);

  const isCorrect = (selectedOption === correctOption);

  if (isCorrect) {
    button.classList.add('selected-correct');
    card.classList.add('answered-correct');
    statusBadge.className = 'q-status-badge status-correct';
    statusBadge.textContent = '✅ CORRECT';
    expHeader.className = 'exp-header correct-title';
    expHeader.innerHTML = '<span class="exp-icon">✔</span> Excellent! Option ' + correctOption + ' is correct.';
  } else {
    button.classList.add('selected-incorrect');
    card.classList.add('answered-incorrect');
    statusBadge.className = 'q-status-badge status-incorrect';
    statusBadge.textContent = '❌ INCORRECT';
    expHeader.className = 'exp-header incorrect-title';
    expHeader.innerHTML = '<span class="exp-icon">❌</span> Incorrect. You selected <strong>' + selectedOption + '</strong>. Correct Answer is <strong>' + correctOption + '</strong>.';

    // Highlight the correct option in green
    allButtons.forEach(btn => {
      const letterNode = btn.querySelector('.opt-letter');
      if (letterNode && letterNode.textContent.trim() === correctOption) {
        btn.classList.add('reveal-correct');
      }
    });
  }

  explanationBox.style.display = 'block';
  explanationBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  updateExamProgressTracker();
}

function resetQuestionCard(btn) {
  const card = btn.closest('.interactive-question-card');
  if (!card) return;
  const statusBadge    = card.querySelector('.q-status-badge');
  const explanationBox = card.querySelector('.q-explanation-box');
  const allButtons     = card.querySelectorAll('.q-option-btn');

  card.classList.remove('answered-correct', 'answered-incorrect');
  statusBadge.className = 'q-status-badge status-unanswered';
  statusBadge.textContent = 'UNANSWERED';
  explanationBox.style.display = 'none';

  allButtons.forEach(b => {
    b.disabled = false;
    b.classList.remove('selected-correct', 'selected-incorrect', 'reveal-correct');
  });

  updateExamProgressTracker();
}

function resetAllExamQuestions() {
  document.querySelectorAll('.interactive-question-card').forEach(card => {
    const resetBtn = card.querySelector('.q-reset-btn');
    if (resetBtn) resetQuestionCard(resetBtn);
  });
}

function updateExamProgressTracker() {
  const cards = document.querySelectorAll('.interactive-question-card');
  if (cards.length === 0) return;

  let answered = 0, correct = 0;
  cards.forEach(card => {
    if (card.classList.contains('answered-correct'))   { answered++; correct++; }
    else if (card.classList.contains('answered-incorrect')) { answered++; }
  });

  const countBadge = document.getElementById('examProgressCount');
  const scoreBadge = document.getElementById('examScoreCount');

  if (countBadge) countBadge.textContent = `${answered} / ${cards.length} Answered`;
  if (scoreBadge) {
    const pct = answered > 0 ? Math.round((correct / answered) * 100) : 0;
    scoreBadge.textContent = `Score: ${pct}% (${correct}/${answered})`;
  }
}
