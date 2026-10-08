---
ko_hash: a807f67585d61891d2c7c61ee39e5b9254205160
---
# Maintenance — inclusion, evidence, and review

_Last updated: 2026-09 · owner: Youngjin · volatility: medium_

**L0 TL;DR**: Separate relevance, release status, evidence, permitted use, and support. Automation detects missing/inconsistent records; people own factual review and customer-site approval.

## Inclusion criteria (THE FILTER)

The old “2 of 4” rule is now only a **relevance signal**: customer demand, AWS mapping, release status, and site cases. AWS mapping plus a roadmap does not establish verification.

Inclusion requires **all** of: (1) a customer problem or R&D question, (2) exact primary source/check date/version, (3) evidence, limits, and permitted use, (4) an owner and actionable next step. Numbers need conditions, samples, and units. Items without primary-source checks stay in Radar.

Research can support hypothesis-driven R&D guidance, not operational performance promises. Expansion recommendations additionally need the [pilot card](start.md#pilot) and [site gates](operations.md#release).

## Maturity, sources, and use

| Dimension | Label | Interpretation |
|---|---|---|
| Release | GA / Preview / Research / not applicable | Per product; do not label principles, laws, or algorithms GA |
| Evidence | Vendor announcement / source comparison / reproduction / customer-site validation | Do not infer the next stage automatically |
| Use | Learning/R&D / PoC evaluation / operational expansion review | Record validated scope and limitations |
| Support | AWS service / model provider / partner-SI / sample maintainer | Separate contracts and site responsibilities |

`[1]` official documentation/paper, `[2]` documented reproduction, `[3]` vendor announcement, `[4]` unverified are **source types**, not a ranking or official AWS endorsement. `[2]` requires operator, versions, environment, logs, and measurement conditions. Legacy `[2]` without logs is not reproduction evidence. An announcement is not GA; one run is not production validation.

## Metadata and freshness

Keep page `_owner: name · updated: YYYY-MM · volatility: high/medium/low_` metadata. This date describes the **page edit/review scope**; partial edits do not refresh unrelated claim dates. Page badges warn after high 1 / medium 3 / low 6 months.

Add decision-critical claims to [evidence records](evidence.md). `checked_on` is the source comparison date, `review_after_days` the claim review interval, and `pages` identifies affected summaries/pillars. Unmigrated legacy claims remain explicitly outside the register.

## Standard template

```text
Item / customer problem:
Release / evidence level / intended use / support owner:
L0: what it is and under which conditions it applies:
Alternatives / AWS mapping and prerequisites:
Evidence ID / exact source URL / version / check date:
Experiment: environment, sample, units, logs / reproducer:
Limitations / cost, success, and stop criteria:
Next action / execution asset / operating handover:
Owner / human reviewer or pending:
```

Keep L0 short; link or collapse details. Define unfamiliar terms with a first-use `[^term]` and 1–2 sentences under the final `<!-- 용어 각주 -->` marker. Preserve footnote IDs, URLs, and structure in translations. Executive summaries must retain pillar conditions/limits. Keep internal customer information and sales strategy out of public pages.

## Playbook promotion pipeline

1. Record topic, primary source, and customer problem in Radar or the candidate form.
2. Owner checks inclusion requirements and assigns specialist review; scans cannot promote automatically.
3. Compare evidence, versions, dates, and measurement conditions; state R&D/PoC/site-validation scope.
4. Update Korean originals, affected summaries, and en/zh/ja together.
5. Render evidence, sync hashes, run checks, then review and integrate.

## Roles and outstanding review

| Role | Responsibility |
|---|---|
| Owner Youngjin | Assign reviews, decide inclusion, manage updates |
| Human specialists — unassigned | Licensing / AWS services-Regions / robotics-safety / reproduction |
| Automation/comparison tools | Candidate intake, assisted source comparison, metadata/link/sync checks |

Naming one owner does not resolve review bottlenecks. Record specialist owners after they accept. Distinguish automated comparison from human approval; never invent reviewers.

## Checks and limitations

```bash
python3 scripts/check_evidence.py
python3 scripts/check_translation_sync.py
python3 scripts/check_nav_index_sync.py
python3 scripts/check_staleness.py --check
mkdocs build --strict
```

Invalid evidence/rendering, nav drift, missing metadata, and internal document link/anchor errors block deployment. Overdue/human-pending review is reported; translation drift is currently warn-only in CI. Separately require **zero translation drift before commit**. Builds do not verify external reachability, facts, translation meaning, or robot execution.

**➡️ Next action**: assign pending [evidence reviews](evidence.md#review) by specialty and review the earliest-due sources with every affected page.

_owner: Youngjin · updated: 2026-09 · volatility: medium_
