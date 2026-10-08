---
ko_hash: 73bcdad69049eb03dc424488198cc220d69d73d1
---
# Guide — usage and verification scope

_Last updated: 2026-09 · owner: Youngjin · volatility: medium_

**L0 TL;DR**: Customers use [Start](start.md) for fit, ROI, and pilot decisions; engineers use [Execution](execution.md) and [Operations](operations.md). AWS staff prepare with the [conversation guide](exec-guide.md).

## Reading order

Business decision → architecture decision → relevant pillar → experiment/evaluation → operating handover. Explore new topics in [Radar](radar.md); inspect sources and dates in [Evidence](evidence.md).

## Verification pipeline

Candidate intake → primary-source comparison → problem/evidence/use/owner review → source/translation updates → structural checks → review. Scans collect candidates; they do not approve promotion. The former “2 of 4” rule is only a relevance signal ([Maintenance](maintenance.md)).

## What automation checks

| Check | Scope | Does not guarantee |
|---|---|---|
| Page freshness | Age of page metadata | Every claim was rechecked |
| Claim evidence | Dates, required fields, affected pages, language rendering | Source truth or site suitability |
| Translation hash | Which source version a translation follows | Semantic accuracy |
| Strict build | Internal document links, anchors, configuration | External reachability, technical claims, successful execution |

Review claim dates, reproduction logs, and human-review status, not just page badges. See [Maintenance](maintenance.md) for procedures and [claims.json](assets/claims.json) for machine-readable records.

_owner: Youngjin · updated: 2026-09 · volatility: medium_
