/* zai theme behavior: theme toggle, language switch, active nav, search i18n.
   No dependencies. Loaded with defer. */
(function () {
  var root = document.documentElement;

  /* ---------- theme toggle ---------- */
  var toggle = document.getElementById("theme-toggle");
  function effectiveMode() {
    if (root.dataset.mode === "dark" || root.dataset.mode === "light") return root.dataset.mode;
    return (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches) ? "dark" : "light";
  }
  function syncToggle() {
    if (toggle) toggle.setAttribute("aria-pressed", effectiveMode() === "dark" ? "true" : "false");
  }
  if (toggle) {
    toggle.addEventListener("click", function () {
      var next = effectiveMode() === "dark" ? "light" : "dark";
      root.dataset.mode = next;
      try { localStorage.setItem("zai-theme", next); } catch (e) {}
      syncToggle();
    });
    syncToggle();
    if (window.matchMedia) {
      var mq = window.matchMedia("(prefers-color-scheme: dark)");
      var onChange = function () { syncToggle(); };
      if (mq.addEventListener) { mq.addEventListener("change", onChange); }
      else if (mq.addListener) { mq.addListener(onChange); }
    }
  }

  /* ---------- language switch: map mirrored paths only ---------- */
  var lang = document.getElementById("lang-switch");
  if (lang) {
    var mirrored = ["/", "/chat/", "/code/", "/api/", "/models/", "/history/",
                    "/company/", "/ecosystem/", "/la-famille/", "/meta/"];
    var p = location.pathname;
    var isMirrored = mirrored.some(function (pre) { return p === pre || p.indexOf(pre) === 0; });
    if (p === "/zh" || p === "/zh/") { lang.href = "/"; }
    else if (p.indexOf("/zh/") === 0) {
      var en = p.slice(3);
      var enMirrored = mirrored.some(function (pre) { return en === pre || en.indexOf(pre) === 0; });
      lang.href = (enMirrored ? en : "/") + location.hash;
    } else {
      lang.href = (isMirrored ? "/zh" + p : "/zh/") + location.hash;
    }
  }

  /* ---------- active nav ---------- */
  var path = location.pathname;
  Array.prototype.forEach.call(document.querySelectorAll(".z-nav a"), function (a) {
    var href = a.getAttribute("href");
    if (href && href !== "/" && href !== "/zh/" && path.indexOf(href) === 0) {
      a.setAttribute("aria-current", "page");
    }
  });

  /* ---------- search i18n patch (search.js ships fixed English strings) ---------- */
  if ((root.lang || "").toLowerCase().indexOf("zh") === 0) {
    var list = document.getElementById("search-results-list");
    if (list) {
      new MutationObserver(function () {
        Array.prototype.forEach.call(list.querySelectorAll(".search-no-results"), function (n) {
          if (n.textContent === "No results found") n.textContent = "未找到结果";
        });
        Array.prototype.forEach.call(list.querySelectorAll(".search-result-section"), function (n) {
          var t = n.textContent || "";
          if (t.indexOf("Section: ") === 0) n.textContent = "小节: " + t.slice(9);
        });
        Array.prototype.forEach.call(list.querySelectorAll(".search-result-title"), function (n) {
          if (n.textContent === "Untitled") n.textContent = "未命名";
        });
      }).observe(list, { childList: true, subtree: true, characterData: true });
    }
  }
})();
