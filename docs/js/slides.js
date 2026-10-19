(function () {
  const slides = Array.from(document.querySelectorAll(".slide"));
  const total = slides.length;
  const counter = document.getElementById("counter");
  const sectionName = document.getElementById("section-name");
  const progress = document.getElementById("progress");
  const clock = document.getElementById("clock");
  const config = window.WORKSHOP_CONFIG || {};
  let current = 0;
  let startTime = Date.now();

  // Each divider names a section; later slides inherit it for the HUD.
  let section = "";
  slides.forEach(function (slide) {
    if (slide.dataset.section) {
      section = slide.dataset.section;
    }
    slide.dataset.sectionName = section;
  });

  function indexFromHash() {
    const n = parseInt(window.location.hash.replace("#", ""), 10);
    if (isNaN(n) || n < 1) {
      return 0;
    }
    if (n > total) {
      return total - 1;
    }
    return n - 1;
  }

  function show(i) {
    if (i < 0) {
      i = 0;
    }
    if (i > total - 1) {
      i = total - 1;
    }
    slides[current].classList.remove("active");
    current = i;
    slides[current].classList.add("active");
    if (counter) {
      counter.textContent = (current + 1) + " / " + total;
    }
    if (sectionName) {
      sectionName.textContent = slides[current].dataset.sectionName;
    }
    if (progress) {
      progress.style.width = (((current + 1) / total) * 100) + "%";
    }
    const wanted = "#" + (current + 1);
    if (window.location.hash !== wanted) {
      history.replaceState(null, "", wanted);
    }
    if (!document.body.classList.contains("overview")) {
      window.scrollTo(0, 0);
    }
    tick();
  }

  function next() {
    show(current + 1);
  }

  function prev() {
    show(current - 1);
  }

  function toggleFullscreen() {
    if (document.fullscreenElement) {
      if (document.exitFullscreen) {
        document.exitFullscreen();
      }
      return;
    }
    if (document.documentElement.requestFullscreen) {
      document.documentElement.requestFullscreen();
    }
  }

  function toggleOverview() {
    document.body.classList.toggle("overview");
    if (document.body.classList.contains("overview")) {
      slides[current].scrollIntoView({ block: "center" });
    } else {
      window.scrollTo(0, 0);
    }
  }

  function toggleNotes() {
    document.body.classList.toggle("show-notes");
  }

  function isInteractive(target) {
    return Boolean(target.closest("a, button, input, select, textarea, summary, pre, aside.notes, .hud, .qr"));
  }

  function pad(n) {
    if (n < 10) {
      return "0" + n;
    }
    return String(n);
  }

  function tick() {
    if (!clock) {
      return;
    }
    const secs = Math.floor((Date.now() - startTime) / 1000);
    let text = pad(Math.floor(secs / 60)) + ":" + pad(secs % 60);
    const planned = slides[current].dataset.at;
    if (planned) {
      text = text + " (plan " + planned + ")";
    }
    clock.textContent = text;
  }

  document.addEventListener("keydown", function (e) {
    if (e.ctrlKey || e.metaKey || e.altKey) {
      return;
    }
    const key = e.key;
    const inOverview = document.body.classList.contains("overview");
    if (key === "ArrowRight" || key === "PageDown" || key === " ") {
      e.preventDefault();
      next();
    } else if (key === "ArrowLeft" || key === "PageUp") {
      e.preventDefault();
      prev();
    } else if (key === "Home") {
      e.preventDefault();
      show(0);
    } else if (key === "End") {
      e.preventDefault();
      show(total - 1);
    } else if (key === "n" || key === "N") {
      toggleNotes();
    } else if (key === "f" || key === "F") {
      toggleFullscreen();
    } else if (key === "o" || key === "O") {
      toggleOverview();
    } else if (key === "Escape" && inOverview) {
      toggleOverview();
    } else if (key === "t" || key === "T") {
      startTime = Date.now();
      tick();
    }
  });

  document.addEventListener("click", function (e) {
    if (document.body.classList.contains("overview")) {
      const picked = e.target.closest(".slide");
      if (picked) {
        document.body.classList.remove("overview");
        show(slides.indexOf(picked));
      }
      return;
    }
    if (isInteractive(e.target)) {
      return;
    }
    const sel = window.getSelection();
    if (sel && sel.toString().length > 0) {
      return;
    }
    if (e.clientX < window.innerWidth / 2) {
      prev();
    } else {
      next();
    }
  });

  let touchX = null;
  let touchY = null;
  document.addEventListener("touchstart", function (e) {
    if (e.touches.length !== 1) {
      touchX = null;
      return;
    }
    touchX = e.touches[0].clientX;
    touchY = e.touches[0].clientY;
  }, { passive: true });

  document.addEventListener("touchend", function (e) {
    if (touchX === null || document.body.classList.contains("overview")) {
      return;
    }
    const dx = e.changedTouches[0].clientX - touchX;
    const dy = e.changedTouches[0].clientY - touchY;
    touchX = null;
    if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy) * 1.5) {
      if (dx < 0) {
        next();
      } else {
        prev();
      }
    }
  }, { passive: true });

  window.addEventListener("hashchange", function () {
    show(indexFromHash());
  });

  const buttons = {
    "btn-prev": prev,
    "btn-next": next,
    "btn-notes": toggleNotes,
    "btn-overview": toggleOverview
  };
  Object.keys(buttons).forEach(function (id) {
    const el = document.getElementById(id);
    if (el) {
      el.addEventListener("click", buttons[id]);
    }
  });

  if (config.REPO_URL) {
    document.querySelectorAll("[data-repo-link]").forEach(function (a) {
      a.href = config.REPO_URL;
      if (a.dataset.repoLink === "text") {
        a.textContent = config.REPO_URL.replace("https://", "");
      }
    });
  }

  const pollLink = document.getElementById("poll-link");
  const qrBox = document.getElementById("poll-qr");
  let pollUrl = "https://github.com/TexBonham/GithubWorkshop/discussions";
  if (config.POLL_URL) {
    pollUrl = config.POLL_URL;
  }
  if (pollLink) {
    pollLink.href = pollUrl;
    pollLink.textContent = pollUrl.replace("https://", "");
  }

  function drawQr() {
    if (!qrBox || typeof window.QRCode !== "function") {
      return;
    }
    try {
      new window.QRCode(qrBox, {
        text: pollUrl,
        width: 320,
        height: 320,
        colorDark: "#000000",
        colorLight: "#ffffff",
        correctLevel: window.QRCode.CorrectLevel.M
      });
    } catch (err) {
      qrBox.textContent = "";
    }
  }

  // Loaded from here rather than a <script> tag so a slow or blocked CDN never delays the deck.
  if (qrBox) {
    const qrScript = document.createElement("script");
    qrScript.src = "https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js";
    qrScript.async = true;
    qrScript.onload = drawQr;
    document.head.appendChild(qrScript);
  }

  setInterval(tick, 1000);
  show(indexFromHash());
})();
