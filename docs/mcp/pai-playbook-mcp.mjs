#!/usr/bin/env node
// docs/mcp/pai-playbook-mcp.mjs — Physical AI Playbook MCP 서버 (stdio, 단일 파일, 의존성 없음)
// 실행: node "$HOME/.pai-playbook/server.mjs"   (Node 18+)
// 콘텐츠: PAI_PLAYBOOK_DOCS_DIR(로컬 docs/)가 있으면 파일, 없으면 GitHub raw(main).
// 설정 절차: https://comeddy.github.io/pai-playbook/mcp/
import { readFile } from "node:fs/promises";
import path from "node:path";
import readline from "node:readline";

const NAME = "pai-playbook";
const VERSION = "1.0.0";
const RAW = "https://raw.githubusercontent.com/comeddy/pai-playbook/main/";
const SITE = "https://comeddy.github.io/pai-playbook/";
const LANGS = ["ko", "en", "zh", "ja"];
const SUPPORTED = ["2025-06-18", "2025-03-26", "2024-11-05"];
const DOCS_DIR = process.env.PAI_PLAYBOOK_DOCS_DIR || null;
const TTL_MS = 10 * 60 * 1000;
const cache = new Map();

const log = (...a) => process.stderr.write(a.join(" ") + "\n");

// rel: "mkdocs.yml" | "docs/<file>"
async function source(rel) {
  const hit = cache.get(rel);
  if (hit && hit.until > Date.now()) return hit.text;
  let text;
  if (DOCS_DIR) {
    const p = rel === "mkdocs.yml"
      ? path.join(DOCS_DIR, "..", "mkdocs.yml")
      : path.join(DOCS_DIR, rel.replace(/^docs\//, ""));
    text = await readFile(p, "utf8");
  } else {
    const res = await fetch(RAW + rel);
    if (!res.ok) throw new Error(`${rel}: HTTP ${res.status}`);
    text = await res.text();
  }
  cache.set(rel, { text, until: Date.now() + TTL_MS });
  return text;
}

const isMissing = (e) => /ENOENT|HTTP 404/.test(e?.message || "");

async function pages() {
  const lines = (await source("mkdocs.yml")).split("\n");
  const start = lines.findIndex((l) => l.trimEnd() === "nav:");
  if (start < 0) throw new Error("mkdocs.yml: nav 블록 없음");
  const out = [];
  for (const line of lines.slice(start + 1)) {
    if (line.trim() && !line.startsWith(" ")) break;
    const m = line.match(/^\s+-\s+"?(.*?)"?:\s*(\S+)\.md\s*$/);
    if (m) out.push({ id: m[2], title: m[1] });
  }
  return out;
}

function checkLang(lang) {
  if (!LANGS.includes(lang)) throw new Error(`lang은 ${LANGS.join("/")} 중 하나여야 합니다 (받은 값: ${lang})`);
}

async function pageText(id, lang) {
  checkLang(lang);
  const list = await pages();
  if (!list.some((p) => p.id === id)) {
    throw new Error(`알 수 없는 페이지: ${id}. 사용 가능: ${list.map((p) => p.id).join(", ")}`);
  }
  const file = lang === "ko" ? `${id}.md` : `${id}.${lang}.md`;
  const raw = await source(`docs/${file}`);
  return raw.replace(/^---\n[\s\S]*?\n---\n/, "");
}

const pageUrl = (id, lang) => `${SITE}${lang === "ko" ? "" : lang + "/"}${id === "index" ? "" : id + "/"}`;

const TOOLS = [
  {
    name: "playbook_list_pages",
    description: "Physical AI Playbook의 페이지 목록(id·제목·URL). 다른 도구의 page 인자에 id를 사용한다.",
    inputSchema: { type: "object", properties: { lang: { type: "string", enum: LANGS, description: "기본 ko" } } },
  },
  {
    name: "playbook_read_page",
    description: "Playbook 페이지 1개의 마크다운 원문을 읽는다 (예: index, guide, pillar-2, radar, decisions).",
    inputSchema: {
      type: "object", required: ["page"],
      properties: { page: { type: "string", description: "페이지 id (playbook_list_pages 참고)" },
                    lang: { type: "string", enum: LANGS, description: "기본 ko" } },
    },
  },
  {
    name: "playbook_search",
    description: "모든 Playbook 페이지에서 문자열을 검색해 'page:줄번호: 텍스트' 스니펫을 돌려준다 (대소문자 무시, 랭킹 없음).",
    inputSchema: {
      type: "object", required: ["query"],
      properties: { query: { type: "string" }, lang: { type: "string", enum: LANGS, description: "기본 ko" },
                    limit: { type: "integer", minimum: 1, maximum: 100, description: "기본 20" } },
    },
  },
  {
    name: "playbook_evidence",
    description: "근거 기록(claims.json): claim_id를 주면 해당 주장 전체, 없으면 전체 요약(id·상태·확인일·영향 페이지).",
    inputSchema: { type: "object", properties: { claim_id: { type: "string" } } },
  },
];

const handlers = {
  async playbook_list_pages({ lang = "ko" }) {
    checkLang(lang);
    const list = await pages();
    return list.map((p) => `${p.id} — ${p.title} — ${pageUrl(p.id, lang)}`).join("\n");
  },
  async playbook_read_page({ page, lang = "ko" }) {
    if (!page) throw new Error("page 인자가 필요합니다");
    return pageText(page, lang);
  },
  async playbook_search({ query, lang = "ko", limit = 20 }) {
    if (!query || !String(query).trim()) throw new Error("query가 비어 있습니다");
    checkLang(lang);
    const q = String(query).toLowerCase();
    const max = Math.min(Math.max(Number(limit) || 20, 1), 100);
    const hits = [];
    for (const p of await pages()) {
      let text;
      try { text = await pageText(p.id, lang); } catch (e) { log(`search skip ${p.id}: ${e.message}`); continue; }
      const lines = text.split("\n");
      for (let i = 0; i < lines.length && hits.length < max; i++) {
        if (lines[i].toLowerCase().includes(q)) hits.push(`${p.id}:${i + 1}: ${lines[i].trim().slice(0, 200)}`);
      }
      if (hits.length >= max) break;
    }
    return hits.length ? hits.join("\n") : `검색 결과 없음: ${query}`;
  },
  async playbook_evidence({ claim_id }) {
    let raw;
    try {
      raw = await source("docs/assets/claims.json");
    } catch (e) {
      if (isMissing(e)) throw new Error("근거 기록(assets/claims.json)이 아직 게시되지 않았습니다 — 근거 기록 페이지가 배포되면 사용할 수 있습니다");
      throw e;
    }
    const claims = JSON.parse(raw).claims || [];
    if (claim_id) {
      const c = claims.find((x) => x.id === claim_id);
      if (!c) throw new Error(`알 수 없는 claim_id: ${claim_id}. 사용 가능: ${claims.map((x) => x.id).join(", ")}`);
      return JSON.stringify(c, null, 2);
    }
    return claims.map((c) => `${c.id} · ${c.status} · checked_on ${c.checked_on} · pages ${(c.pages || []).join(", ")}`).join("\n");
  },
};

const reply = (id, result) => process.stdout.write(JSON.stringify({ jsonrpc: "2.0", id, result }) + "\n");
const fail = (id, code, message) => process.stdout.write(JSON.stringify({ jsonrpc: "2.0", id, error: { code, message } }) + "\n");
const isRequestObject = (m) => typeof m === "object" && m !== null && !Array.isArray(m);

async function dispatch(msg) {
  const { id, method } = msg;
  const params = isRequestObject(msg.params) ? msg.params : {};
  if (id === undefined || id === null) return; // notifications/initialized 등 알림 — 응답 금지
  switch (method) {
    case "initialize": {
      const v = SUPPORTED.includes(params.protocolVersion) ? params.protocolVersion : "2025-03-26";
      return reply(id, { protocolVersion: v, capabilities: { tools: {} }, serverInfo: { name: NAME, version: VERSION } });
    }
    case "ping": return reply(id, {});
    case "tools/list": return reply(id, { tools: TOOLS });
    case "tools/call": {
      const name = params.name;
      if (typeof name !== "string" || !Object.hasOwn(handlers, name)) return fail(id, -32602, `알 수 없는 도구: ${name}`);
      try {
        const text = await handlers[name](isRequestObject(params.arguments) ? params.arguments : {});
        return reply(id, { content: [{ type: "text", text }] });
      } catch (e) {
        return reply(id, { content: [{ type: "text", text: e.message }], isError: true });
      }
    }
    default: return fail(id, -32601, `지원하지 않는 메서드: ${method}`);
  }
}

let chain = Promise.resolve(); // 요청 순서대로 응답
readline.createInterface({ input: process.stdin, crlfDelay: Infinity }).on("line", (line) => {
  if (!line.trim()) return;
  let msg;
  // 오류 응답도 chain에 태워 입력 순서대로 출력한다 (동기 write는 앞선 요청의 비동기 응답을 추월함)
  try { msg = JSON.parse(line); } catch { chain = chain.then(() => fail(null, -32700, "JSON 파싱 실패")); return; }
  if (!isRequestObject(msg)) { chain = chain.then(() => fail(null, -32600, "Invalid Request")); return; }
  chain = chain
    .then(() => dispatch(msg))
    .catch((e) => { log("dispatch error:", e?.message); if (msg?.id != null) fail(msg.id, -32603, String(e?.message)); });
});
process.stdin.on("end", () => chain.catch(() => {}).then(() => process.exit(0)));
