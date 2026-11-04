# Physical AI Playbook — Overview and Fact-Checking

> Written: 2026-11-04 · Site: <https://comeddy.github.io/pai-playbook/>
> ⚠️ A personal project, not official AWS documentation. Always reconfirm service specs, pricing, and Region availability in the official documentation.

**In one line:** a shared decision tool for customers and AWS SAs that separates what is truly ready from what is still worth watching — with sources attached.

## Part 1. About the Playbook

**What it is.** The Physical AI Playbook is a public, practical guide for customers who want to apply AI to robots and autonomous systems, and for the AWS Solutions Architects who support them. It starts from one question — "Is Physical AI the right fit for this task?" — and carries it through pilot economics, executing data, simulation, and fine-tuning, and finally failure and recovery in operations, as a single flow. It is published on the web with a Korean source and English, Chinese, and Japanese translations, and it can also be queried directly from AI assistants through an MCP server.

**How the menu is organized.** The top menu has six groups. *Getting Started* is the entry point, covering business fit and ROI, the execution path, and operations and recovery. *Technology Pillars* guides technology choices along five axes — data collection (P1), VLA model training (P2), simulation (P3), sim-to-real (P4), and agent orchestration (P5) — plus a decision tree. *Executives* holds a briefing for investment decisions and a guide for executive conversations. *News & Resources* holds summaries of the AWS Physical AI blog, workshops, and Radar, the queue of items awaiting verification. *Reference* holds the evidence records, the maintenance rules, and how to connect via MCP.

**What it contains.** Each entry opens with a one-line summary and then reads in order: customer need, solution overview, AWS mapping, decision criteria, customer cases, next action, and related assets. Every claim carries a source type ([1] official docs or papers, [2] documented reproduction, [3] vendor announcement, [4] unverified) and a maturity label (GA, Preview, Research, Hype, Retired), and every page states its owner, review month, and volatility. The playbook's identity rests on one rule: never inflate an "announcement" into GA, or "we ran it ourselves" into production validation.

**Promotion criteria.** A new technology does not go straight into the pillars; it lands on Radar first. Every Radar item states the condition for moving into the main text — for example "weights released or GA, plus independent performance validation," "GA plus a real deployment," or "peer review plus reproduction." To enter the main text, an item needs all four of the following: a customer problem to solve; an exact primary source with check date and version; the limits of the evidence and the permitted scope of use; and an owner with an actionable next step.

**How it is updated.** Automation and people split the work. Every day a cloud routine scans the web, arXiv, and the AWS blog and adds news and Radar candidates as "unverified · awaiting source check." The owner then checks the primary source directly, settles the grade, and decides whether to promote. Nothing is promoted by an automated scan alone. Once promotion is decided, the Korean source, the affected summaries, and the three translations are changed together, and the change ships only after the evidence, translation-sync, and build checks all pass. Every page also declares who refreshes it and what they watch, and a daily GitHub Actions job raises missing blog posts, stalled routines, and overdue reviews as issues, so no page goes stale quietly.

**Why it matters.** In the end, the playbook offers not a list of answers but the grounds for a decision. It lets customers and SAs open the same page, sort "what we can use now" from "what we should keep watching," and agree on the next step in the same language.

## Part 2. How Fact-Checking Works

> Sources: `docs/maintenance.md`, `scripts/radar_scan.md`, `docs/assets/claims.json`, `scripts/check_*.py`
> Key point: **automation catches omissions, mismatches, and format errors; people confirm facts and promotions against primary sources.** Verification that was not actually done is never recorded as complete.

### 1. Core principles

| Principle | What it means |
|---|---|
| Primary sources first | Official docs, papers, GitHub releases, and vendors' original blog posts are the reference. Secondary coverage is background only; dates, versions, and licenses — which web summaries often get wrong — are rechecked in the original. |
| Source type labels | `[1]` official docs or papers · `[2]` documented reproduction · `[3]` vendor announcement · `[4]` unverified. These are **types**, not a ranking. |
| No inflation | Do not turn "announced" into GA, "we ran it" into production validation, or a vendor's own numbers into independent validation. |
| Separate dimensions | Record release status (GA/Preview/Research), evidence level (vendor claim/source check/reproduction/customer field validation), intended use (learning·R&D/PoC/production rollout), and support owner separately. Never infer a higher level from a lower one. |
| Numbers need conditions | When quoting a number, include measurement conditions, sample, and units. Mark self-reported figures "self-reported, do not quote to customers." |
| People vs. automation | Record automated source comparison, experimental reproduction, and human approval as distinct states. |

### 2. Verification steps by intake path

#### 2-1. Automated intake (daily routine → News and Radar)

1. A cloud routine (daily at 02:12 UTC) scans the web, arXiv, and the AWS Physical AI blog RSS feed.
2. **Every** incoming item enters as `[4]` unverified. News items get a `⏳ awaiting source check (auto-scan date)` marker.
3. Links are checked for HTTP 200 with `curl -sIL -o /dev/null -w '%{http_code}'` before insertion. If the routine's egress is blocked and the check can't run, the commit message says "links not verified (egress)."
4. Automation never changes the grade or marker of an existing item.

#### 2-2. Owner source check (`[4]` → `[3]`/`[1]`)

1. From an environment with open egress, recheck every link with `curl`.
2. Open the primary source and compare **dates, versions, licenses, and numbers**.
3. Record the result inside the entry, in the form `🔗 link 200 · source checked YYYY-MM-DD`.
4. Correct what is wrong, and delete claims that are not in the source.
   - 2026-09-27 recheck: 6 of 10 items corrected. For example, a claim of a "live hardware demo" that was not in the IFA press release was removed.
5. Once the source is confirmed, News items move to `[3]` (vendor original) and the ⏳ marker is removed. Facts confirmed in official documentation are marked `[1]`, while performance claims stay unverified.
   - Example: π0.7. The official announcement is `[1]`, but its performance claims remain unverified.

#### 2-3. Inclusion and promotion into the pillars

Every Radar item lists its **promotion condition** — for example "weights released or GA + independent performance validation," "GA + real deployment," or "peer review + reproduction." Inclusion in the main text requires **all** four of the following (THE FILTER):

1. A customer problem or R&D question to solve
2. An exact primary source, check date, and applicable version
3. Evidence, its limits, and the permitted scope of use
4. An owner and an actionable next step

The promotion pipeline runs in this order (`maintenance.md`):

1. Record the item on Radar or in the candidate form.
2. The owner confirms the inclusion criteria and the reviewers. **Nothing is promoted on an automated scan alone.**
3. Compare evidence, version, date, and measurement conditions, and state whether the scope is R&D, PoC, or field validation.
4. Update the Korean source, the affected summaries, and the en/zh/ja translations together.
5. Generate the evidence display, sync translation hashes, pass the checks, then ship.

### 3. Evidence records (`docs/assets/claims.json`)

Claims that affect customer decisions (licensing, data residency, cost, performance, and so on) are kept as separate records.

| Field | Meaning |
|---|---|
| `checked_on` | The date the source was **actually** compared |
| `review_after_days` | Per-claim review interval (30 days, 90 days, etc.) |
| `status` | `source-checked` · `reproduction-pending` · `withdrawn` |
| `verified_by` | Who did the comparison, e.g. "Codex (source comparison)" |
| `human_review` | `pending` / `complete`. `complete` requires a named `human_reviewer` (enforced by the check script). |
| `pages` · `sources` | Affected pages and primary-source URLs |

Running `python3 scripts/check_evidence.py --render` generates the evidence page in all four languages. As of 2026-11-04 there are 7 records, and all 7 are still awaiting human review.

### 4. What the automated checks catch — and what they don't

| Check | Catches |
|---|---|
| `check_evidence.py` | Evidence record structure, status values, mismatches across the four language displays, overdue reviews (warning) |
| `check_translation_sync.py` | `ko_hash` mismatch between the Korean source and translations (translation drift) |
| `check_nav_index_sync.py` | Mismatch between the nav and the home-page list |
| `check_refresh_paths.py` | Pages with no refresh path declared in `refresh.yml` |
| `check_staleness.py` | Pages whose `updated` metadata is past the volatility deadline (1/3/6 months) |
| `mkdocs build --strict` | Missing metadata, broken internal links and anchors |
| `source-drift` (Actions, daily) | Posts in the RSS feed but missing from News (3+ days after publication), stalled routines, overdue owner-page reviews |

**What they don't catch:** whether external links are alive, whether claims are true, whether a translation means the same thing, and whether anything actually runs on a robot. People check these four. For external links, a manual `curl` 200 check is the only line of defense.

### 5. Checklist — fact-checking a single entry

- [ ] Link returns `curl -sIL` 200 (official sources only)
- [ ] Date, version, and license confirmed in the primary source (check the code LICENSE and the weights license separately)
- [ ] Numbers: measurement conditions, sample, units, and whether they are self-reported
- [ ] Release label matches the source wording (Preview ≠ GA, early access ≠ public)
- [ ] Region and data-processing location (available in Seoul does not mean processed in Seoul — cross-Region inference can move it)
- [ ] Source type `[1]`–`[4]` updated and check date recorded
- [ ] If it affects customer decisions, update `claims.json` → `--render`
- [ ] Reflected in all four languages → `ko_hash` updated → gates pass
- [ ] Out-of-scope findings logged as GitHub issues

### 6. Real cases

| Date | Case | Lesson |
|---|---|---|
| 2026-09-27 | Rechecked 10 Radar intake items, corrected 6 | Auto-scan summaries often get links and numbers wrong |
| 2026-10 | News missed three weeks of posts | Date badges alone aren't enough → added RSS comparison (`source-drift`) |
| 2026-11-04 | Pillars went two months without review | Added `review_alert`, which watches the owner's review month, not commit dates |
| 2026-11-04 | GR00T N1.7 license | Check code (Apache-2.0) and weights (NVIDIA Open Model License) separately; keep the warning when the README intro and the LICENSE disagree |
| 2026-11-04 | Isaac Sim 6.x · Isaac Lab 3.0 | GA confirmed from primary sources (GitHub releases, GA announcement). Updating P3 awaits owner approval (issue #37) — confirming and promoting are separate steps |
