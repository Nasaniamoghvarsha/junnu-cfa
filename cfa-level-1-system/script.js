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
document.addEventListener('DOMContentLoaded', () => {
  loadContent('home', document.querySelector('[data-file="home"]'));
  loadDarkModePreference();
});

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
      <div style="text-align:center;padding:60px 20px;color:var(--red);">
        <h2>⚠️ File Not Found</h2>
        <p>Could not load: ${file}.md</p>
        <p style="color:var(--text-muted);font-size:0.85rem;">${err.message}</p>
      </div>
    `;
    breadcrumb.textContent = 'Error';
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
