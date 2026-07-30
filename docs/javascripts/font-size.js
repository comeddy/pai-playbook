/* 글자 크기 조절 버튼 — 저장값 조기 적용은 overrides/main.html extrahead 인라인 스크립트가 담당 */
(function () {
  var STEPS = [85, 90, 95, 100, 105, 110, 115, 120, 125, 130];
  var KEY = "pai-fs";
  var LABELS = {
    ko: ["글자 작게", "글자 크게"],
    en: ["Decrease font size", "Increase font size"],
    zh: ["缩小字号", "放大字号"],
    ja: ["文字を小さく", "文字を大きく"]
  };
  var labels = LABELS[(document.documentElement.lang || "ko").slice(0, 2)] || LABELS.ko;

  var minus = makeButton("A−", labels[0], -1);
  var plus = makeButton("A+", labels[1], +1);
  var box = document.createElement("div");
  box.className = "pai-fs-controls";
  box.appendChild(minus);
  box.appendChild(plus);
  document.body.appendChild(box);
  apply(current());

  function makeButton(text, label, delta) {
    var b = document.createElement("button");
    b.type = "button";
    b.textContent = text;
    b.setAttribute("aria-label", label);
    b.title = label;
    b.addEventListener("click", function () {
      var i = STEPS.indexOf(current()) + delta;
      if (i >= 0 && i < STEPS.length) apply(STEPS[i]);
    });
    return b;
  }
  function current() {
    var v;
    try { v = parseInt(localStorage.getItem(KEY), 10); } catch (e) { return 100; }
    return STEPS.indexOf(v) === -1 ? 100 : v;
  }
  function apply(v) {
    if (v === 100) {
      delete document.documentElement.dataset.fs;
      try { localStorage.removeItem(KEY); } catch (e) {}
    } else {
      document.documentElement.dataset.fs = v;
      try { localStorage.setItem(KEY, v); } catch (e) {}
    }
    minus.disabled = v === STEPS[0];
    plus.disabled = v === STEPS[STEPS.length - 1];
  }
})();
