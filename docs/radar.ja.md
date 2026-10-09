---
ko_hash: 65b0be28854136a23f62fbfab4bfa425d2c947db
---
# Radar — キュー / ウォッチリスト


_最終更新: 2026-09 · owner: Youngjin · volatility: 高_
[← index へ](index.md)

> **L0 TL;DR**: 原文・再現・現場確認が必要な候補です。[掲載条件](maintenance.md#掲載基準-the-filter)を全て満たしownerが用途を確認して昇格します。走査は承認しません。
>
> ⚠️ **ここにある項目を顧客提案で「成熟した能力」のように扱わないでください。** 華やかなデモがデプロイ可能性を覆い隠すことがよくあります。

---

> **確認範囲**：ページ更新日は全項目の再確認日ではありません。主要訂正の日付・再現/人の確認状態は[根拠](evidence.md)を参照し、既存項目の確認日は従来どおり適用します。

## 🔬 モデル / アルゴリズム（検証待ち）

| 項目 | ラベル | 要点 | 昇格条件 |
|---|---|---|---|
| Physical Intelligence **[π0.7](https://www.physicalintelligence.company/)** | 🔵 Research | ✨ **注目**: π0/π0.5 で VLA をリードする PI の次期フラッグシップの噂 — 登場すれば業界基準を再び塗り替える可能性<br>⏳ **待機**: 二次情報源のみ `[4]`、PI の一次確認なし | PI 公式リリース + 性能検証 |
| **[GR00T N1.6 / N1.7](https://github.com/NVIDIA/Isaac-GR00T) 商用ライセンス** | 🟡→ | ✨ **注目**: 商用許可が事実なら、顧客提案に使える希少なオープン VLA になる（N1.5 は非商用のため提案不可）<br>⏳ **待機**: 商用許可の主張が二次情報源のみ `[4]`（N1.5 はモデルカード上で明確に非商用 `[1]`） | ライブモデルカードでライセンス確定 |
| **[World-action models](https://developer.nvidia.com/isaac/gr00t)**（DreamZero → GR00T N2） | 🟡 Preview | ✨ **注目**: VLA の次世代と目される「行動まで生成するワールドモデル」軸 — NVIDIA ロードマップの方向性指標<br>⏳ **待機**: GR00T N2「年末予定」、DreamZero は研究 | GA + 実デプロイ事例 |
| Google DeepMind **[Genie 3](https://deepmind.google/discover/blog/genie-3-a-new-frontier-for-world-models/)**（ロボット学習用ワールドモデル[^wfm]） | 🟡 Preview | ✨ **注目**: フロンティア級ワールドモデルをロボット学習のデータ源に使う試み — 成立すれば実データのボトルネックを迂回<br>⏳ **待機**: ワールドモデル自体はプレビュー、ロボット学習への適用は研究 | ロボットポリシー学習の検証事例 |
| **VLM ベースの SysID[^sysid]**（[Vid2Sid](https://arxiv.org/abs/2602.19359), [Swim2Real](https://arxiv.org/abs/2603.20827)） | 🔵 Research | ✨ **注目**: 映像のみから物理パラメータを推定しシミュレーター校正を自動化 — sim-to-real の手作業キャリブレーションを不要にできる可能性<br>⏳ **待機**: 2026 プレプリント、単一ラボ | peer-review + 再現 |
| **VIRAL / [VideoMimic](https://www.videomimic.net/) / [Real2Render2Real](https://real2render2real.com/)**（visual sim-to-real[^s2r] at scale） | 🔵 Research | ✨ **注目**: 一般映像からシミュレーション環境・実演を再構成する visual sim-to-real — データ収集のコスト構造を変える候補<br>⏳ **待機**: CVPR/CoRL 研究、本番ではない | 本番デプロイの証拠 |
| **Robbyant [LingBot-VLA](https://huggingface.co/robbyant) / [UnifoLM-VLA-0](https://huggingface.co/unitreerobotics)** | 🔵 Research | ✨ **注目**: 中国発の新たなオープン VLA 系列 — オープンウェイト競争構図の観察用<br>⏳ **待機**: 二次情報源、検証なし | 一次確認 + AWS マッピング |

## 🖥️ シミュレーション / ツール（成熟度待ち）

| 項目 | ラベル | 要点 | 昇格条件 |
|---|---|---|---|
| **[Genesis](https://github.com/Genesis-Embodied-AI/Genesis)** 物理エンジン[^physeng] | ⚪ Hype | ✨ **注目**: 「超高速汎用物理エンジン」の主張で話題 — 事実なら GPU シミュレーションのコスト構造が変わる<br>⏳ **待機**: 「430,000 倍」は反駁済み `[1]`、接触マニピュレーションで遅い | 独立ベンチマーク + 本番採用 |
| **[MuJoCo Warp](https://github.com/google-deepmind/mujoco_warp)** | 🟡 Alpha | ✨ **注目**: MuJoCo の精度と GPU 並列化を両立 — Isaac 一強構図の代替候補<br>⏳ **待機**: PyPI classifier「3-Alpha」`[1]`、本番ではない | Beta/GA への移行 |
| **[NVIDIA Newton](https://github.com/newton-physics/newton)** 物理エンジン | 🟡 Preview | ✨ **注目**: Google DeepMind・Disney Research と共同開発する次世代オープンソース物理エンジン — Isaac エコシステムの次期標準の有力候補<br>⏳ **待機**: Isaac Sim 6.0 で experimental バックエンド | GA + Isaac Lab 3.0 正式 |
| **[Isaac Sim 6.0](https://docs.isaacsim.omniverse.nvidia.com/latest/index.html)** | 🟡 Preview | ✨ **注目**: Newton 統合を含む次世代の構造刷新 — 現行 5.x スタックの移行方向の指標<br>⏳ **待機**: 「Early Developer Release」、API 変動（最新 GA は 5.1） | 6.x GA 宣言 |
| **[Cosmos 3](https://www.nvidia.com/en-us/ai/cosmos/) を sim-to-real 学習源として** | 🟢 GA（モデル）/🔵（実戦） | ✨ **注目**: ワールドモデル生成データで実デプロイ可能なポリシーを学習する軸 — 成立すれば SDG パイプラインの勢力図が変わる<br>⏳ **待機**: モデルは GA だが「ワールドモデルのデータで実デプロイ可能なポリシーを学習」はアーリーアダプターのみ。⚠️ **AWS 未ホスティング** | AWS マッピング強化 + 学習検証 |

## 🤖 ハードウェア / デプロイ（ロードマップ・デモ）

| 項目 | ラベル | 要点 | 昇格条件 |
|---|---|---|---|
| **Tesla Optimus V3** | ⚪ Hype | ✨ **注目**: 最大の話題性を持つヒューマノイド量産計画 — 顧客からの質問頻度が最も高い項目<br>⏳ **待機**: Musk の主張のみ、生産未開始 | 検証されたデプロイ |
| **Hyundai·BD オールエレクトリック [Atlas](https://bostondynamics.com/atlas/)** | ⚪ ロードマップ | ✨ **注目**: 現代自動車グループの量産ロードマップ（2028 から 3 万台/年）— 韓国の顧客接点で最も直接的なヒューマノイドトラック<br>⏳ **待機**: オールエレクトリック Atlas 製品版を公開（2026-07、BD 公式 `[3]`）。展開 2.5 万+台・生産能力 3 万/年はいずれも **2028 開始**、現在の実稼働 ~0。2026 は小規模パイロットのみ（現代 RMAC + Google DeepMind）。⚠️「第 5 世代」は誤称 | 実稼働出荷の開始 |
| **[Apptronik Apollo 2 + Robot Park](https://apptronik.com/)** | 🟡 パイロット | ✨ **注目**: Mercedes・GXO の実運用パイロット + Google DeepMind データ提携 — ヒューマノイド商用化最前線の指標<br>⏳ **待機**: Mercedes-Benz・GXO で運用パイロット `[3]` + Google DeepMind Gemini Robotics データ提携（9 万平方フィート）。自律・商用拡大は未検証。AWS マッピングは一般的（データ→S3/SageMaker）、提携自体は Google `[4]` | 商用デプロイ規模 + 自律成果の検証 |
| **[1X Neo](https://www.1x.tech/neo)** 自律性 | 🟡 Preview | ✨ **注目**: 家庭用ヒューマノイドを実際に販売（$20k）する初の事例群 — 遠隔操作混合運用モデルの試金石<br>⏳ **待機**: 自律 + VR 遠隔操作（Expert Mode）の混合運用 — CEO 自身が認めている（[Engadget](https://www.engadget.com/ai/1x-neo-is-a-20000-home-robot-that-will-learn-chores-via-teleoperation-040252200.html) `[3]`）。「自律 60~70%」という数字は一次ソースなし `[4]` | 真の自律性の検証 |
| **[Figure 03](https://www.figure.ai/)「8 時間自律シフト」** | ⚪ Hype | ✨ **注目**: 検証済み BMW パイロットの実績の上での自律性主張 — 事実なら産業ヒューマノイド自律性の基準を塗り替える<br>⏳ **待機**: CEO のツイート、独立検証なし（Figure 02@BMW は検証済みパイロット） | 第三者による自律性監査 |
| **[Cosmos 3](https://www.nvidia.com/en-us/ai/cosmos/) 採用**（Doosan/LG/Samsung） | 🟢 GA（発表） | ✨ **注目**: 韓国大手 3 社の採用発表 — 韓国の顧客対話で即座に挙がるリファレンス<br>⏳ **待機**: 採用は「発表」であって本番検証ではない | 本番事例の公開 |

## 🔗 エージェント / 接続（初期）

| 項目 | ラベル | 要点 | 昇格条件 |
|---|---|---|---|
| **MCP[^mcp] for robotics**（[ros-mcp-server](https://github.com/lpigeon/ros-mcp-server) など） | 🔵 Research | ✨ **注目**: エージェント標準プロトコルをロボットスキルへつなぐ実験が急増（50+ サーバー）— AgentCore 連携の切り口<br>⏳ **待機**: 50+ サーバーがあるがオープンソース/デモ、本番なし（安全性・遅延・決定性が未検証） | 本番ハードニング事例 |
| **ROS 2[^ros] + LLM エージェント[^agent]**（NASA JPL [ROSA](https://github.com/nasa-jpl/rosa), [RAI](https://github.com/RobotecAI/rai)） | 🔵 Research | ✨ **注目**: NASA JPL ROSA など実組織での検証事例を保有 — 自然言語→ロボット運用の最も現実的な入り口<br>⏳ **待機**: ROSA(JPL) が最強の実例だが mock-ops。現場デプロイは限定的 | 現場での本番デプロイ |
| **エージェント物理安全標準**（[RoboGuard](https://arxiv.org/abs/2503.07885) など） | 🔵 Research | ✨ **注目**: LLM の意味レベルのリスクを扱う標準の空白地帯 — 規制・調達要件として浮上する可能性<br>⏳ **待機**: ISO は物理のみ、LLM の意味的リスク標準が不在 | 標準化の進展 |
| **[AgentCore Payments / Agent Registry](https://aws.amazon.com/bedrock/agentcore/)（ソウル）** | 🟡 Preview/未提供 | ✨ **注目**: ロボットエージェントの商取引・レジストリ基盤の AWS ネイティブ軸 — ソウルリージョン開放後は即提案可能<br>⏳ **待機**: ソウルリージョン未提供 — Agent Registry は東京 ✅、Payments は東京にも未提供（APAC はシドニーのみ）`[1]` | ソウルリージョン拡張 |

## 🆕 最新スキャン流入（2026-10-09 · リンク・一次ソース照合 2026-09-27）

<!-- 自動スキャン（arXiv/ウェブ）の流入分。2026-09-27 に全リンクの生存確認（20/20 HTTP 200）+ 10 件を一次ソース原文と照合 —— 昇格 0 件、訂正 6 件（RLDX ベンチマーク差 +11.1pt、KIMM リンク差し替え、OpenAI リンク差し替え・引用を二次表記、Skild 自社ベンチ公開の反映、Figure Index 数値の出典分離、NEURA IFA 実機展示の削除）。等級は流入方針どおり [4]（自社公表・独立検証なし）を維持。THE FILTER を通過するまで顧客提案での使用禁止。定期更新は scripts/radar_scan.md を参照。 -->

| 項目 | ラベル | 要点 | 昇格条件 |
|---|---|---|---|
| **[NEURA Robotics 4NE1 / Neuraverse × AWS](https://press.aboutamazon.com/aws/2026/4/neura-robotics-and-aws-enter-strategic-collaboration-to-accelerate-physical-ai-at-scale)**（ドイツのフルスタックロボティクス、AWS と戦略的協業） | ⚪ ロードマップ | ✨ **注目**：AWS が Neuraverse の主要クラウドプロバイダーとしてプラットフォームをホストし、NEURA Gym の学習パイプラインを SageMaker と統合、NEURA は AWS パートナーネットワーク（APN）で GTM を拡大 —— サービス名が明記された AWS パートナーシップで、Radar 内の欧州ヒューマノイドトラック<br>⏳ **待機**：AWS・NEURA 公式発表（2026-04-21、press.aboutamazon.com）`[4]` —— Amazon フルフィルメントセンターへの配備は原文では「explore opportunities」（検討）にとどまり、実配備ではない。[最大 14 億ドルのシリーズ C](https://neura-robotics.com/record-series-c/)（2026-06-10、Amazon・NVIDIA・Tether などが参加、自社表現「フルスタックロボティクス史上最大」）+ [IFA 2026 ベルリン基調講演](https://www.ifa-berlin.com/press-releases/ifa-2026-neura)（2026-09-05）で話題更新、第三者検証なし。🔗 リンク 200 · 一次ソース照合 2026-09-27。**AWS 角度：公式協業（SageMaker・APN 明記）** | Amazon フルフィルメントセンター等の実配備事例公開 + 独立した性能検証 |
| **[RLWRLD RLDX-1](https://arxiv.org/abs/2605.03269)**（81 億パラメータのデクスタリティ[^dext]基盤モデル、AWS 上で学習） | 🔵 Research | ✨ **注目**：KAIST 出身のソウル発スタートアップのオープンなロボティクス基盤モデルを [AWS Physical AI ブログ](https://aws.amazon.com/blogs/physical-ai/putting-dexterous-robots-to-work-how-rlwrld-builds-physical-ai-with-aws/)（2026-06-22）が直接紹介 —— EC2 p5e/p5en（H200）・ParallelCluster・FSx for Lustre で学習、五指ハンドの精密マニピュレーション特化、コード・重みを [GitHub で公開](https://github.com/RLWRLD/RLDX-1)（CC BY 4.0）—— NEURA とともに Radar 内の AWS 公式協業事例であり、韓国発トラック<br>⏳ **待機**：arXiv 技術レポート（2026-05-05）+ AWS ブログ `[4]` —— シミュレーションベンチ 6 種・実機 3 プラットフォームの自社測定値（GR-1 Tabletop 58.7 vs GR00T N1.6 47.6 = +11.1pt、表 1(b)；ALLEX 実機 86.8% vs π0.5・GR00T N1.6 約 40%；SIMPLER 81.5% は AWS ブログの引用）、独立再現・査読なし —— **自社公表値、顧客への引用禁止**。AWS との関係は学習インフラ + Generative AI Accelerator 参加（2025-10）の段階で、実配備はロッテホテル＆リゾートで 2030 年目標（安全検証が条件）。🔗 リンク 200 · 一次ソース照合 2026-09-27。**AWS 角度：AWS ブログ事例（EC2・ParallelCluster・FSx）· 🇰🇷 韓国接点** | 独立ベンチマーク再現 + 実配備事例の公開 |
| **[Figure Index → Helix 2.5](https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization)**（クラウドソーシングした人間動画データで事前学習したヒューマノイド用ニューラルネット、未学習の家庭 30 軒でゼロショット検証） | 🟡 Preview | ✨ **注目**：Figure がクラウドソーシングデータ（Index）で事前学習した単一ポリシーを、データ収集・ファインチューニングなしでベイエリアの実際の家庭 30 軒（すべて未学習）に配備し、リビングの片付け・タオル折り・ベッドメイキングの 3 タスクを実行 —— Index 事前学習のみでゼロショットのタスク全体成功率が 9%→56% に上がったと発表、クラウドソーシングデータパイプラインが実際のポリシー性能につながるという初の定量的主張<br>⏳ **待機**：Figure 公式発表（2026-09-17、figure.ai）`[4]` —— 9%→56% は Figure 社内のブラインド評価による**自社測定値、顧客への引用禁止**（420 回中 237 回は二次メディアの記載で、原文ページのテキストでは未確認；Index 報酬 1,500 万ドルは [Index 発表](https://www.figure.ai/news/introducing-index)（2026-08-25）が出典）、独立再現・第三者検証なし。🔗 リンク 200 · 一次ソース照合 2026-09-27。**AWS 角度：なし** | 独立再現・第三者ベンチマーク検証 + 家庭・タスク拡大の実証 |
| **[KIMM カイロス（KAIROS）V0.7](https://www.kimm.re.kr/sub0504/view/id/21372)**（K-Moonshot 国家戦略技術課題の韓国産 AI ヒューマノイド） | ⚪ ロードマップ | ✨ **注目**：韓国機械研究院（KIMM）が科学技術情報通信部支援の「AI ヒューマノイド・グローバルトップ研究団」として開発中の国家プロジェクトのヒューマノイド —— 2026-09-07 の「2026 グローバル機械技術フォーラム」で V0.7 を公開、タルチュム（仮面舞）・国民体操などの全身動作を実演（4 月の創立 50 周年で初公開された V0.5 は握手・手振り程度）—— 韓国の顧客対話で出てくる可能性のある「国立研究機関発」ヒューマノイドトラック<br>⏳ **待機**：KIMM 公式ニュース（2026-09-07）`[4]` —— 実演は自社デモで、自律性能の数値なし。V1.0 公開 2027-04 目標・追加開発費約 30 億ウォンは KIMM 原文にはなく、[イーデイリー](https://www.edaily.co.kr/News/Read?newsId=03883526645577824)・[ニュースピム](https://www.newspim.com/news/view/20260907001070)の報道（二次）。商用化・自律性能は皆無、デモ段階。🔗 リンク 200（従来の 4 月プレスリリースのリンクを 09-07 公式ニュースに差し替え）· 一次ソース照合 2026-09-27。**AWS 角度：なし · 🇰🇷 韓国接点** | V1.0 公開 + 自動車組立・家庭用の実証事例公開 |
| **[XPENG IRON](https://www.xpeng.com/news/01a080371029a057bc8e8a02a2c6012b)**（中国 EV メーカー XPENG のヒューマノイド、自動車級量産ラインから初の完成ロボットが自力歩行） | ⚪ ロードマップ | ✨ **注目**：完成車メーカーが自社 EV 生産ノウハウ（コア工程の自動化 80%+）をそのままヒューマノイド量産ラインに移植 —— 完成したロボットがラインから自力で歩き出す様子を公開（全身 76 自由度、各手 21 自由度）—— 韓国の顧客対話における「中国 EV 発ヒューマノイド」競合トラック<br>⏳ **待機**：XPENG 公式発表（2026-09-08、xpeng.com）`[4]` —— 原文では「量産開始」は 2026 年末の目標で、初期の商用投入は自社店舗・キャンパス、中国・海外での正式発売・納入は 2027 年。自由度・自動化率は自社公表で、独立した性能・安全検証なし。🔗 リンク 200 · 一次ソース照合 2026-09-27。**AWS 角度：なし** | 実際の量産出荷開始 + 第三者による安全・性能検証 |
| **[Skild AI S1](https://skild.ai/blogs/s1)**（人間の実演動画 1 本だけでファインチューニングなしに最長 10 分の長期タスクを実行するインコンテキスト学習型ロボット基盤モデル） | 🟡 Preview | ✨ **注目**：人間の実演動画 1 本を「ビジュアルプロンプト」として受け取り、ファインチューニング・重み変更なしで最長 10 分・数十ステップの未学習長期タスクを実行 —— [NVIDIA 公式ブログ](https://blogs.nvidia.com/blog/skild-ai-s1-physical-ai/)（2026-09-10）が Skild・NVIDIA・Foxconn による NVIDIA Blackwell システム組立ライン（バスバー・リミットブロック取付、ネジ 16 本締結）への配備と「60 件超の配備パートナーシップ」を紹介 —— 「少数パートナーへの配備」宣言段階から産業売上段階へ移行したとする初期事例<br>⏳ **待機**：NVIDIA・Skild AI 公式発表（2026-09-10）`[4]` —— [Skild 自社記事](https://www.skild.ai/blogs/skild-crosses-100m-arr)の ARR 1 億ドル（初の商用配備から 10 か月）・認識売上 5,000 万ドル・有償顧客 60 社超、S1 ブログ（2026-08）の既知タスク 96%・未知タスク 66% の成功率はいずれも**自社公表値、顧客への引用禁止**（第三者監査・独立検証なし）。AWS マッピング・ソウルリージョン連携事例なし。🔗 リンク 200 · 一次ソース照合 2026-09-27。**AWS 角度：なし（NVIDIA スタック）** | 独立した性能・売上検証（第三者監査）+ AWS マッピング事例の公開 |
| **[Intrinsic Core](https://www.intrinsic.ai/blog/posts/introducing-intrinsic-core)**（Alphabet のロボティクス子会社 Intrinsic が産業用ロボティクススタックをオープンソース化 —— リアルタイム制御・NVIDIA FoundationPose ベースの姿勢推定・モーション/グラスプ計画・Gazebo ベースのシミュレーション・カメラキャリブレーション・ROS 互換ドライバー） | 🟢 GA（オープンソース） | ✨ **注目**：Intrinsic が自社の製造配備で実際に使うものと同じスタックを ROSCon 2026（トロント）で Apache 2.0 として丸ごと公開（[GitHub](https://github.com/intrinsic-ai/intrinsic-core)）—— Isaac エコシステム一強の構図に Alphabet 発の代替スタックが初めて登場、Radar 🖥️ シミュレーション/ツール軸（Isaac/MuJoCo/Newton）に競合観察対象を追加<br>⏳ **待機**：Intrinsic 公式ブログ（2026-09-22）`[4]` —— コードは公開されたが、Intrinsic 外部の独立採用事例（原文は FANUC・UR 互換とチャレンジ参加者数のみ言及）・AWS マッピング事例なし。🔗 リンク 200 · 一次ソース照合 2026-09-27。**AWS 角度：なし（競合スタック）** | 外部の独立採用事例の公開 + AWS インフラマッピングの検証 |
| **[Agility Robotics Digit 5](https://www.agilityrobotics.com/content/agility-unveils-digit-5-humanoid-robot-built-for-cooperatively-safe-work-at-scale)**（既存の Digit@GXO に対し、近接協働の安全アーキテクチャと 90 分駆動バッテリーを備えた第 5 世代汎用ヒューマノイド） | 🟡 Preview | ✨ **注目**：pillar-4 で「最もよく検証された有償ヒューマノイド」としてすでに掲載されている Agility Digit（@GXO）の次世代モデル —— 衝突リスク検知時に回避・停止・着座し、視聴覚信号で人との近接作業を可能にする安全設計、90 分駆動・9 分充電、CE マーキングで EU・英国へ参入する計画を発表<br>⏳ **待機**：Agility 公式発表（2026-09-15、agilityrobotics.com）`[4]` —— 3 億ドル超の複数年受注は「2026-05 時点、契約マイルストーン達成が条件」で、Digit 5 の実稼働は 0（既存の 65,000 時間超の実績は Digit 4）。アーリーアクセスは 2027 年上半期、製造・倉庫顧客向け GA は 2027 年末予定。🔗 リンク 200 · 一次ソース照合 2026-09-27。**AWS 角度：なし** | Digit 5 実稼働顧客事例の公開（EU/北米）+ 安全アーキテクチャの第三者検証 |
| **[Dyna Robotics DYNA-2 / DYNA 2.1](https://www.prnewswire.com/news-releases/dyna-robotics-launches-dyna-2-1-physical-agent-a-semi-humanoid-robot-that-completes-full-workflows-such-as-a-commercial-laundry-shift-302892411.html)**（ロボット実機データを使わず、エゴセントリックな人間動画 100 万時間超のみで事前学習したワールド-アクションモデルに加え、クリーニング・ホテルハウスキーピング・フードサービスなどのフルワークフローを実際に遂行するセミヒューマノイド physical agent の実配備） | 🟡 Preview | ✨ **注目**：ロボット実機データを使わず人間の一人称視点動画のみで事前学習したワールド-アクションモデル（DYNA-2）を、少量のロボットデータでのファインチューニングだけでホテル・レストラン・クリーニング店に実配備されたセミヒューマノイド（DYNA 2.1）へとつなげた —— 「人間データ→ロボットのスケーリング則」という主張で、Radar 🔬 World-action models 軸にデータパイプラインの視点（ロボットフリーの事前学習）を加える事例<br>⏳ **待機**：Dyna Robotics 公式発表（PR Newswire、DYNA-2 訂正版 2026-08-10・DYNA 2.1 2026-09-29）`[4]` —— 成功率 20%→80~90%、DYNA-1 比 1.55 倍、顧客現場 87% vs 46% はいずれも**自社公表値、顧客への引用禁止**で、独立検証・査読なし。モデル重み・API は非公開（自社運用のハードウェア経由のみでアクセス可能）。⚠️ 今回の実行環境の egress 制限により prnewswire.com の curl 200 手動検証は未実施（コミットメッセージ・issue 参照）。**AWS 角度：なし（2025-09 のシリーズ A に Amazon Industrial Innovation Fund が投資家として参加したのみで、インフラパートナーシップではない）** | 独立した性能検証（第三者監査）+ 実配備顧客事例の公開拡大 |
| **[Magic-W0](https://arxiv.org/abs/2609.39870)**（Magiclab Robotics、3D 幾何・モーション・未来セマンティクスで構造化したワールド表現と行動生成を双方向に結合したワールド-アクション基盤モデル） | 🔵 Research | ✨ **注目**：エゴセントリックな人間操作動画・実ロボット軌跡・シミュレーションデータで大規模に事前学習し、RoboDojo-Sim ベンチマークで 1 位と自社主張 —— Radar 🔬 World-action models 軸（DreamZero→GR00T N2）にコード公開（GitHub）を伴う中国ロボティクススタートアップの実装事例を追加<br>⏳ **待機**：arXiv プレプリント（2026-09-30 投稿・v2 2026-10-03）`[4]` —— RoboDojo-Sim・LIBERO の自社ベンチマークと自社実機テストが中心で、査読・独立再現なし。コードは公開（MagiclabRobotics/Magic-W0）だが、学習済み重みの公開状況は不明。⚠️ 今回の実行環境の egress 制限により arxiv.org・github.com の curl 200 手動検証は未実施（コミットメッセージ・issue 参照）。**AWS 角度：なし** | 査読 + 独立再現 + 実機配備事例 |

## 終了・受付制限 — 状態別確認 { #-廃止済み--提案禁止記録保存用 }

| 項目 | 状態 | 代替 |
|---|---|---|
| **[AWS IoT FleetWise](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/what-is-iotfleetwise.html)** | 新規受付停止、既存顧客は継続可 `[1]` | 新規の既定構成から除外 — [根拠](evidence.md#fleetwise-new-customers) |
| **[AWS RoboMaker](https://aws.amazon.com/robomaker/)** | 🔴 終了 (2025-09-10) `[1]` | EC2 G6e/G7e + Isaac Sim AMI + AWS Batch |
| **[SageMaker Edge Manager](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-eol.html)** | 🔴 終了 (2024-04-26) `[1]` | ONNX + IoT Greengrass V2 (+ SageMaker Neo) |
| **[IoT Greengrass V1](https://docs.aws.amazon.com/greengrass/v1/developerguide/what-is-gg.html)** | 🔴 終了 (2026-06-01) `[1]` | Greengrass V2 |
| **[Gazebo Classic 11](https://classic.gazebosim.org/)** | 🔴 EOL (2025-01) `[1]` | Gazebo Jetty/Harmonic |
| **Trainium for VLA** | ⚪ 公開事例なし `[4]` | 現在は CUDA/NVIDIA（提案時にリスクを明示） |

> ⚠️ **噂への警戒（事実ではない）**: 「AWS IoT TwinMaker 廃止」は**誤情報** — TwinMaker は GA・新規顧客に開放（低速度）。SiteWise のメンテナンスと混同した第三者ブログの主張です。繰り返さないでください。→ [pillar-3](pillar-3.md)。

---

## 昇格手順（要約）

1. **キャプチャ**: 指定チャンネル/絵文字で候補を収集
2. **確認**：[掲載条件](maintenance.md#掲載基準-the-filter)を全て満たし、発売・根拠・用途・支援を分けます。
3. **通過時**: 担当ピラーの owner が[標準テンプレート](maintenance.md#標準テンプレート)で編入し、Radar から削除
4. **未達時**: ここに一行で保持し、昇格条件を明示

パイプライン全体 → [maintenance](maintenance.md#playbook-昇格パイプライン)。

---
_owner: Youngjin · updated: 2026-09 · volatility: 高（Radar は本質的に急速に変化します — 月次レビューを推奨）_

<!-- 용어 각주 -->

[^wfm]: **ワールド基盤モデル（WFM, World Foundation Model）** — 物理世界の次のシーンを予測・生成するよう学習された大型モデルです。テキスト・映像プロンプトから物理的にもっともらしい映像・シナリオを作り、ロボット学習データを拡張します。🎥 [NVIDIA Cosmos 紹介](https://www.youtube.com/watch?v=9Uch931cDx8)
[^sysid]: **システム同定（SysID, System Identification）** — 実機ロボットの物理パラメータ（摩擦・質量・モーター応答）を測定し、シミュレーターを実物に合わせて校正する作業です。
[^s2r]: **sim-to-real** — シミュレーションで学習したポリシーを実際のロボットへ移すこと、またはその方法論です。シミュレーションと現実の物理・視覚の差（ドメインギャップ）のため、そのまま移すと性能が崩れます。🎥 [NVIDIA sim-to-real ロボティクスショーケース](https://www.youtube.com/watch?v=sffNvv3GkRA)
[^physeng]: **物理エンジン（physics engine）** — 剛体動力学・接触・摩擦・衝突を数値的に計算するシミュレーターの中核ソフトウェアです。エンジンの精度・速度のトレードオフがシミュレーター選択（Isaac/MuJoCo/Genesis）を左右します。
[^mcp]: **MCP（Model Context Protocol）** — エージェントとツール・データソースをつなぐオープン標準プロトコルです。「エージェント用 USB-C」に例えられ、ロボットスキルを MCP サーバーとして公開する実験が増えています。
[^ros]: **ROS 2 (Robot Operating System 2)** — ロボットソフトウェアの事実上の標準オープンソースミドルウェアです。センサー・制御ノードがトピック（topic）で通信する分散構造で、産業・研究ロボットスタックの共通基盤です。
[^agent]: **LLM エージェント** — 大規模言語モデルが自ら計画を立て、ツール（API・ロボットスキル）を選んで呼び出し、多段階のタスクを遂行するソフトウェアです。単純な質疑応答と異なり「行動」がある点が核心です。
[^dext]: **デクステリティ（dexterity）** — ロボットの手・アームが人の手のように精緻かつ器用に物体を扱う能力です。単純なグリッパーの把持・配置とは異なり、5 指ハンドで物体を回転させたり道具を操作したりするなど、接触の多い複雑な操作を指します。
