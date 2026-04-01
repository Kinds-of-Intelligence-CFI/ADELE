document.addEventListener('DOMContentLoaded', function () {
  initNavbar();
  initSmoothScrolling();
  initScrollSpy();
  initDimensionTabs();
  initLLMSelector();
  initScrollAnimations();
});

/* ---------- Navbar ---------- */
function initNavbar() {
  var navbar = document.getElementById('adele-navbar');
  if (!navbar) return;

  // Burger toggle (mobile)
  var burger = navbar.querySelector('.navbar-burger');
  var menu = navbar.querySelector('.navbar-menu');
  if (burger && menu) {
    burger.addEventListener('click', function () {
      burger.classList.toggle('is-active');
      menu.classList.toggle('is-active');
    });
  }

  // Scroll shadow
  window.addEventListener('scroll', function () {
    navbar.classList.toggle('is-scrolled', window.scrollY > 10);
  }, { passive: true });
}

/* ---------- Smooth Scrolling ---------- */
function initSmoothScrolling() {
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      var href = this.getAttribute('href');
      if (href === '#') return;
      var target = document.querySelector(href);
      if (target) {
        e.preventDefault();
        var nav = document.getElementById('adele-navbar');
        var navHeight = nav ? nav.offsetHeight : 0;
        var top = target.getBoundingClientRect().top + window.pageYOffset - navHeight - 16;
        window.scrollTo({ top: top, behavior: 'smooth' });

        // Close mobile menu
        var burger = document.querySelector('.navbar-burger');
        var menu = document.querySelector('.navbar-menu');
        if (burger) burger.classList.remove('is-active');
        if (menu) menu.classList.remove('is-active');
      }
    });
  });
}

/* ---------- Scroll Spy ---------- */
function initScrollSpy() {
  var sections = document.querySelectorAll('section[id]');
  var navItems = document.querySelectorAll('#adele-navbar .navbar-menu .navbar-item[href^="#"]');
  if (!sections.length || !navItems.length) return;

  var nav = document.getElementById('adele-navbar');
  var navHeight = nav ? nav.offsetHeight : 0;

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        navItems.forEach(function (item) { item.classList.remove('is-active'); });
        var link = document.querySelector('#adele-navbar .navbar-item[href="#' + entry.target.id + '"]');
        if (link) link.classList.add('is-active');
      }
    });
  }, {
    rootMargin: '-' + (navHeight + 20) + 'px 0px -55% 0px',
    threshold: 0
  });

  sections.forEach(function (section) { observer.observe(section); });
}

/* ---------- Dimension Tabs ---------- */
function initDimensionTabs() {
  var buttons = document.querySelectorAll('.dimension-tabs .tab-btn');
  var rubrics = document.querySelectorAll('#dimension-rubrics .rubric');
  if (!buttons.length) return;

  function selectDimension(btn) {
    buttons.forEach(function (b) { b.classList.remove('is-active'); });
    btn.classList.add('is-active');

    var targetId = btn.getAttribute('data-target');
    rubrics.forEach(function (rubric) {
      if (rubric.id === targetId) {
        rubric.style.display = 'block';
        rubric.style.opacity = '0';
        requestAnimationFrame(function () {
          rubric.style.transition = 'opacity 250ms ease';
          rubric.style.opacity = '1';
        });
      } else {
        rubric.style.display = 'none';
        rubric.style.opacity = '0';
      }
    });
  }

  buttons.forEach(function (btn) {
    btn.addEventListener('click', function () { selectDimension(btn); });
  });

}

/* ---------- LLM Selector ---------- */
function initLLMSelector() {
  var buttons = document.querySelectorAll('.llm-selector-grid .llm-btn');
  var containers = document.querySelectorAll('#LLM-rubrics .LLM');
  if (!buttons.length) return;

  function selectLLM(btn) {
    buttons.forEach(function (b) { b.classList.remove('is-active'); });
    btn.classList.add('is-active');

    var targetId = btn.getAttribute('data-target');
    containers.forEach(function (container) {
      if (container.id === targetId) {
        container.style.display = 'block';
        container.style.opacity = '0';
        requestAnimationFrame(function () {
          container.style.transition = 'opacity 250ms ease';
          container.style.opacity = '1';
        });
      } else {
        container.style.display = 'none';
        container.style.opacity = '0';
      }
    });
  }

  buttons.forEach(function (btn) {
    btn.addEventListener('click', function () { selectLLM(btn); });
  });

  // Auto-select "All LLMs" button
  if (buttons.length > 0) {
    selectLLM(buttons[0]);
  }
}

/* ---------- Levels Toggle ---------- */
function toggleLevels(show) {
  var cards = document.querySelectorAll('.rubric-card');
  cards.forEach(function (card) {
    if (show) {
      card.classList.add('show-levels');
    } else {
      card.classList.remove('show-levels');
    }
  });
}

/* ---------- Scroll Animations ---------- */
function initScrollAnimations() {
  var elements = document.querySelectorAll('.animate-on-scroll');
  if (!elements.length) return;

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

  elements.forEach(function (el) { observer.observe(el); });
}
