/* ==========================================================================
   ABYSSAL ARCHIVE — interactions
   No dependencies. Every enhancement degrades gracefully without JS.
   ========================================================================== */

(() => {
  "use strict";

  const doc = document;
  const root = doc.documentElement;
  const body = doc.body;
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ------------------------------------------------------------------------
     Header, mobile navigation and back-to-top
     ------------------------------------------------------------------------ */

  const header = doc.querySelector("[data-header]");
  const menuToggle = doc.querySelector("[data-menu-toggle]");
  const nav = doc.querySelector("#site-nav");
  let lastScroll = 0;
  let ticking = false;

  const setHeaderState = () => {
    if (!header) return;
    header.classList.toggle("is-scrolled", window.scrollY > 24);
    lastScroll = window.scrollY;
    ticking = false;
  };

  if (header) {
    setHeaderState();
    window.addEventListener(
      "scroll",
      () => {
        if (!ticking) {
          window.requestAnimationFrame(setHeaderState);
          ticking = true;
        }
      },
      { passive: true }
    );
  }

  const closeNav = () => {
    if (!body.classList.contains("nav-open")) return;
    body.classList.remove("nav-open");
    menuToggle?.setAttribute("aria-expanded", "false");
    menuToggle?.setAttribute("aria-label", "打开导航菜单");
    if (nav?.contains(document.activeElement)) menuToggle?.focus();
  };

  const openNav = () => {
    body.classList.add("nav-open");
    menuToggle?.setAttribute("aria-expanded", "true");
    menuToggle?.setAttribute("aria-label", "关闭导航菜单");
    const firstLink = nav?.querySelector("a");
    window.setTimeout(() => firstLink?.focus(), 120);
  };

  menuToggle?.addEventListener("click", () => {
    if (body.classList.contains("nav-open")) closeNav();
    else openNav();
  });

  doc.querySelectorAll("[data-nav-close]").forEach((el) => el.addEventListener("click", closeNav));
  nav?.querySelectorAll("a").forEach((link) => link.addEventListener("click", closeNav));

  doc.addEventListener("keydown", (event) => {
    if (event.key === "Escape") closeNav();
  });

  window.addEventListener("resize", () => {
    if (window.innerWidth > 960) closeNav();
  });

  doc.querySelectorAll("[data-to-top]").forEach((button) => {
    button.addEventListener("click", (event) => {
      event.preventDefault();
      window.scrollTo({ top: 0, behavior: reduceMotion ? "auto" : "smooth" });
    });
  });

  /* ------------------------------------------------------------------------
     Scroll reveal
     ------------------------------------------------------------------------ */

  const revealItems = doc.querySelectorAll("[data-reveal]");
  if (revealItems.length) {
    if (reduceMotion || !("IntersectionObserver" in window)) {
      revealItems.forEach((item) => item.classList.add("is-visible"));
    } else {
      const revealObserver = new IntersectionObserver(
        (entries, observer) => {
          entries.forEach((entry) => {
            if (!entry.isIntersecting) return;
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          });
        },
        { rootMargin: "0px 0px -8% 0px", threshold: 0.08 }
      );
      revealItems.forEach((item) => revealObserver.observe(item));
    }
  }

  /* ------------------------------------------------------------------------
     Generic quote rotators
     ------------------------------------------------------------------------ */

  doc.querySelectorAll("[data-quote-rotator]").forEach((rotator) => {
    const slides = Array.from(rotator.querySelectorAll("[data-quote-slide]"));
    if (!slides.length) return;
    const prev = rotator.querySelector("[data-quote-prev]");
    const next = rotator.querySelector("[data-quote-next]");
    const count = rotator.querySelector("[data-quote-count]");
    const autoplay = rotator.dataset.autoplay === "true";
    let index = slides.findIndex((slide) => !slide.hidden);
    if (index < 0) index = 0;
    let timer = null;

    const show = (nextIndex, userInitiated = false) => {
      index = (nextIndex + slides.length) % slides.length;
      slides.forEach((slide, slideIndex) => {
        const active = slideIndex === index;
        slide.hidden = !active;
        slide.setAttribute("aria-hidden", active ? "false" : "true");
      });
      if (count) {
        count.textContent = `${String(index + 1).padStart(2, "0")} / ${String(slides.length).padStart(2, "0")}`;
      }
      if (userInitiated) restartAutoplay();
    };

    const restartAutoplay = () => {
      if (!autoplay || reduceMotion) return;
      window.clearInterval(timer);
      timer = window.setInterval(() => show(index + 1), 9000);
    };

    prev?.addEventListener("click", () => show(index - 1, true));
    next?.addEventListener("click", () => show(index + 1, true));

    rotator.addEventListener("mouseenter", () => window.clearInterval(timer));
    rotator.addEventListener("mouseleave", restartAutoplay);
    rotator.addEventListener("focusin", () => window.clearInterval(timer));
    rotator.addEventListener("focusout", restartAutoplay);

    show(index);
    restartAutoplay();
  });

  /* ------------------------------------------------------------------------
     Tabs
     ------------------------------------------------------------------------ */

  doc.querySelectorAll("[data-tabs]").forEach((tabs) => {
    const tabButtons = Array.from(tabs.querySelectorAll('[role="tab"]'));
    const panels = Array.from(tabs.querySelectorAll('[role="tabpanel"]'));
    if (!tabButtons.length || !panels.length) return;

    const activate = (newIndex, focus = false) => {
      const safeIndex = (newIndex + tabButtons.length) % tabButtons.length;
      tabButtons.forEach((button, index) => {
        const selected = index === safeIndex;
        button.setAttribute("aria-selected", selected ? "true" : "false");
        button.tabIndex = selected ? 0 : -1;
        if (selected && focus) button.focus();
      });
      panels.forEach((panel, index) => {
        const selected = index === safeIndex;
        panel.hidden = !selected;
        panel.setAttribute("aria-hidden", selected ? "false" : "true");
      });
    };

    tabButtons.forEach((button, index) => {
      button.addEventListener("click", () => activate(index));
      button.addEventListener("keydown", (event) => {
        let nextIndex = null;
        if (event.key === "ArrowRight" || event.key === "ArrowDown") nextIndex = index + 1;
        if (event.key === "ArrowLeft" || event.key === "ArrowUp") nextIndex = index - 1;
        if (event.key === "Home") nextIndex = 0;
        if (event.key === "End") nextIndex = tabButtons.length - 1;
        if (nextIndex === null) return;
        event.preventDefault();
        activate(nextIndex, true);
      });
    });

    activate(0);
  });

  /* ------------------------------------------------------------------------
     Filter groups (gallery / voices)
     ------------------------------------------------------------------------ */

  doc.querySelectorAll("[data-filter-group]").forEach((group) => {
    const targetSelector = group.dataset.filterTarget;
    const target = targetSelector ? doc.querySelector(targetSelector) : null;
    if (!target) return;
    const buttons = Array.from(group.querySelectorAll("[data-filter]"));
    const items = Array.from(target.querySelectorAll("[data-category]"));
    const count = group.querySelector("[data-filter-count]");
    const status = group.querySelector("[data-filter-status]");
    const empty = target.querySelector("[data-empty]");

    const applyFilter = (filter, announce = true) => {
      let visible = 0;
      items.forEach((item) => {
        const categories = (item.dataset.category || "").split(/\s+/);
        const match = filter === "all" || categories.includes(filter);
        item.hidden = !match;
        if (match) visible += 1;
      });
      buttons.forEach((button) => {
        button.setAttribute("aria-pressed", button.dataset.filter === filter ? "true" : "false");
      });
      if (count) count.textContent = String(visible).padStart(2, "0");
      if (empty) empty.hidden = visible !== 0;
      if (status && announce) {
        status.textContent = `已显示 ${visible} 项`;
      }
    };

    buttons.forEach((button) => {
      button.addEventListener("click", () => applyFilter(button.dataset.filter));
    });

    applyFilter("all", false);
  });

  /* ------------------------------------------------------------------------
     Lightbox
     ------------------------------------------------------------------------ */

  const lightbox = doc.querySelector("[data-lightbox]");
  if (lightbox && typeof lightbox.showModal === "function") {
    const lightboxImage = lightbox.querySelector("[data-lightbox-image]");
    const lightboxCaption = lightbox.querySelector("[data-lightbox-caption]");
    const lightboxMeta = lightbox.querySelector("[data-lightbox-meta]");
    const lightboxCount = lightbox.querySelector("[data-lightbox-count]");
    const closeButton = lightbox.querySelector("[data-lightbox-close]");
    const prevButton = lightbox.querySelector("[data-lightbox-prev]");
    const nextButton = lightbox.querySelector("[data-lightbox-next]");
    let activeItems = [];
    let activeIndex = 0;
    let lastTrigger = null;

    const visibleGalleryItems = () =>
      Array.from(doc.querySelectorAll(".gallery-card[data-category]")).filter((item) => !item.hidden);

    const render = (index) => {
      if (!activeItems.length) return;
      activeIndex = (index + activeItems.length) % activeItems.length;
      const item = activeItems[activeIndex];
      const button = item.querySelector(".gallery-btn");
      const image = item.querySelector("img");
      if (lightboxImage) {
        lightboxImage.src = button?.dataset.full || image?.src || "";
        lightboxImage.alt = image?.alt || "";
      }
      if (lightboxCaption) lightboxCaption.textContent = button?.dataset.caption || image?.alt || "";
      if (lightboxMeta) lightboxMeta.textContent = button?.dataset.meta || "";
      if (lightboxCount) {
        lightboxCount.textContent = `${String(activeIndex + 1).padStart(2, "0")} / ${String(activeItems.length).padStart(2, "0")}`;
      }
      lightbox.setAttribute("aria-label", `影像查看器：${button?.dataset.caption || ""}`);
    };

    const openLightbox = (item, trigger) => {
      activeItems = visibleGalleryItems();
      activeIndex = Math.max(0, activeItems.indexOf(item));
      lastTrigger = trigger || null;
      render(activeIndex);
      body.classList.add("modal-open");
      lightbox.showModal();
    };

    doc.querySelectorAll(".gallery-btn").forEach((button) => {
      button.addEventListener("click", () => {
        const item = button.closest(".gallery-card");
        if (item) openLightbox(item, button);
      });
    });

    closeButton?.addEventListener("click", () => lightbox.close());
    prevButton?.addEventListener("click", () => render(activeIndex - 1));
    nextButton?.addEventListener("click", () => render(activeIndex + 1));

    lightbox.addEventListener("click", (event) => {
      if (event.target === lightbox || event.target.classList.contains("lightbox-inner")) {
        lightbox.close();
      }
    });

    lightbox.addEventListener("close", () => {
      body.classList.remove("modal-open");
      if (lightboxImage) lightboxImage.src = "";
      lastTrigger?.focus();
    });

    lightbox.addEventListener("keydown", (event) => {
      if (event.key === "ArrowLeft") {
        event.preventDefault();
        render(activeIndex - 1);
      }
      if (event.key === "ArrowRight") {
        event.preventDefault();
        render(activeIndex + 1);
      }
    });
  }

  /* ------------------------------------------------------------------------
     Copy quote buttons and toast
     ------------------------------------------------------------------------ */

  let toastTimer = null;
  const toast = doc.createElement("div");
  toast.className = "toast";
  toast.setAttribute("role", "status");
  toast.setAttribute("aria-live", "polite");
  body.appendChild(toast);

  const showToast = (message) => {
    toast.textContent = message;
    toast.classList.add("is-visible");
    window.clearTimeout(toastTimer);
    toastTimer = window.setTimeout(() => toast.classList.remove("is-visible"), 2400);
  };

  const copyText = async (text) => {
    try {
      if (navigator.clipboard && window.isSecureContext) {
        await navigator.clipboard.writeText(text);
        return true;
      }
    } catch (error) {
      // Fall through to the textarea fallback.
    }
    try {
      const textarea = doc.createElement("textarea");
      textarea.value = text;
      textarea.setAttribute("readonly", "");
      textarea.style.position = "fixed";
      textarea.style.opacity = "0";
      body.appendChild(textarea);
      textarea.select();
      const ok = doc.execCommand("copy");
      textarea.remove();
      return ok;
    } catch (error) {
      return false;
    }
  };

  doc.querySelectorAll("[data-copy-target]").forEach((button) => {
    button.addEventListener("click", async () => {
      const target = doc.querySelector(button.dataset.copyTarget);
      const text = target?.textContent?.trim();
      if (!text) return;
      const copied = await copyText(text);
      showToast(copied ? "台词已复制到剪贴板" : "复制失败，请手动选择文本");
    });
  });

  /* ------------------------------------------------------------------------
     Current year
     ------------------------------------------------------------------------ */

  doc.querySelectorAll("[data-year]").forEach((el) => {
    el.textContent = String(new Date().getFullYear());
  });

  /* ------------------------------------------------------------------------
     Tiny page-load state for CSS transitions
     ------------------------------------------------------------------------ */

  window.requestAnimationFrame(() => root.classList.add("page-ready"));
})();
