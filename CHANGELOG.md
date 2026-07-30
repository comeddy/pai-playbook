# Changelog

[![English](https://img.shields.io/badge/lang-English-blue)](#english)
[![한국어](https://img.shields.io/badge/lang-%ED%95%9C%EA%B5%AD%EC%96%B4-red)](#korean)
[![中文](https://img.shields.io/badge/lang-%E4%B8%AD%E6%96%87-green)](#chinese)
[![日本語](https://img.shields.io/badge/lang-%E6%97%A5%E6%9C%AC%E8%AA%9E-orange)](#japanese)

---

<a id="english"></a>

# English

All notable changes to this project are documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). Versions are git-tagged (v1.0.0+).

## [Unreleased]

## [1.5.0] - 2026-07-24

### Added

- Add a footer link (history icon) to the GitHub changelog on every page in all four languages
- Register 8 verified AWS official Physical AI repos (7 aws-samples + 1 awslabs) as related assets across pillars, each with maturity caveats, in all four languages: AWS Physical AI Toolchain (OSMO on EKS) and Self-improving Physical AI and Agentic AI Robot (pillar 5), Physical AI Scaffolding Kit (pillars 2-3), Embodied AI Platform (pillar 2), VLA Simulator — 1-click benchmarking of 7 VLA models on EC2 (pillar 3), Android PAI data collector app and VAMS visual asset management (pillar 1)

### Changed

- Update the Radar RLDX-1 entry: replace "no AWS connection found" with a simulation-benchmarking-scoped connection (the aws-samples VLA Simulator runs RLDX-1 on EC2 within its non-commercial license; no commercial positioning)
- Record the 2026-07-20 weekly scan intake in the Radar (8 items) and its primary-source verification results (0 promoted, 6 corrected), in all four languages
- Expand the weekly scan runbook scope: add physical AI data (robot data collection and datasets) to the arXiv query, and The Robot Report and IEEE Spectrum Robotics to the news sources

## [1.4.0] - 2026-07-19

### Added

- Add a standalone intro landing page at `/intro/` (self-contained HTML) and expand it to four languages (`/intro/en|zh|ja/`) with hreflang alternates and language switchers in both the header nav and the footer
- Introduce a multi-verifier scheme for primary-source verification: an optional `verified by:` metadata field (the owner stays a single person), a "Verifiers (multiple allowed)" role in the promotion pipeline, and a verifier input on the promotion issue form — applied across all four languages
- Add a bilingual CHANGELOG with git tags (v1.0.0–v1.3.0), GitHub Releases, and a README release badge
- Add `docs/CNAME` groundwork for the `pai.zerojin.art` custom domain (domain not yet activated)

## [1.3.0] - 2026-07-19

### Added

- Register verified AWS official workshops: Bedrock AgentCore Getting Started, AgentCore Deep Dive (pillar 5), and IoT TwinMaker end-to-end (pillar 3)
- Place the Physical AI E2E workshop (Korean) in pillar 2 (GR00T VLA fine-tuning track) and pillar 3 (Isaac Lab RL track)
- Add execution assets: LeRobot teleop data collection on Greengrass sample (aws-samples), Omniverse digital twin hands-on (Korean), and an internal AWS-NVIDIA robotics reference architecture (marked internal-only)

### Fixed

- Disambiguate "국내" (domestic) in all translations to explicit Korean/韩国/韓国 (30 spots) — Chinese readers previously read it as "in China"; add a glossary rule to prevent regression
- Unify spelling 워크샵 → 워크숍 (standard orthography) and 실재 → 실제 after a full 4-language proofreading sweep (40 files, only these findings)

## [1.2.0] - 2026-07-18

### Added

- Add a "Guide" page explaining the full verification pipeline (candidate discovery → Radar → THE FILTER → promotion → monitoring), exposed via top tab navigation
- Expand the FAQ from Top 10 to Top 20 with a source column (items 11–20 from public-community research)
- Add the Radar "latest scan intake" section with a weekly automated scan (cloud routine, Mondays 02:00 UTC) and its runbook
- Add 18 Mermaid diagrams across pillars, decision trees, guide, and maintenance; replace all ASCII diagrams
- Add ~46 curated official links on first occurrences of bold product names (all pre-verified with curl)
- Register verified workshop assets: NVIDIA Isaac Lab on AWS, and the self-built pai-sim-isaaclab hands-on (promoted into the next-action line)
- Add footer social links (GitHub repo, LinkedIn, Bluesky), a bilingual README, and a CC-BY-4.0 LICENSE

### Changed

- Rename the home title to "Physical AI Playbook 안내"; rename the action label "SA 다음 액션" to "다음 액션" (118 spots); rename the promotion-pipeline heading (with all cross-page anchors updated)
- Update radar intake entries after primary-source verification (promote Apptronik Apollo 2, correct the Atlas misnomer, correct AgiBot/1X NEO claims)

### Fixed

- Fix a list-rendering bug where bullets collapsed into paragraphs: insert 160 missing blank lines before lists (5 pillars × 4 languages)

## [1.1.0] - 2026-07-18

### Added

- Publish the site in four languages: English, Chinese (Simplified), and Japanese translations of all pages, with Korean as the source of truth (mkdocs-static-i18n suffix structure, language switcher)
- Add ko_hash-based translation drift detection (`scripts/check_translation_sync.py`, warn-only CI step)
- Add the translation glossary (`i18n/glossary.md`) and the translate-sync skill (detect → glossary → translate changed files → strict-build gate)
- Extend the staleness badge to inject per-language badges into translated pages
- Add multilingual site links to the README

### Changed

- Remove `navigation.instant` (documented incompatibility with the i18n language switcher)

## [1.0.0] - 2026-07-11

### Added

- Initial release: 8 pages (home, pillars 1–5, decision trees, Radar, maintenance) generated from the master prompt with per-page adversarial fact-checking
- MkDocs Material site with GitHub Actions deploy to GitHub Pages (strict-build gate: broken links/anchors fail the deploy)
- Automated staleness badges based on per-page volatility (1/3/6-month review cadence), refreshed by a weekly cron redeploy
- Promotion issue form with the THE FILTER checklist built in
- Owner assignment for pillar pages

[Unreleased]: https://github.com/comeddy/pai-playbook/compare/v1.5.0...HEAD
[1.5.0]: https://github.com/comeddy/pai-playbook/compare/v1.4.0...v1.5.0
[1.4.0]: https://github.com/comeddy/pai-playbook/compare/v1.3.0...v1.4.0
[1.3.0]: https://github.com/comeddy/pai-playbook/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/comeddy/pai-playbook/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/comeddy/pai-playbook/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/comeddy/pai-playbook/releases/tag/v1.0.0

---

<a id="korean"></a>

# 한국어

이 프로젝트의 주요 변경 사항을 이 파일에 기록합니다.
형식은 [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)를 따르고, [Semantic Versioning](https://semver.org/spec/v2.0.0.html)을 준수합니다. 버전은 git 태그(v1.0.0+)로 관리합니다.

## [Unreleased]

## [1.5.0] - 2026-07-24

### Added

- 모든 페이지 푸터에 GitHub CHANGELOG 링크(history 아이콘) 추가, 4개 언어 공통 적용
- 검증된 AWS 공식 Physical AI 리포 8종(aws-samples 7 + awslabs 1)을 필러별 관련 자산으로 등재, 각각 성숙도 캐비앗 명시, 4개 언어 반영: AWS Physical AI Toolchain(OSMO on EKS)·Self-improving Physical AI·Agentic AI Robot(pillar 5), Physical AI Scaffolding Kit(pillar 2~3), Embodied AI Platform(pillar 2), VLA Simulator — 7개 VLA 모델 원클릭 EC2 벤치마킹(pillar 3), Android PAI 데이터 수집 앱·VAMS 시각 자산 관리(pillar 1)

### Changed

- Radar RLDX-1 항목 갱신: "AWS 연계 근거 없음" 표기를 시뮬레이션 벤치마킹 한정 연계로 교체(aws-samples VLA Simulator가 비상업 라이선스 허용 범위 내에서 RLDX-1을 EC2에서 구동, 상업 포지셔닝 불가)
- Radar에 2026-07-20 주간 스캔 유입(8건)과 1차 출처 검증 결과(승격 0건, 정정 6건) 기록, 4개 언어 반영
- 주간 스캔 런북 범위 확장: arXiv 쿼리에 physical AI data(로봇 데이터 수집·데이터셋) 추가, 뉴스 소스에 The Robot Report·IEEE Spectrum Robotics 추가

## [1.4.0] - 2026-07-19

### Added

- `/intro/` 독립 랜딩 페이지 추가(단일 HTML) 및 4개 언어 확장(`/intro/en|zh|ja/`) — hreflang 대체 링크와 header nav·footer 양쪽 언어 전환기 포함
- 1차 출처 검증자 다인 체계 도입: 선택 `검증:` 메타데이터 필드(owner는 1명 유지), 승격 파이프라인 "검증 담당(복수 가능)" 역할, 승격 이슈 폼 검증자 입력 필드 — 4개 언어 반영
- 이중 언어 CHANGELOG·git 태그(v1.0.0~v1.3.0)·GitHub Releases·README 릴리스 뱃지 추가
- `pai.zerojin.art` 커스텀 도메인용 `docs/CNAME` 기반 작업 추가(도메인 미활성)

## [1.3.0] - 2026-07-19

### Added

- 검증된 AWS 공식 워크숍 등재: Bedrock AgentCore 시작·Deep Dive(pillar 5), IoT TwinMaker E2E(pillar 3)
- Physical AI E2E 워크숍(한국어)을 pillar 2(GR00T VLA 파인튜닝 트랙)와 pillar 3(Isaac Lab RL 트랙)에 배치
- 실행 자산 추가: LeRobot 텔레옵 수집 on Greengrass 샘플(aws-samples), Omniverse 디지털 트윈 핸즈온(한국어), 사내 AWS·NVIDIA 로보틱스 참조 아키텍처(사내 전용 표기)

### Fixed

- 번역본의 "국내" 모호함을 Korean/韩国/韓国으로 명시(30곳) — 중국어 독자에게 중국으로 읽히던 문제, 용어집 규칙으로 재발 방지
- 4개 언어 전수 교정(40개 파일) 결과 반영: 워크샵 → 워크숍 표기 통일, 실재 → 실제 수정

## [1.2.0] - 2026-07-18

### Added

- 검증 파이프라인 전과정(후보 발견 → Radar → THE FILTER → 승격 → 감시)을 설명하는 "가이드" 페이지 신설, 상단 탭 내비게이션으로 노출
- FAQ를 Top 10에서 Top 20으로 확장하고 출처 열 추가(11~20번은 공개 커뮤니티 조사 기반)
- Radar "최신 스캔 유입" 섹션 + 주간 자동 스캔(클라우드 루틴, 매주 월 02:00 UTC) + 런북 추가
- 필러·의사결정 트리·가이드·유지보수에 Mermaid 다이어그램 18개 추가, ASCII 다이어그램 전량 대체
- 굵은 제품명 첫 등장에 선별 공식 링크 약 46곳 추가(전수 curl 사전 검증)
- 검증된 워크숍 자산 등재: NVIDIA Isaac Lab on AWS, 자체 개발 pai-sim-isaaclab 핸즈온(다음 액션으로 승격)
- 푸터 소셜 링크(GitHub 저장소·LinkedIn·Bluesky), 이중 언어 README, CC-BY-4.0 LICENSE 추가

### Changed

- 홈 제목을 "Physical AI Playbook 안내"로 변경, 액션 라벨 "SA 다음 액션"을 "다음 액션"으로 변경(118곳), 승격 파이프라인 제목 변경(교차 페이지 앵커 일괄 갱신)
- 1차 출처 검증 결과를 Radar 유입 항목에 반영(Apptronik Apollo 2 승격, Atlas 오칭 정정, AgiBot·1X NEO 주장 정정)

### Fixed

- 불릿이 문단으로 뭉개지던 목록 렌더링 버그 수정: 목록 앞 빈 줄 160곳 삽입(필러 5개 × 4개 언어)

## [1.1.0] - 2026-07-18

### Added

- 사이트 4개 언어 발행: 전 페이지의 영어·중국어(간체)·일본어 번역, 한국어를 원본으로 유지(mkdocs-static-i18n suffix 구조, 언어 전환기)
- ko_hash 기반 번역 표류 감지 추가(`scripts/check_translation_sync.py`, 경고 전용 CI 스텝)
- 번역 용어집(`i18n/glossary.md`)과 translate-sync 스킬 추가(탐지 → 용어집 → 변경분 번역 → strict 빌드 게이트)
- staleness 배지를 번역 페이지에도 언어별로 주입하도록 확장
- README에 다국어 사이트 링크 추가

### Changed

- `navigation.instant` 제거(i18n 언어 전환기와의 문서화된 비호환)

## [1.0.0] - 2026-07-11

### Added

- 최초 릴리스: 마스터 프롬프트로 생성한 8페이지(홈·필러 1~5·의사결정 트리·Radar·유지보수), 페이지별 적대적 사실 검증 수행
- MkDocs Material 사이트 + GitHub Actions의 GitHub Pages 배포(strict 빌드 게이트: 깨진 링크·앵커는 배포 실패)
- 페이지별 변동성 기반 staleness 배지 자동화(1/3/6개월 검토 주기), 주간 cron 재배포로 갱신
- THE FILTER 체크리스트를 내장한 승격 이슈 폼 추가
- 필러 페이지 owner 지정

[Unreleased]: https://github.com/comeddy/pai-playbook/compare/v1.5.0...HEAD
[1.5.0]: https://github.com/comeddy/pai-playbook/compare/v1.4.0...v1.5.0
[1.4.0]: https://github.com/comeddy/pai-playbook/compare/v1.3.0...v1.4.0
[1.3.0]: https://github.com/comeddy/pai-playbook/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/comeddy/pai-playbook/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/comeddy/pai-playbook/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/comeddy/pai-playbook/releases/tag/v1.0.0

---

<a id="chinese"></a>

# 中文

本项目的所有重要变更均记录在此文件中。
格式遵循 [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)，并遵守 [Semantic Versioning](https://semver.org/spec/v2.0.0.html)。版本以 git 标签管理（v1.0.0+）。

## [Unreleased]

## [1.5.0] - 2026-07-24

### Added

- 在所有页面页脚添加指向 GitHub CHANGELOG 的链接（history 图标），四种语言统一应用
- 将 8 个经验证的 AWS 官方 Physical AI 仓库（aws-samples 7 个 + awslabs 1 个）登记为各支柱的相关资产，逐一标注成熟度注意事项，四种语言同步：AWS Physical AI Toolchain（OSMO on EKS）·Self-improving Physical AI·Agentic AI Robot（pillar 5），Physical AI Scaffolding Kit（pillar 2~3），Embodied AI Platform（pillar 2），VLA Simulator —— 在 EC2 上一键基准测试 7 个 VLA 模型（pillar 3），Android PAI 数据采集应用·VAMS 视觉资产管理（pillar 1）

### Changed

- 更新 Radar 中 RLDX-1 条目：将"未发现 AWS 关联"改为仅限仿真基准测试的关联（aws-samples VLA Simulator 在非商业许可允许范围内于 EC2 上运行 RLDX-1，不可用于商业定位）
- 在 Radar 中记录 2026-07-20 周扫描流入（8 条）及其一手来源验证结果（晋升 0 条、更正 6 条），四种语言同步
- 扩展周扫描 runbook 范围：在 arXiv 查询中加入 physical AI data（机器人数据采集·数据集），新闻来源加入 The Robot Report·IEEE Spectrum Robotics

## [1.4.0] - 2026-07-19

### Added

- 新增 `/intro/` 独立着陆页（单文件 HTML）并扩展为四种语言（`/intro/en|zh|ja/`）—— 含 hreflang 替代链接及 header nav·footer 双处语言切换器
- 引入一手来源多人验证机制：可选的 `验证:` 元数据字段（owner 保持 1 人）、晋升管道中的"验证负责人（可多人）"角色、晋升议题表单的验证者输入项 —— 四种语言同步
- 新增双语 CHANGELOG·git 标签（v1.0.0~v1.3.0）·GitHub Releases·README 发布徽章
- 为自定义域名 `pai.zerojin.art` 添加 `docs/CNAME` 基础工作（域名尚未启用）

## [1.3.0] - 2026-07-19

### Added

- 登记经验证的 AWS 官方研讨会：Bedrock AgentCore 入门·Deep Dive（pillar 5）、IoT TwinMaker 端到端（pillar 3）
- 将 Physical AI E2E 研讨会（韩语）配置到 pillar 2（GR00T VLA 微调赛道）与 pillar 3（Isaac Lab RL 赛道）
- 新增执行资产：LeRobot 遥操作采集 on Greengrass 示例（aws-samples）、Omniverse 数字孪生实操（韩语）、内部 AWS·NVIDIA 机器人参考架构（标注仅限内部）

### Fixed

- 消除译文中"国内"的歧义，明确改为 Korean/韩国/韓国（30 处）—— 此前中文读者会误读为中国，并新增术语表规则防止回归
- 反映四种语言全量校对（40 个文件）结果：统一 워크샵 → 워크숍 的拼写，修正 실재 → 실제

## [1.2.0] - 2026-07-18

### Added

- 新设讲解完整验证管道（候选发现 → Radar → THE FILTER → 晋升 → 监控）的"指南"页面，通过顶部标签导航露出
- 将 FAQ 从 Top 10 扩展为 Top 20 并增加来源列（第 11~20 条基于公开社区调研）
- 新增 Radar"最新扫描流入"栏目 + 周自动扫描（云例程，每周一 02:00 UTC）+ runbook
- 在支柱·决策树·指南·维护页新增 18 个 Mermaid 图，全面替换 ASCII 图
- 在加粗产品名首次出现处添加约 46 个精选官方链接（全部经 curl 预先验证）
- 登记经验证的研讨会资产：NVIDIA Isaac Lab on AWS、自研 pai-sim-isaaclab 实操（晋升为后续行动）
- 新增页脚社交链接（GitHub 仓库·LinkedIn·Bluesky）、双语 README、CC-BY-4.0 LICENSE

### Changed

- 首页标题改为"Physical AI Playbook 안내"，行动标签"SA 다음 액션"改为"다음 액션"（118 处），晋升管道标题变更（跨页锚点一并更新）
- 将一手来源验证结果反映到 Radar 流入条目（晋升 Apptronik Apollo 2、更正 Atlas 误称、更正 AgiBot·1X NEO 的主张）

### Fixed

- 修复列表项被压成段落的渲染缺陷：在列表前插入 160 处缺失的空行（5 个支柱 × 4 种语言）

## [1.1.0] - 2026-07-18

### Added

- 网站以四种语言发布：全部页面的英语·中文（简体）·日语翻译，韩语保持为源文本（mkdocs-static-i18n suffix 结构、语言切换器）
- 新增基于 ko_hash 的翻译漂移检测（`scripts/check_translation_sync.py`，仅警告的 CI 步骤）
- 新增翻译术语表（`i18n/glossary.md`）与 translate-sync 技能（检测 → 术语表 → 翻译变更文件 → strict 构建门禁）
- 扩展 staleness 徽章，使其按语言注入到翻译页面
- 在 README 中添加多语言站点链接

### Changed

- 移除 `navigation.instant`（与 i18n 语言切换器存在已文档化的不兼容）

## [1.0.0] - 2026-07-11

### Added

- 首次发布：由主提示生成的 8 个页面（首页·支柱 1~5·决策树·Radar·维护），逐页执行对抗性事实核查
- MkDocs Material 站点 + GitHub Actions 部署到 GitHub Pages（strict 构建门禁：损坏的链接·锚点导致部署失败）
- 基于页面易变性的 staleness 徽章自动化（1/3/6 个月复核周期），由每周 cron 重新部署刷新
- 新增内置 THE FILTER 清单的晋升议题表单
- 指定支柱页面 owner

[Unreleased]: https://github.com/comeddy/pai-playbook/compare/v1.5.0...HEAD
[1.5.0]: https://github.com/comeddy/pai-playbook/compare/v1.4.0...v1.5.0
[1.4.0]: https://github.com/comeddy/pai-playbook/compare/v1.3.0...v1.4.0
[1.3.0]: https://github.com/comeddy/pai-playbook/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/comeddy/pai-playbook/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/comeddy/pai-playbook/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/comeddy/pai-playbook/releases/tag/v1.0.0

---

<a id="japanese"></a>

# 日本語

このプロジェクトの主要な変更点をこのファイルに記録します。
形式は [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) に従い、[Semantic Versioning](https://semver.org/spec/v2.0.0.html) を遵守します。バージョンは git タグ（v1.0.0+）で管理します。

## [Unreleased]

## [1.5.0] - 2026-07-24

### Added

- 全ページのフッターに GitHub CHANGELOG へのリンク（history アイコン）を追加、4言語共通で適用
- 検証済みの AWS 公式 Physical AI リポジトリ 8 種（aws-samples 7 + awslabs 1）をピラー別の関連資産として登録、それぞれ成熟度の注意書きを明記、4言語に反映：AWS Physical AI Toolchain（OSMO on EKS）・Self-improving Physical AI・Agentic AI Robot（pillar 5）、Physical AI Scaffolding Kit（pillar 2～3）、Embodied AI Platform（pillar 2）、VLA Simulator — 7 つの VLA モデルを EC2 でワンクリック・ベンチマーク（pillar 3）、Android PAI データ収集アプリ・VAMS 視覚資産管理（pillar 1）

### Changed

- Radar の RLDX-1 項目を更新：「AWS 連携の根拠なし」表記をシミュレーションベンチマーク限定の連携に置き換え（aws-samples VLA Simulator が非商用ライセンスの許容範囲内で RLDX-1 を EC2 上で実行、商用ポジショニングは不可）
- Radar に 2026-07-20 週次スキャン流入（8 件）と一次ソース検証結果（昇格 0 件・訂正 6 件）を記録、4言語に反映
- 週次スキャン runbook の範囲を拡張：arXiv クエリに physical AI data（ロボットデータ収集・データセット）を追加、ニュースソースに The Robot Report・IEEE Spectrum Robotics を追加

## [1.4.0] - 2026-07-19

### Added

- `/intro/` 独立ランディングページを追加(単一 HTML)し、4言語へ拡張（`/intro/en|zh|ja/`）— hreflang 代替リンクと header nav・footer 両方の言語スイッチャーを含む
- 一次ソース検証の複数検証者体制を導入：任意の `検証:` メタデータフィールド（owner は 1 名を維持）、昇格パイプラインの「検証担当（複数可）」役割、昇格イシューフォームの検証者入力欄 — 4言語に反映
- バイリンガル CHANGELOG・git タグ（v1.0.0～v1.3.0）・GitHub Releases・README リリースバッジを追加
- カスタムドメイン `pai.zerojin.art` 用の `docs/CNAME` 基盤作業を追加（ドメインは未有効化）

## [1.3.0] - 2026-07-19

### Added

- 検証済みの AWS 公式ワークショップを登録：Bedrock AgentCore 入門・Deep Dive（pillar 5）、IoT TwinMaker エンドツーエンド（pillar 3）
- Physical AI E2E ワークショップ（韓国語）を pillar 2（GR00T VLA ファインチューニングトラック）と pillar 3（Isaac Lab RL トラック）に配置
- 実行資産を追加：LeRobot テレオペ収集 on Greengrass サンプル（aws-samples）、Omniverse デジタルツインハンズオン（韓国語）、社内 AWS・NVIDIA ロボティクス参照アーキテクチャ（社内限定と表記）

### Fixed

- 翻訳における「国内」の曖昧さを Korean/韩国/韓国 に明示（30 箇所）— 中国語読者に中国と読まれていた問題、用語集ルールで再発防止
- 4言語の全数校正（40 ファイル）の結果を反映：워크샵 → 워크숍 の表記統一、실재 → 실제 の修正

## [1.2.0] - 2026-07-18

### Added

- 検証パイプラインの全工程（候補発見 → Radar → THE FILTER → 昇格 → 監視）を説明する「ガイド」ページを新設、上部タブナビゲーションで公開
- FAQ を Top 10 から Top 20 へ拡張し出典列を追加（11～20 番は公開コミュニティ調査に基づく）
- Radar「最新スキャン流入」セクション + 週次自動スキャン（クラウドルーチン、毎週月曜 02:00 UTC）+ runbook を追加
- ピラー・意思決定ツリー・ガイド・メンテナンスに Mermaid 図 18 個を追加、ASCII 図を全量置き換え
- 太字の製品名の初出箇所に厳選した公式リンクを約 46 箇所追加（全数 curl で事前検証）
- 検証済みワークショップ資産を登録：NVIDIA Isaac Lab on AWS、自作 pai-sim-isaaclab ハンズオン（次のアクションへ昇格）
- フッターのソーシャルリンク（GitHub リポジトリ・LinkedIn・Bluesky）、バイリンガル README、CC-BY-4.0 LICENSE を追加

### Changed

- ホームのタイトルを「Physical AI Playbook 안내」に変更、アクションラベル「SA 다음 액션」を「다음 액션」に変更（118 箇所）、昇格パイプラインの見出しを変更（ページ横断アンカーを一括更新）
- 一次ソース検証の結果を Radar 流入項目に反映（Apptronik Apollo 2 を昇格、Atlas の誤称を訂正、AgiBot・1X NEO の主張を訂正）

### Fixed

- 箇条書きが段落に潰れるリストレンダリング不具合を修正：リスト前の空行 160 箇所を挿入（ピラー 5 × 4言語）

## [1.1.0] - 2026-07-18

### Added

- サイトを 4言語で公開：全ページの英語・中国語（簡体字）・日本語翻訳、韓国語をソースとして維持（mkdocs-static-i18n suffix 構造、言語スイッチャー）
- ko_hash ベースの翻訳ドリフト検知を追加（`scripts/check_translation_sync.py`、警告のみの CI ステップ）
- 翻訳用語集（`i18n/glossary.md`）と translate-sync スキルを追加（検知 → 用語集 → 変更ファイルの翻訳 → strict ビルドゲート）
- staleness バッジを翻訳ページにも言語別に注入するよう拡張
- README に多言語サイトリンクを追加

### Changed

- `navigation.instant` を削除（i18n 言語スイッチャーとの文書化された非互換）

## [1.0.0] - 2026-07-11

### Added

- 初回リリース：マスタープロンプトで生成した 8 ページ（ホーム・ピラー 1～5・意思決定ツリー・Radar・メンテナンス）、ページごとに敵対的ファクトチェックを実施
- MkDocs Material サイト + GitHub Actions による GitHub Pages デプロイ（strict ビルドゲート：壊れたリンク・アンカーはデプロイ失敗）
- ページ別の揮発性に基づく staleness バッジ自動化（1/3/6 か月レビュー周期）、週次 cron 再デプロイで更新
- THE FILTER チェックリストを内蔵した昇格イシューフォームを追加
- ピラーページの owner を指定

[Unreleased]: https://github.com/comeddy/pai-playbook/compare/v1.5.0...HEAD
[1.5.0]: https://github.com/comeddy/pai-playbook/compare/v1.4.0...v1.5.0
[1.4.0]: https://github.com/comeddy/pai-playbook/compare/v1.3.0...v1.4.0
[1.3.0]: https://github.com/comeddy/pai-playbook/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/comeddy/pai-playbook/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/comeddy/pai-playbook/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/comeddy/pai-playbook/releases/tag/v1.0.0
