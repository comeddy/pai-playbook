/* 총비용·ROI 계산기 — start*.md 의 <div class="pai-roi-calc"> 에만 렌더링.
 * 규칙: 빈칸 = 견적 대기(계산에서 0으로 취급하지 않음), 0 = 해당 없음.
 * 수식은 start.md #roi 본문과 계약 — 바꾸면 4개 언어 본문 수식도 같이 고친다. */
(function () {
  var root = document.querySelector(".pai-roi-calc");
  if (!root) return;

  var KEY = "pai-roi-v1";
  var SC = ["low", "base", "high"];
  var CATS = ["initial", "experiment", "monthly"];

  var T = {
    ko: {
      period: "분석 기간(개월)", cat: "구분", item: "항목", unit: "단위", qty: "수량",
      unitCost: "단가 (USD)", low: "낮음", base: "기준", high: "높음", checked: "확인일·출처",
      sub: "소계 (기준)", initial: "초기 고정비", experiment: "실험 변동비", monthly: "운영 반복비 (월)",
      effect: "월 기대 효과 (USD)", effectNote: "실제 감소한 재작업·정지 시간, 실현 가능한 처리량 가치 — 생산성과 인건비를 이중 계산하지 않는다",
      addRow: "+ 항목 추가", del: "삭제", reset: "초기화", dl: "결과 CSV 다운로드", newItem: "새 항목",
      hint: "빈칸 = 견적 대기(0으로 계산하지 않음), 0 = 해당 없음. 낮음·높음 단가를 비우면 기준 단가를 쓴다. 운영 반복비 수량은 월 기준. 입력값은 이 브라우저에만 저장된다.",
      metric: "지표", invest: "초기 투자 (초기 고정비 + 실험 변동비)", opsP: "기간 운영비", effP: "기간 효과",
      netP: "기간 순편익", netM: "월 순편익", payback: "회수 기간", roi: "기간 ROI",
      worst: "보수적 조합 (높은 비용 × 낮은 효과)", pending: "견적 대기", noPayback: "회수 불가",
      months: "개월", pendingList: "견적 대기 항목", scen: "시나리오",
      items: {
        robot_and_sensors: ["로봇·그리퍼·센서", "세트"], integration_and_safety: ["설치·SI·안전 검토", "시간"],
        data_and_environment: ["데이터 수집·환경 제작", "시간"], gpu_instances: ["GPU 인스턴스", "인스턴스·시간"],
        storage_network_logs: ["스토리지·전송·로그", "월"], engineering_and_retries: ["실험 인력·재시도", "시간"],
        maintenance_and_interventions: ["유지보수·사람 개입", "시간/월"], cloud_inference_and_revalidation: ["추론·연결·재검증", "월"]
      }
    },
    en: {
      period: "Analysis period (months)", cat: "Group", item: "Item", unit: "Unit", qty: "Qty",
      unitCost: "Unit cost (USD)", low: "Low", base: "Base", high: "High", checked: "Checked · source",
      sub: "Subtotal (base)", initial: "Initial fixed", experiment: "Experiment variable", monthly: "Recurring ops (monthly)",
      effect: "Monthly expected benefit (USD)", effectNote: "Actual reductions in rework/downtime, realizable throughput value — do not double-count productivity and labor savings",
      addRow: "+ Add item", del: "Delete", reset: "Reset", dl: "Download results CSV", newItem: "New item",
      hint: "Blank = quote pending (never counted as 0), 0 = not applicable. Blank low/high rates fall back to the base rate. Recurring-ops quantities are per month. Inputs are saved only in this browser.",
      metric: "Metric", invest: "Initial investment (initial fixed + experiment)", opsP: "Period operating cost", effP: "Period benefit",
      netP: "Period net benefit", netM: "Monthly net benefit", payback: "Payback period", roi: "Period ROI",
      worst: "Conservative mix (high cost × low benefit)", pending: "Quote pending", noPayback: "No payback",
      months: "months", pendingList: "Quote-pending items", scen: "Scenario",
      items: {
        robot_and_sensors: ["Robot, gripper, sensors", "set"], integration_and_safety: ["Installation, SI, safety review", "hour"],
        data_and_environment: ["Data collection, environment build", "hour"], gpu_instances: ["GPU instances", "instance-hour"],
        storage_network_logs: ["Storage, transfer, logs", "month"], engineering_and_retries: ["Engineering time, retries", "hour"],
        maintenance_and_interventions: ["Maintenance, human interventions", "hour/month"], cloud_inference_and_revalidation: ["Inference, connectivity, revalidation", "month"]
      }
    },
    zh: {
      period: "分析期间（月）", cat: "类别", item: "项目", unit: "单位", qty: "数量",
      unitCost: "单价 (USD)", low: "低", base: "基准", high: "高", checked: "确认日期·来源",
      sub: "小计（基准）", initial: "初始固定费用", experiment: "实验变动费用", monthly: "运营经常费用（月）",
      effect: "月预期收益 (USD)", effectNote: "实际减少的返工及停机、可兑现的吞吐量价值 — 不要重复计算生产率提升与人工节省",
      addRow: "+ 添加项目", del: "删除", reset: "重置", dl: "下载结果 CSV", newItem: "新项目",
      hint: "空白 = 待报价（不按 0 计算），0 = 不适用。低/高单价留空时使用基准单价。运营经常费用的数量按月计。输入值仅保存在本浏览器中。",
      metric: "指标", invest: "初始投资（初始固定 + 实验变动）", opsP: "期间运营费用", effP: "期间收益",
      netP: "期间净收益", netM: "月净收益", payback: "回收期", roi: "期间 ROI",
      worst: "保守组合（高费用 × 低收益）", pending: "待报价", noPayback: "无法回收",
      months: "个月", pendingList: "待报价项目", scen: "情景",
      items: {
        robot_and_sensors: ["机器人、夹爪、传感器", "套"], integration_and_safety: ["安装、SI、安全审查", "小时"],
        data_and_environment: ["数据采集、环境制作", "小时"], gpu_instances: ["GPU 实例", "实例·小时"],
        storage_network_logs: ["存储、传输、日志", "月"], engineering_and_retries: ["实验人员、重试", "小时"],
        maintenance_and_interventions: ["维护、人工介入", "小时/月"], cloud_inference_and_revalidation: ["推理、连接、复核", "月"]
      }
    },
    ja: {
      period: "分析期間（か月）", cat: "区分", item: "項目", unit: "単位", qty: "数量",
      unitCost: "単価 (USD)", low: "低", base: "基準", high: "高", checked: "確認日・出典",
      sub: "小計（基準）", initial: "初期固定費", experiment: "実験変動費", monthly: "継続運用費（月）",
      effect: "月間期待効果 (USD)", effectNote: "実際に減少する手戻り・停止、実現可能な処理量の価値 — 生産性向上と人件費削減を二重計上しない",
      addRow: "+ 項目を追加", del: "削除", reset: "リセット", dl: "結果CSVをダウンロード", newItem: "新しい項目",
      hint: "空欄 = 見積待ち（0として計算しない）、0 = 該当なし。低・高の単価が空欄なら基準単価を使います。継続運用費の数量は月単位。入力値はこのブラウザにのみ保存されます。",
      metric: "指標", invest: "初期投資（初期固定費 + 実験変動費）", opsP: "期間運用費", effP: "期間効果",
      netP: "期間純便益", netM: "月間純便益", payback: "回収期間", roi: "期間ROI",
      worst: "保守的な組合せ（高費用 × 低効果）", pending: "見積待ち", noPayback: "回収不可",
      months: "か月", pendingList: "見積待ちの項目", scen: "シナリオ",
      items: {
        robot_and_sensors: ["ロボット・グリッパー・センサー", "セット"], integration_and_safety: ["設置・SI・安全審査", "時間"],
        data_and_environment: ["データ収集・環境制作", "時間"], gpu_instances: ["GPUインスタンス", "インスタンス時間"],
        storage_network_logs: ["保存・転送・ログ", "月"], engineering_and_retries: ["実験人員・再実行", "時間"],
        maintenance_and_interventions: ["保守・人の介入", "時間/月"], cloud_inference_and_revalidation: ["推論・接続・再検証", "月"]
      }
    }
  };
  var lang = (document.documentElement.lang || "ko").slice(0, 2);
  var L = T[lang] || T.ko;

  var DEFAULT_ROWS = [
    ["initial", "robot_and_sensors"], ["initial", "integration_and_safety"], ["initial", "data_and_environment"],
    ["experiment", "gpu_instances"], ["experiment", "storage_network_logs"], ["experiment", "engineering_and_retries"],
    ["monthly", "maintenance_and_interventions"], ["monthly", "cloud_inference_and_revalidation"]
  ];

  function freshState() {
    return {
      months: "12",
      effect: { low: "", base: "", high: "" },
      rows: DEFAULT_ROWS.map(function (r) {
        return { cat: r[0], id: r[1], name: L.items[r[1]][0], unit: L.items[r[1]][1], qty: "", low: "", base: "", high: "", checked: "" };
      })
    };
  }

  var state = load() || freshState();

  function load() {
    try {
      var s = JSON.parse(localStorage.getItem(KEY + "-" + lang));
      return s && Array.isArray(s.rows) ? s : null;
    } catch (e) { return null; }
  }
  function save() {
    try { localStorage.setItem(KEY + "-" + lang, JSON.stringify(state)); } catch (e) { /* 저장 불가 환경: 무시 */ }
  }

  /* 빈칸 → null(견적 대기). 숫자가 아니면 null. */
  function num(v) {
    if (v === null || v === undefined || String(v).trim() === "") return null;
    var n = Number(String(v).replace(/,/g, ""));
    return isFinite(n) ? n : null;
  }

  /* 행 소계: 수량·기준 단가 중 하나라도 비면 null(견적 대기). 낮음·높음 단가는 비면 기준 단가. */
  function rowCost(r, sc) {
    var q = num(r.qty), b = num(r.base);
    if (q === null || b === null) return null;
    var u = sc === "base" ? b : (num(r[sc]) === null ? b : num(r[sc]));
    return q * u;
  }

  /* 구분별 합계. pending 행이 하나라도 있으면 null. */
  function catSum(cat, sc) {
    var total = 0, pend = false;
    state.rows.forEach(function (r) {
      if (r.cat !== cat) return;
      var c = rowCost(r, sc);
      if (c === null) pend = true; else total += c;
    });
    return pend ? null : total;
  }

  function effectOf(sc) {
    var e = num(state.effect[sc]);
    return e === null && sc !== "base" ? num(state.effect.base) : e;
  }

  /* 한 시나리오의 결과. costSc = 비용 시나리오, effSc = 효과 시나리오. 값이 null이면 견적 대기. */
  function scenario(costSc, effSc) {
    var m = num(state.months);
    var ini = catSum("initial", costSc), exp = catSum("experiment", costSc), mon = catSum("monthly", costSc);
    var eff = effectOf(effSc);
    var invest = ini === null || exp === null ? null : ini + exp;
    var opsP = mon === null || m === null ? null : mon * m;
    var effP = eff === null || m === null ? null : eff * m;
    var netP = effP === null || opsP === null ? null : effP - opsP;
    var netM = eff === null || mon === null ? null : eff - mon;
    var payback = invest === null || netM === null ? null : (netM > 0 ? invest / netM : "none");
    var denom = invest === null || opsP === null ? null : invest + opsP;
    var roi = denom === null || effP === null ? null : (denom === 0 ? "none" : (effP - invest - opsP) / denom);
    return { invest: invest, opsP: opsP, effP: effP, netP: netP, netM: netM, payback: payback, roi: roi };
  }

  function results() {
    return [
      { label: L.low, r: scenario("low", "low") },
      { label: L.base, r: scenario("base", "base") },
      { label: L.high, r: scenario("high", "high") },
      { label: L.worst, r: scenario("high", "low") }
    ];
  }

  var usd = new Intl.NumberFormat("en-US", { style: "currency", currency: "USD", maximumFractionDigits: 0 });
  function fmtMoney(v) { return v === null ? L.pending : usd.format(v); }
  function fmtPayback(v) { return v === null ? L.pending : v === "none" ? L.noPayback : v.toFixed(1) + " " + L.months; }
  function fmtRoi(v) { return v === null ? L.pending : v === "none" ? "—" : (v * 100).toFixed(1) + "%"; }

  function pendingRows() {
    return state.rows.filter(function (r) { return rowCost(r, "base") === null; }).map(function (r) { return r.name; });
  }

  /* ---------- 렌더링 ---------- */
  function el(tag, attrs, children) {
    var e = document.createElement(tag);
    if (attrs) Object.keys(attrs).forEach(function (k) {
      if (k === "text") e.textContent = attrs[k];
      else if (k === "on") Object.keys(attrs.on).forEach(function (ev) { e.addEventListener(ev, attrs.on[ev]); });
      else e.setAttribute(k, attrs[k]);
    });
    (children || []).forEach(function (c) { if (c) e.appendChild(c); });
    return e;
  }
  function input(value, onInput, opts) {
    opts = opts || {};
    return el("input", {
      type: "text", inputmode: opts.text ? "text" : "decimal", value: value || "",
      "aria-label": opts.label || "", placeholder: opts.ph || "", class: opts.text ? "pai-roi-txt" : "pai-roi-num",
      on: { input: function (e) { onInput(e.target.value); save(); refresh(); } }
    });
  }
  function wrap(table) { return el("div", { class: "pai-roi-scroll" }, [table]); }

  var resultBox, subCells = [];

  function render() {
    root.innerHTML = "";
    subCells = [];

    var top = el("div", { class: "pai-roi-top" }, [
      el("label", null, [
        el("span", { text: L.period + " " }),
        input(state.months, function (v) { state.months = v; }, { label: L.period })
      ])
    ]);

    var head = el("tr", null, [L.cat, L.item, L.unit, L.qty, L.unitCost + " · " + L.low, L.unitCost + " · " + L.base, L.unitCost + " · " + L.high, L.checked, L.sub, ""]
      .map(function (h) { return el("th", { text: h, scope: "col" }); }));
    var body = el("tbody");
    state.rows.forEach(function (r, i) {
      var catSel = el("select", { "aria-label": L.cat, on: { change: function (e) { r.cat = e.target.value; save(); refresh(); } } },
        CATS.map(function (c) { var o = el("option", { value: c, text: L[c] }); if (c === r.cat) o.selected = true; return o; }));
      var sub = el("td", { class: "pai-roi-sub" });
      subCells.push([sub, r]);
      body.appendChild(el("tr", null, [
        el("td", null, [catSel]),
        el("td", null, [input(r.name, function (v) { r.name = v; }, { text: true, label: L.item })]),
        el("td", null, [input(r.unit, function (v) { r.unit = v; }, { text: true, label: L.unit })]),
        el("td", null, [input(r.qty, function (v) { r.qty = v; }, { label: L.qty })]),
        el("td", null, [input(r.low, function (v) { r.low = v; }, { label: L.low, ph: L.base })]),
        el("td", null, [input(r.base, function (v) { r.base = v; }, { label: L.base })]),
        el("td", null, [input(r.high, function (v) { r.high = v; }, { label: L.high, ph: L.base })]),
        el("td", null, [input(r.checked, function (v) { r.checked = v; }, { text: true, label: L.checked, ph: "YYYY-MM-DD" })]),
        sub,
        el("td", null, [el("button", { type: "button", class: "pai-roi-del", "aria-label": L.del, title: L.del, text: "×",
          on: { click: function () { state.rows.splice(i, 1); save(); render(); } } })])
      ]));
    });
    var costTable = el("table", { class: "pai-roi-table" }, [el("thead", null, [head]), body]);

    var effTable = el("table", { class: "pai-roi-table" }, [
      el("thead", null, [el("tr", null, ["", L.low, L.base, L.high].map(function (h) { return el("th", { text: h, scope: "col" }); }))]),
      el("tbody", null, [el("tr", null, [el("th", { scope: "row", text: L.effect })].concat(SC.map(function (sc) {
        return el("td", null, [input(state.effect[sc], function (v) { state.effect[sc] = v; }, { label: L.effect + " " + L[sc], ph: sc === "base" ? "" : L.base })]);
      })))])
    ]);

    var actions = el("div", { class: "pai-roi-actions" }, [
      el("button", { type: "button", class: "md-button", text: L.addRow, on: { click: function () {
        state.rows.push({ cat: "initial", id: "custom", name: L.newItem, unit: "", qty: "", low: "", base: "", high: "", checked: "" });
        save(); render();
      } } }),
      el("button", { type: "button", class: "md-button", text: L.reset, on: { click: function () {
        state = freshState(); save(); render();
      } } }),
      el("button", { type: "button", class: "md-button md-button--primary", text: L.dl, on: { click: download } })
    ]);

    resultBox = el("div", { class: "pai-roi-results", "aria-live": "polite" });

    root.appendChild(top);
    root.appendChild(el("p", { class: "pai-roi-hint", text: L.hint }));
    root.appendChild(wrap(costTable));
    root.appendChild(wrap(effTable));
    root.appendChild(el("p", { class: "pai-roi-hint", text: L.effectNote }));
    root.appendChild(actions);
    root.appendChild(resultBox);
    refresh();
  }

  function refresh() {
    subCells.forEach(function (p) {
      var c = rowCost(p[1], "base");
      p[0].textContent = c === null ? L.pending : usd.format(c);
      p[0].classList.toggle("pai-roi-pending", c === null);
    });
    var res = results();
    var rows = [
      ["invest", fmtMoney], ["opsP", fmtMoney], ["effP", fmtMoney], ["netP", fmtMoney],
      ["netM", fmtMoney], ["payback", fmtPayback], ["roi", fmtRoi]
    ];
    var t = el("table", { class: "pai-roi-table pai-roi-out" }, [
      el("thead", null, [el("tr", null, [el("th", { text: L.metric, scope: "col" })].concat(res.map(function (x) { return el("th", { text: x.label, scope: "col" }); })))]),
      el("tbody", null, rows.map(function (row) {
        return el("tr", null, [el("th", { scope: "row", text: L[row[0]] })].concat(res.map(function (x) {
          var v = x.r[row[0]];
          return el("td", { text: row[1](v), class: v === null ? "pai-roi-pending" : (typeof v === "number" && v < 0 ? "pai-roi-neg" : "") });
        })));
      }))
    ]);
    resultBox.innerHTML = "";
    resultBox.appendChild(wrap(t));
    var pend = pendingRows();
    if (num(state.effect.base) === null) pend.push(L.effect);
    if (pend.length) resultBox.appendChild(el("p", { class: "pai-roi-hint pai-roi-pending", text: L.pendingList + ": " + pend.join(", ") }));
  }

  /* ---------- CSV 다운로드 (입력 + 소계 + 결과) ---------- */
  function csvCell(v) {
    var s = v === null || v === undefined ? "" : String(v);
    // 스프레드시트 수식 주입 방지 — 숫자(음수 포함)는 그대로 둔다
    if (typeof v !== "number" && /^[=+\-@]/.test(s) && !isFinite(Number(s))) s = "'" + s;
    return /[",\n]/.test(s) ? '"' + s.replace(/"/g, '""') + '"' : s;
  }
  function raw(v) { return v === null ? L.pending : v === "none" ? "" : Math.round(v * 100) / 100; }

  function download() {
    var lines = [];
    var push = function (arr) { lines.push(arr.map(csvCell).join(",")); };
    var subLabel = L.sub.replace(/\s*\(.*\)|（.*）/, ""); // "소계 (기준)" → "소계"
    var today = new Date().toISOString().slice(0, 10);
    push(["PAI Playbook — " + L.roi, today, "USD"]);
    push([L.period, state.months]);
    push([]);
    push([L.cat, L.item, L.unit, L.qty, L.unitCost + " " + L.low, L.unitCost + " " + L.base, L.unitCost + " " + L.high,
      subLabel + " " + L.low, subLabel + " " + L.base, subLabel + " " + L.high, L.checked]);
    state.rows.forEach(function (r) {
      push([L[r.cat], r.name, r.unit, r.qty, r.low, r.base, r.high].concat(SC.map(function (sc) {
        var c = rowCost(r, sc); return c === null ? L.pending : c;
      })).concat([r.checked]));
    });
    push([]);
    push([L.effect, L.low, state.effect.low, L.base, state.effect.base, L.high, state.effect.high]);
    push([]);
    var res = results();
    push([L.metric].concat(res.map(function (x) { return x.label; })));
    ["invest", "opsP", "effP", "netP", "netM"].forEach(function (k) {
      push([L[k]].concat(res.map(function (x) { return raw(x.r[k]); })));
    });
    push([L.payback + " (" + L.months + ")"].concat(res.map(function (x) {
      return x.r.payback === "none" ? L.noPayback : raw(x.r.payback);
    })));
    push([L.roi + " (%)"].concat(res.map(function (x) {
      return x.r.roi === null ? L.pending : x.r.roi === "none" ? "" : Math.round(x.r.roi * 1000) / 10;
    })));
    var pend = pendingRows();
    if (pend.length) { push([]); push([L.pendingList].concat(pend)); }

    // BOM: 엑셀이 UTF-8 한·중·일 문자를 깨뜨리지 않도록
    var blob = new Blob(["﻿" + lines.join("\r\n")], { type: "text/csv;charset=utf-8" });
    var a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "pilot-roi-" + today + ".csv";
    document.body.appendChild(a);
    a.click();
    setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 0);
  }

  render();
})();
