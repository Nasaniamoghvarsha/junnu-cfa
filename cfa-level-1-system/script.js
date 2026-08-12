// ============================================
// CFA Level I Preparation System — Script
// ============================================

// =========== STATE ===========
let currentFile = 'home';
const contentBody = document.getElementById('contentBody');
const breadcrumb = document.getElementById('breadcrumb');
const navTree = document.getElementById('navTree');
const searchInput = document.getElementById('searchInput');

// =========== INITIALIZATION ===========
(function init() {
  loadContent('home', document.querySelector('[data-file="home"]'));
  loadDarkModePreference();
})();

// =========== CONTENT LOADING ===========
async function loadContent(file, linkElement, event) {
  if (event) event.preventDefault();

  // Update active state
  document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
  if (linkElement) linkElement.classList.add('active');

  currentFile = file;
  contentBody.innerHTML = '<div class="loading">Loading</div>';

  try {
    if (file === 'home') {
      renderHome();
      breadcrumb.textContent = 'Dashboard';
    } else {
      // Check if marked.js loaded
      if (typeof marked === 'undefined') {
        contentBody.innerHTML = '<div style="text-align:center;padding:60px 20px;color:var(--red);"><h2>⚠️ Renderer Not Loaded</h2><p>Failed to load the markdown renderer. Check your internet connection and reload the page.</p></div>';
        return;
      }
      const response = await fetch(`${file}.md`);
      if (!response.ok) throw new Error(`File not found: ${file}.md`);
      const markdown = await response.text();
      const html = marked.parse(markdown);
      contentBody.innerHTML = html;
      
      // Transform raw Markdown questions into interactive exam components
      setupInteractiveQuestions(contentBody);

      if (typeof renderMathInElement === 'function') {
        renderMathInElement(contentBody, {
          delimiters: [
            {left: '$$', right: '$$', display: true},
            {left: '\\(', right: '\\)', display: false},
            {left: '\\[', right: '\\]', display: true}
          ],
          throwOnError: false
        });
      }
      breadcrumb.textContent = file.replace(/\//g, ' › ').replace(/-/g, ' ');
    }

    // Scroll to top of content
    document.querySelector('.content').scrollTop = 0;

    // Close sidebar on mobile after navigation
    if (window.innerWidth <= 768) {
      closeSidebar();
    }

  } catch (err) {
    contentBody.innerHTML = `
      <div style="text-align:center;padding:60px 20px;">
        <h2 style="color:var(--orange);">📡 File Not Available Locally</h2>
        <p style="color:var(--text-muted);margin:12px 0;">Could not load: <code>${file}.md</code></p>
        <p style="color:var(--text-muted);font-size:0.85rem;">This file works on GitHub Pages. The local preview only shows the Dashboard.</p>
        <div style="margin-top:20px;">
          <a class="quick-link" onclick="loadContent('home', this)" style="display:inline-block;">← Back to Dashboard</a>
        </div>
      </div>
    `;
    breadcrumb.textContent = 'Preview Unavailable';
  }
}

// =========== HOME DASHBOARD ===========
function renderHome() {
  contentBody.innerHTML = `
    <div class="home-dashboard">
      <div class="home-hero">
        <h1>CFA Level I<br>Complete Preparation System</h1>
        <p class="subtitle">21 files · 150+ original questions · 144 formulas · 222 Learning Outcomes</p>
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
          <div class="stat-number">150+</div>
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
        <a class="quick-link" onclick="loadContent('question-bank/questions/01-ethics/standards-i-vii', this)">📝 Ethics Questions (20)</a>
        <a class="quick-link" onclick="loadContent('formula-bank/all-formulas', this)">🔢 Formula Bank (144)</a>
        <a class="quick-link" onclick="loadContent('curriculum/coverage-matrix', this)">📋 Coverage Matrix (222 LOs)</a>
        <a class="quick-link" onclick="loadContent('pattern-library/trap-catalog', this)">⚠️ Trap Catalog (70+)</a>
        <a class="quick-link" onclick="loadContent('dashboard/tracking-system', this)">📊 Readiness Dashboard</a>
        <a class="quick-link" onclick="loadContent('dashboard/error-bank-system', this)">🔴 Error Bank System</a>
        <a class="quick-link" onclick="loadContent('mock-exams/mock-exam-system', this)">📄 Mock Exam System</a>
        <a class="quick-link" onclick="loadContent('protocols/final-protocols', this)">📅 Final 30-Day Protocol</a>
      </div>

      <h2>Subject Weights</h2>
      <table>
        <thead><tr><th>#</th><th>Subject</th><th>Weight</th><th>Priority</th></tr></thead>
        <tbody>
          <tr><td>1</td><td>Ethical & Professional Standards</td><td>15–20%</td><td>🔴 Tier 1</td></tr>
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
      if (l.closest('li') && l.closest('li').style.display !== 'none') {
        hasVisible = true;
      }
    });
    section.style.display = hasVisible || !query ? '' : 'none';

    // Auto-expand sections with matching content
    if (query && hasVisible) {
      const category = section.querySelector('.nav-category');
      const sub = section.querySelector('.nav-sub');
      if (category && sub) {
        category.classList.add('open');
        sub.classList.add('open');
      }
    }
  });

  // Reset all items when search is cleared
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

// Keyboard shortcut: Ctrl+K for search
document.addEventListener('keydown', (e) => {
  if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
    e.preventDefault();
    searchInput.focus();
  }
});

// Close sidebar when clicking overlay
document.getElementById('sidebarOverlay').addEventListener('click', closeSidebar);

// =========== INTERACTIVE QUESTION PARSER & ENGINE ===========
function setupInteractiveQuestions(container) {
  const headers = Array.from(container.querySelectorAll('h3, h4')).filter(h => {
    const txt = h.textContent || '';
    return txt.includes('Q-') || txt.includes('Difficulty:');
  });

  if (headers.length === 0) return;

  if (!document.getElementById('examProgressBar')) {
    const progressHeader = document.createElement('div');
    progressHeader.className = 'exam-progress-bar';
    progressHeader.id = 'examProgressBar';
    progressHeader.innerHTML = `
      <div class="exam-progress-info">
        <span>🎯 Interactive Exam Practice Mode</span>
        <span class="exam-progress-badge" id="examProgressCount">0 / ${headers.length} Answered</span>
        <span class="exam-score-badge" id="examScoreCount">Score: 0%</span>
      </div>
      <button class="exam-reset-all-btn" onclick="resetAllExamQuestions()">🔄 Reset All</button>
    `;
    container.insertBefore(progressHeader, container.firstChild);
  }

  let qIndex = 0;
  headers.forEach(header => {
    try {
      qIndex++;
      const metaText = header.textContent.trim();

      let sibling = header.nextElementSibling;
      const nodesToRemove = [];
      let blockText = '';

      while (sibling && !['H2', 'H3'].includes(sibling.tagName)) {
        if (sibling.tagName === 'HR' && sibling.nextElementSibling && ['H2', 'H3'].includes(sibling.nextElementSibling.tagName)) {
          nodesToRemove.push(sibling);
          break;
        }
        nodesToRemove.push(sibling);
        blockText += (sibling.innerText || sibling.textContent || '') + '\n';
        sibling = sibling.nextElementSibling;
      }

      const idMatch = metaText.match(/Q-[A-Z0-9-]+/i);
      const qId = idMatch ? idMatch[0] : `Q-${qIndex}`;

      const diffMatch = metaText.match(/Difficulty:\s*(\d+)/i);
      const diff = diffMatch ? diffMatch[1] : '3';

      const timeMatch = metaText.match(/Time:\s*(\d+s?)/i);
      const time = timeMatch ? timeMatch[1] : '90s';

      const patternMatch = metaText.match(/Pattern:\s*([^|]+)/i);
      const pattern = patternMatch ? patternMatch[1].trim() : 'Standard';

      let stemText = '';
      const stemMatch = blockText.match(/Question:\s*([\s\S]*?)(?=A[\)\.]|B[\)\.]|C[\)\.]|Correct Answer:|$)/i);
      if (stemMatch) {
        stemText = stemMatch[1].trim();
      }

      // Smart Multi-Option Extractor (handles separate lines AND single-line options)
      const options = [];

      function cleanOptionString(s) {
        if (!s) return '';
        return s.trim()
          .replace(/^A[\)\.]?\s*/i, '')
          .replace(/^B[\)\.]?\s*/i, '')
          .replace(/^C[\)\.]?\s*/i, '')
          .replace(/\s*(?:Correct Answer:|Explanation:|Wrong Answer Analysis:).*$/i, '')
          .replace(/\n/g, ' ')
          .trim();
      }

      const optAReg = /(?:^|\s|\n)A[\)\.]?\s*([\s\S]*?)(?=(?:^|\s|\n)B[\)\.]?|Correct Answer:|$)/i;
      const optBReg = /(?:^|\s|\n)B[\)\.]?\s*([\s\S]*?)(?=(?:^|\s|\n)C[\)\.]?|Correct Answer:|$)/i;
      const optCReg = /(?:^|\s|\n)C[\)\.]?\s*([\s\S]*?)(?=(?:^|\s|\n)Correct Answer:|Explanation:|$)/i;

      const matchA = blockText.match(optAReg);
      const matchB = blockText.match(optBReg);
      const matchC = blockText.match(optCReg);

      if (matchA && cleanOptionString(matchA[1])) {
        options.push({ letter: 'A', text: cleanOptionString(matchA[1]) });
      }
      if (matchB && cleanOptionString(matchB[1])) {
        options.push({ letter: 'B', text: cleanOptionString(matchB[1]) });
      }
      if (matchC && cleanOptionString(matchC[1])) {
        options.push({ letter: 'C', text: cleanOptionString(matchC[1]) });
      }

      // Fallback line parsing
      if (options.length < 3) {
        const lineList = blockText.split('\n');
        lineList.forEach(line => {
          const m = line.trim().match(/^([A-C])[\)\.]?\s*(.*)/);
          if (m && !options.some(o => o.letter === m[1].toUpperCase())) {
            options.push({ letter: m[1].toUpperCase(), text: cleanOptionString(m[2]) });
          }
        });
      }

      options.sort((a, b) => a.letter.localeCompare(b.letter));

      const correctMatch = blockText.match(/Correct Answer:\s*([A-C])/i);
      const correctLetter = correctMatch ? correctMatch[1].toUpperCase() : 'A';

      let expText = '';
      const expMatch = blockText.match(/Explanation:\s*([\s\S]*?)(?=Wrong Answer Analysis:|LO Reference:|$)/i);
      if (expMatch) expText = expMatch[1].trim();

      let wrongText = '';
      const wrongMatch = blockText.match(/Wrong Answer Analysis:\s*([\s\S]*?)(?=LO Reference:|Related Concepts:|$)/i);
      if (wrongMatch) wrongText = wrongMatch[1].trim();

      const loMatch = blockText.match(/LO Reference:\s*([^\n]+)/i);
      const loRef = loMatch ? loMatch[1].trim() : 'CFA Curriculum';

      const card = document.createElement('div');
      card.className = 'interactive-question-card';
      card.dataset.correct = correctLetter;
      card.id = `q-card-${qIndex}`;

      card.innerHTML = `
        <div class="q-card-header">
          <span class="q-id-badge">${qId}</span>
          <span class="q-meta-badge difficulty">Difficulty: ${diff}/5</span>
          <span class="q-meta-badge">⏱️ ${time}</span>
          <span class="q-meta-badge">${pattern}</span>
          <span class="q-status-badge status-unanswered">UNANSWERED</span>
        </div>
        <div class="q-stem">${stemText || 'Question stem loading...'}</div>
        <div class="q-options-container">
          ${options.map(opt => `
            <button class="q-option-btn" onclick="selectQuestionOption(this, '${opt.letter}')">
              <span class="opt-letter">${opt.letter}</span>
              <span class="opt-text">${opt.text}</span>
            </button>
          `).join('')}
        </div>
        <div class="q-explanation-box" style="display: none;">
          <div class="exp-header correct-title">
            <span class="exp-icon">✔</span> Correct Answer: Option ${correctLetter}
          </div>
          ${expText ? `
            <div class="exp-section">
              <h4>Detailed Explanation:</h4>
              <p>${expText.replace(/\n/g, '<br>')}</p>
            </div>
          ` : ''}
          ${wrongText ? `
            <div class="exp-section">
              <h4>Wrong Answer Analysis:</h4>
              <p>${wrongText.replace(/\n/g, '<br>')}</p>
            </div>
          ` : ''}
          <div class="exp-footer">
            <span class="lo-tag">📌 ${loRef}</span>
            <button class="q-reset-btn" onclick="resetQuestionCard(this)">🔄 Retry Question</button>
          </div>
        </div>
      `;

      nodesToRemove.forEach(node => {
        if (node && node.parentNode) node.parentNode.removeChild(node);
      });

      if (header && header.parentNode) {
        header.parentNode.replaceChild(card, header);
      }
    } catch (err) {
      console.error(`Error parsing question header #${qIndex}:`, err);
    }
  });
}

function selectQuestionOption(button, selectedOption) {
  const card = button.closest('.interactive-question-card');
  const correctOption = card.dataset.correct;
  const statusBadge = card.querySelector('.q-status-badge');
  const explanationBox = card.querySelector('.q-explanation-box');
  const expHeader = card.querySelector('.exp-header');
  const allButtons = card.querySelectorAll('.q-option-btn');

  // Disable all options once answered
  allButtons.forEach(btn => btn.disabled = true);

  const isCorrect = (selectedOption === correctOption);

  if (isCorrect) {
    button.classList.add('selected-correct');
    card.classList.add('answered-correct');
    statusBadge.className = 'q-status-badge status-correct';
    statusBadge.textContent = 'CORRECT 🟢';
    expHeader.className = 'exp-header correct-title';
    expHeader.innerHTML = '<span class="exp-icon">✔</span> Excellent! Option ' + correctOption + ' is correct.';
  } else {
    button.classList.add('selected-incorrect');
    card.classList.add('answered-incorrect');
    statusBadge.className = 'q-status-badge status-incorrect';
    statusBadge.textContent = 'INCORRECT 🔴';
    expHeader.className = 'exp-header incorrect-title';
    expHeader.innerHTML = '<span class="exp-icon">❌</span> Incorrect. You selected Option ' + selectedOption + '. Correct Answer is Option ' + correctOption + '.';

    // Highlight correct option
    allButtons.forEach(btn => {
      const letterNode = btn.querySelector('.opt-letter');
      if (letterNode && letterNode.textContent.trim() === correctOption) {
        btn.classList.add('reveal-correct');
      }
    });
  }

  explanationBox.style.display = 'block';
  updateExamProgressTracker();
}

function resetQuestionCard(btn) {
  const card = btn.closest('.interactive-question-card');
  const statusBadge = card.querySelector('.q-status-badge');
  const explanationBox = card.querySelector('.q-explanation-box');
  const allButtons = card.querySelectorAll('.q-option-btn');

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

  let answered = 0;
  let correct = 0;

  cards.forEach(card => {
    if (card.classList.contains('answered-correct')) {
      answered++;
      correct++;
    } else if (card.classList.contains('answered-incorrect')) {
      answered++;
    }
  });

  const countBadge = document.getElementById('examProgressCount');
  const scoreBadge = document.getElementById('examScoreCount');

  if (countBadge) countBadge.textContent = `${answered} / ${cards.length} Answered`;
  if (scoreBadge) {
    const pct = answered > 0 ? Math.round((correct / answered) * 100) : 0;
    scoreBadge.textContent = `Score: ${pct}% (${correct}/${answered})`;
  }
}

