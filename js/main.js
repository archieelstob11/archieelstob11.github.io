// ============================================================
// Restek UK Ltd - Main JavaScript
// ============================================================

document.addEventListener("DOMContentLoaded", () => {
  initHeader();
  initMobileMenu();
  initScrollAnimations();
  initStatCounters();
  initCookieBanner();
  initBackToTop();
  initHeroParticles();
  initContactForm();
  initSmoothScroll();
});

// ---- Header Scroll Effect ----
function initHeader() {
  const header = document.getElementById("main-header");
  if (!header) return;

  let lastScroll = 0;
  const scrollThreshold = 50;

  window.addEventListener("scroll", () => {
    const currentScroll = window.pageYOffset;

    if (currentScroll > scrollThreshold) {
      header.classList.add("scrolled");
    } else {
      header.classList.remove("scrolled");
    }

    lastScroll = currentScroll;
  });
}

// ---- Mobile Menu ----
function initMobileMenu() {
  const toggle = document.getElementById("mobile-toggle");
  const menu = document.getElementById("mobile-menu");
  const body = document.body;

  if (!toggle || !menu) return;

  toggle.addEventListener("click", () => {
    toggle.classList.toggle("active");
    menu.classList.toggle("active");
    body.classList.toggle("menu-open");
  });

  // Close menu on link click
  const links = menu.querySelectorAll("a");
  links.forEach((link) => {
    link.addEventListener("click", () => {
      toggle.classList.remove("active");
      menu.classList.remove("active");
      body.classList.remove("menu-open");
    });
  });
}

// ---- Scroll Animations ----
function initScrollAnimations() {
  const elements = document.querySelectorAll(".animate-on-scroll");

  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("visible");
            observer.unobserve(entry.target);
          }
        });
      },
      {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px",
      },
    );

    elements.forEach((el) => observer.observe(el));
  } else {
    elements.forEach((el) => el.classList.add("visible"));
  }
}

// ---- Stat Counters ----
function initStatCounters() {
  const counters = document.querySelectorAll(".stat__number[data-count]");

  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            animateCounter(entry.target);
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.5 },
    );

    counters.forEach((counter) => observer.observe(counter));
  }
}

function animateCounter(el) {
  const target = parseInt(el.getAttribute("data-count"));
  const duration = 2000;
  const step = target / (duration / 16);
  let current = 0;

  const timer = setInterval(() => {
    current += step;
    if (current >= target) {
      el.textContent = target;
      clearInterval(timer);
    } else {
      el.textContent = Math.floor(current);
    }
  }, 16);
}

// ---- Cookie Banner ----
function initCookieBanner() {
  const banner = document.getElementById("cookie-banner");
  const acceptBtn = document.getElementById("cookie-accept-btn");
  const settingsBtn = document.getElementById("cookie-settings-btn");

  if (!banner) return;

  // Check if cookies already accepted
  if (localStorage.getItem("cookiesAccepted")) {
    banner.style.display = "none";
    return;
  }

  // Show banner after a short delay
  setTimeout(() => {
    banner.classList.add("visible");
  }, 1500);

  if (acceptBtn) {
    acceptBtn.addEventListener("click", () => {
      localStorage.setItem("cookiesAccepted", "true");
      banner.classList.remove("visible");
      setTimeout(() => {
        banner.style.display = "none";
      }, 500);
    });
  }

  if (settingsBtn) {
    settingsBtn.addEventListener("click", () => {
      // For now, just accept
      localStorage.setItem("cookiesAccepted", "true");
      banner.classList.remove("visible");
      setTimeout(() => {
        banner.style.display = "none";
      }, 500);
    });
  }
}

// ---- Back to Top ----
function initBackToTop() {
  const btn = document.getElementById("back-to-top");
  if (!btn) return;

  window.addEventListener("scroll", () => {
    if (window.pageYOffset > 500) {
      btn.classList.add("visible");
    } else {
      btn.classList.remove("visible");
    }
  });

  btn.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
}

// ---- Hero Particles ----
function initHeroParticles() {
  const container = document.getElementById("hero-particles");
  if (!container) return;

  for (let i = 0; i < 30; i++) {
    const particle = document.createElement("div");
    particle.className = "particle";
    particle.style.left = Math.random() * 100 + "%";
    particle.style.top = Math.random() * 100 + "%";
    particle.style.animationDelay = Math.random() * 6 + "s";
    particle.style.animationDuration = Math.random() * 4 + 3 + "s";
    particle.style.width = particle.style.height = Math.random() * 4 + 1 + "px";
    container.appendChild(particle);
  }
}

// ---- Contact Form ----
function initContactForm() {
  const form = document.getElementById("contact-form");
  if (!form) return;

  form.addEventListener("submit", (e) => {
    e.preventDefault();

    // Basic validation
    const name = form.querySelector("#contact-name");
    const email = form.querySelector("#contact-email");
    const message = form.querySelector("#contact-message");
    let valid = true;

    [name, email, message].forEach((field) => {
      if (field && !field.value.trim()) {
        field.classList.add("error");
        valid = false;
      } else if (field) {
        field.classList.remove("error");
      }
    });

    if (email && email.value && !isValidEmail(email.value)) {
      email.classList.add("error");
      valid = false;
    }

    if (valid) {
      // Show success message
      const successMsg = document.createElement("div");
      successMsg.className = "form-success";
      successMsg.innerHTML =
        '<i class="fas fa-check-circle"></i> Thank you for your message! We will get back to you soon.';
      form.appendChild(successMsg);

      // Reset form
      form.reset();

      // Remove success message after 5 seconds
      setTimeout(() => {
        successMsg.remove();
      }, 5000);
    }
  });

  // Remove error class on input
  form.querySelectorAll("input, textarea, select").forEach((field) => {
    field.addEventListener("input", () => {
      field.classList.remove("error");
    });
  });
}

function isValidEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

// ---- Smooth Scroll ----
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      const href = this.getAttribute("href");
      if (href === "#") return;

      e.preventDefault();
      const target = document.querySelector(href);
      if (target) {
        const headerOffset = 80;
        const elementPosition = target.getBoundingClientRect().top;
        const offsetPosition =
          elementPosition + window.pageYOffset - headerOffset;

        window.scrollTo({
          top: offsetPosition,
          behavior: "smooth",
        });
      }
    });
  });
}

// ---- Active Nav on Scroll ----
window.addEventListener("scroll", () => {
  const sections = document.querySelectorAll("section[id]");
  const navLinks = document.querySelectorAll(".nav__link");
  let current = "";

  sections.forEach((section) => {
    const sectionTop = section.offsetTop - 100;
    if (window.pageYOffset >= sectionTop) {
      current = section.getAttribute("id");
    }
  });
});
