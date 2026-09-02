---
ko_hash: 371ad88d76913058c1523fee9960ea663d997d9a
---
# Radar — キュー / ウォッチリスト


_最終更新: 2026-08 · owner: Youngjin · volatility: 高_
[← index へ](index.md)

> **L0 TL;DR**: 包含基準（[2.5 THE FILTER](maintenance.md#包含基準-the-filter)）はまだ通過していないものの、**注目すべきもの**。各項目は一行 — 成熟度ラベル + **なぜ注目か + なぜ待機中か**。ゲート（4 項目中 2 項目）を通過すると、担当ピラーの owner が標準テンプレートで昇格します。
>
> ⚠️ **ここにある項目を顧客提案で「成熟した能力」のように扱わないでください。** 華やかなデモがデプロイ可能性を覆い隠すことがよくあります。

---

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

## 🆕 最新スキャン流入（2026-09-02 · 一次検証完了 2026-07-21）

<!-- 自動スキャン（arXiv/ウェブ）の流入分。2026-07-21 に一次ソース検証完了（検証エージェント 4 式、公式発表・arXiv 原文と照合）—— 昇格 0 件、訂正 6 件。THE FILTER を通過するまで顧客提案での使用禁止。定期更新は scripts/radar_scan.md を参照。 -->

| 項目 | ラベル | 要点 | 昇格条件 |
|---|---|---|---|
| **[Walden Robotics](https://www.waldenrobotics.com/news/walden-robotics-launches-from-stealth)**（Toyota Research Institute からのスピンアウト、Large Behavior Models[^lbm] ヒューマノイド） | 🟡 パイロット | ✨ **注目**: TRI ロボティクスを率いた Russ Tedrake のスピンアウト + シード 3 億ドル — LBM 商用化の最前線、Toyota 工場での実パイロットを保有<br>⏳ **待機**: 公式発表（2026-07-15）`[4]` —— 2026-01 に TRI からスピンアウト（創業者 Russ Tedrake、元 TRI SVP）、Toyota・Deviation Capital 共同リード + NVIDIA・Boeing・Samsung Ventures などが参加したシード 3 億ドル（バリュエーション 11 億ドル）。ヒューマノイド上半身+ホイール式移動ベース、Diffusion Policy[^diffpol]・Large Behavior Models ベースの方策で、北米 Toyota 工場にて 2026-02 からパイロット→「本番転換」を自社主張、第三者検証なし | 第三者監査・独立検証 + 展開規模拡大の事例 |
| **[Xiaomi-Robotics-1](https://github.com/XiaomiRobotics/Xiaomi-Robotics-1)**（VLA[^vla] ファウンデーションモデル、10 万時間超の実世界 UMI[^umi] 軌跡） | 🔵 Research | ✨ **注目**: UMI 10 万時間超の実世界軌跡というデータスケールで 4 ベンチマークの SOTA を主張 — 中国ビッグテックが VLA 競争へ本格参入するシグナル<br>⏳ **待機**: Xiaomi 公式 arXiv 発表（2607.15330、2026-07-16）`[4]` —— Qwen3-VL ベースの MoT（VLM+DiT）、RoboCasa365（57.4%、従来 SOTA 46.6% から向上）など 4 ベンチマークで自己申告 SOTA（RLDX-1・GR00T N1.6 などと比較、独立再現なし）。⚠️ **訂正（2026-08-10）**: 2026-08-03 に GitHub でコード・チェックポイント（ベース 5B + RoboCasa/RoboCasa365/VLABench タスク別 3 種）の実公開を確認 — **Apache-2.0**（RLDX-1 と異なり商用利用を明示的に許可、AWS マッピングの可能性あり）。リポジトリ自身のリーダーボード数値は arXiv 論文と表記方式が異なり直接対照が必要、独立再現・実導入は依然ゼロ | 独立ベンチマーク再現 + 実導入事例 |
| **[Gemini Robotics 2](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/)**（Google DeepMind、全身制御 VLA） | 🟡 Preview | ✨ **注目**: フロンティアラボの VLA が上半身マニピュレーションを超えて全身（歩行・両手協調）制御へ拡張 — 競合スタックの地形を変える世代転換のシグナル<br>⏳ **待機**: 公式発表（2026-07-30）`[4]` —— これまでの上半身のみの制御を全身制御（歩行・屈曲・両手協調）に拡張、推論モデル Gemini Robotics ER 2・エッジモデル On-Device 2 を同時発表。Apptronik Apollo 2 で実機デモ（電球の取り外し 92% 成功）、自己申告ベンチマークで独立検証なし。公開プレビューは ER 2 のみ（AI Studio/Enterprise Agent Platform）、VLA・On-Device 2 はアーリーアクセスパートナー限定。⚠️ [pillar-2](pillar-2.md) の「Gemini Robotics」競合スタック節は本発表以前のスナップショット（確認 2026-07、ER 1.6/On-Device/1.5 が対象）—— pillar owner による更新が必要 | アーリーアクセス終了・GA 公開 + 独立ベンチマーク検証 |
| **[Xiaomi-Robotics-U0](https://arxiv.org/abs/2607.11643)**（統合埋め込み型データ合成ワールドファウンデーションモデル、38B） | 🔵 Research | ✨ **注目**: text-to-image・シーン合成・動画生成・「embodied transfer」を単一のオートレグレッシブフレームワークに統合し、ロボット学習用の合成データを直接生成 — WorldArena ベンチマークで 100 以上のモデル中総合 1 位を自己申告、実機の π0.5 ポリシーに拡張データを適用し held-out（背景・照明変更）条件でのタスク完了率を 36.9%→63.2% に改善したことまで実測<br>⏳ **待機**: Xiaomi 公式 arXiv 発表（2607.11643、2026-07-13）`[4]` —— ベンチマーク・実機結果ともに自己申告で、独立再現・peer-review なし。⚠️ **訂正（2026-08-18）**: GitHub（`XiaomiRobotics/Xiaomi-Robotics-U0`）でコード・チェックポイントが実際に公開されていることを確認 —— **Apache-2.0**、2026-07 公開（Scene Gen/Transfer/T2I/X2I 対応、Video チェックポイントは未公開）—— 以前の「公開状況は不明」という記載を訂正。π0.5（Physical Intelligence が独立に公開したモデル）の完了率改善は U0 のデータを消費した下流の結果であり、U0 自体の独立再現ではない。同表の既存項目 Xiaomi-Robotics-1（VLA ポリシーモデル）とは別モデル・別事案（本件はデータ合成用 WFM） | peer-review + 独立再現 |
| **[ω-0](https://arxiv.org/abs/2608.06375)**（移動+操作を同時制御するワールド-アクションモデル） | 🔵 Research | ✨ **注目**: 移動・姿勢調整・バランス・操作を分離せず単一モデルで同時実行（concurrent loco-manipulation）—— diffusion[^diffpol] ベースの whole-body アクションを生成し、実機（Unitree G1）で 11 の家庭タスクを自律実行、人の動作データの転移（human-to-humanoid）まで実証<br>⏳ **待機**: arXiv 2608.06375（2026-08-06、NTU・北京大学・BAAI など）`[4]` —— 自己申告ベンチマークで既存の模倣学習・VLA・ヒューマノイド・WAM ベースラインに優位と主張、独立再現・peer-review なし。40 時間規模の ω-HOME データセットの公開状況は不明 | peer-review + 独立再現 + データセット・コード公開の確認 |
| **[XYZ Robotics DEUX](https://zdnet.co.kr/view/?no=20260727093315)**（BrainX・GloveX・TwinX をつなぐ「Physical AI Data Flywheel」を基盤とした双腕セミヒューマノイド） | 🟡 Preview | ✨ **注目**: 韓国のスタートアップが自社カフェ・配送ロボットの商用運用（バリスタロボットは 100 万件超の注文を処理）から得られる実データで BrainX を学習し、テレオペレーション収集デバイス GloveX → デジタルツイン TwinX での検証 → 実機への再展開までをつなぐ自社データフライホイール構造 —— 韓国の顧客接点で直接挙がりうるローカルな Physical AI データパイプライン事例<br>⏳ **待機**: ソウル・ラウンジエックス聖水本店で実証を開始（2026-07-27）`[4]` —— 双腕 32DoF + 3 指ハンド、シリーズ B 130 億ウォンを調達（2026-03）。DEUX の商用ローンチ（2026 年下半期予定）・GloveX の外部販売（2026 年末予定）はいずれも未リリース。自律性能・展開規模は未検証 | 実証拡大 + 自律性能の独立検証 |
| **[ROBOTIS AI Sapiens K1](https://github.com/ROBOTIS-GIT/ai_sapiens)**（DYNAMIXEL-Q ベースのオープンソースヒューマノイドプラットフォーム） | 🟡 Preview | ✨ **注目**: 韓国企業 ROBOTIS のオープンソースヒューマノイド —— スマートフォン映像だけでK-popの振り付けを学習(映像モーションキャプチャ→リターゲティング→シミュレーション RL→sim-to-real)して実演、NVIDIA Kimodo によるテキスト→モーション生成の拡張も統合。韓国の顧客接点で直接挙がりうるローカルなオープンヒューマノイド事例<br>⏳ **待機**: GitHub 公式リポジトリ（`ROBOTIS-GIT/ai_sapiens`、Apache-2.0）`[4]` —— ROS 2 パッケージ（ロボット記述・コントローラーインターフェース・sim2real ツール）は既に公開済みだが、映像→モーション生成の全パイプラインのオープンソース化は ROBOTIS 自身の予告計画のみ（日程未確定）。K-pop 実演は自己申告、独立検証・実導入事例なし | 全パイプライン公開の確認 + 独立検証 |
| **[AWS-NVIDIA Physical AI インフラ拡大](https://press.aboutamazon.com/aws/2026/8/aws-and-nvidia-to-deliver-2-million-additional-gpus-and-next-generation-infrastructure-for-agentic-and-physical-ai)**（Amazon Robotics × NVIDIA 協業） | ⚪ ロードマップ | ✨ **注目**: AWS 自身が物理 AI インフラ（シミュレーション・SDG[^sdg]・ロボット訓練・機能安全・real-to-sim 検証、GPU アクセラレーテッド EC2）を Amazon Robotics の次世代ロボット開発に投入すると公式発表 — Radar 史上最も直接的な「AWS 自社」物理 AI 事例<br>⏳ **待機**: 2026-08-26 AWS・NVIDIA 共同発表 `[4]`（一次ソース press.aboutamazon.com/nvidianews.nvidia.com、多数の二次媒体で交差確認）—— NVIDIA GPU 200 万台追加導入（2027~2028）の一部。Jetson・Omniverse・Isaac プラットフォームの活用範囲のみ公開、Amazon Robotics の具体的なロボット・定量的成果・サービス名は未公開 — ロードマップ段階、実デプロイ 0 | 具体的なロボット/サービスの公開 + AWS サービスマッピングの確定 |
| **[LG × NVIDIA 二足歩行ヒューマノイド + CLOiD](https://www.prnewswire.com/news-releases/lg-to-unveil-its-next-gen-humanoid-robot-built-on-nvidia-isaac-gr00t-302851652.html)** | ⚪ ロードマップ | ✨ **注目**: 韓国の大手企業（LG）が NVIDIA と MOU を締結 — Jetson Thor・Isaac GR00T・Halos（ロボティクス安全フレームワーク）ベースの二足歩行ヒューマノイドを 2027 年第 1 四半期に公開予定、加えてホイール式 CLOiD をテネシー州の洗濯機工場に 2026 年内に実戦検証投入 — 韓国の顧客対話で直接引用できるローカル大手企業のトラック（現代・BD Atlas と似た角度）<br>⏳ **待機**: 2026-08-13 MOU 締結を公式発表（LG Corp 具光謨会長と Jensen Huang が出席）`[4]`。CLOiD のテネシー投入は 2026 年内だが検証段階（商用規模ではない）、二足歩行ヒューマノイドは試作機未公開（2027-Q1 公開予定）— 現在の実稼働は 0 | 二足歩行ヒューマノイド実機公開 + CLOiD 工場検証結果の公開 |
| **[GHOST](https://arxiv.org/abs/2608.29080)**（オンボードカメラのみで 1 人が 2 台のロボットを同時遠隔操作する VR テレオペレーション） | 🔵 Research | ✨ **注目**: Brown University（Tellex lab）が Amazon の資金支援を受けて開発 — 外部モーションキャプチャなしでオンボード RGB-D のみを使い、1 人のオペレーターが Boston Dynamics Spot 2 台を VR で同時遠隔操作、IEEE RA-L に掲載(peer-review 通過)。初心者の成功率 1.6~4 倍、エキスパートの作業速度 1.47 倍向上を実測 — テレオペレーションによるロボットデータ収集パイプラインのコストを下げうるオープンソース事例<br>⏳ **待機**: arXiv 2608.29080（2026-08-29、IEEE RA-L 2026-08 accept）`[4]` — エキスパート評価者は論文著者本人 3 名（バイアスの可能性）、初心者評価は n=15（9 タスク中 2 タスクのみ実施）、Boston Dynamics Spot 専用ハードウェア・専用 Wi-Fi 環境（本番環境での信頼性は未検証） | 独立ユーザー評価の拡大 + 多様なハードウェア・ネットワーク環境での検証 |

## ⚰️ 廃止済み — 提案禁止（記録保存用）

| 項目 | 状態 | 代替 |
|---|---|---|
| **[AWS RoboMaker](https://aws.amazon.com/robomaker/)** | 🔴 終了 (2025-09-10) `[1]` | EC2 G6e/G7e + Isaac Sim AMI + AWS Batch |
| **[SageMaker Edge Manager](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-eol.html)** | 🔴 終了 (2024-04-26) `[1]` | ONNX + IoT Greengrass V2 (+ SageMaker Neo) |
| **[IoT Greengrass V1](https://docs.aws.amazon.com/greengrass/v1/developerguide/what-is-gg.html)** | 🔴 終了 (2026-06-01) `[1]` | Greengrass V2 |
| **[Gazebo Classic 11](https://classic.gazebosim.org/)** | 🔴 EOL (2025-01) `[1]` | Gazebo Jetty/Harmonic |
| **Trainium for VLA** | ⚪ 公開事例なし `[4]` | 現在は CUDA/NVIDIA（提案時にリスクを明示） |

> ⚠️ **噂への警戒（事実ではない）**: 「AWS IoT TwinMaker 廃止」は**誤情報** — TwinMaker は GA・新規顧客に開放（低速度）。SiteWise のメンテナンスと混同した第三者ブログの主張です。繰り返さないでください。→ [pillar-3](pillar-3.md)。

---

## 昇格手順（要約）

1. **キャプチャ**: 指定チャンネル/絵文字で候補を収集
2. **フィルタ**: [2.5 ゲート](maintenance.md#包含基準-the-filter)を適用（4 項目中 2 項目以上）
3. **通過時**: 担当ピラーの owner が[標準テンプレート](maintenance.md#標準テンプレート)で編入し、Radar から削除
4. **未達時**: ここに一行で保持し、昇格条件を明示

パイプライン全体 → [maintenance](maintenance.md#playbook-昇格パイプライン)。

---
_owner: Youngjin · updated: 2026-08 · volatility: 高（Radar は本質的に急速に変化します — 月次レビューを推奨）_

<!-- 용어 각주 -->

[^wfm]: **ワールド基盤モデル（WFM, World Foundation Model）** — 物理世界の次のシーンを予測・生成するよう学習された大型モデルです。テキスト・映像プロンプトから物理的にもっともらしい映像・シナリオを作り、ロボット学習データを拡張します。🎥 [NVIDIA Cosmos 紹介](https://www.youtube.com/watch?v=9Uch931cDx8)
[^sysid]: **システム同定（SysID, System Identification）** — 実機ロボットの物理パラメータ（摩擦・質量・モーター応答）を測定し、シミュレーターを実物に合わせて校正する作業です。
[^s2r]: **sim-to-real** — シミュレーションで学習したポリシーを実際のロボットへ移すこと、またはその方法論です。シミュレーションと現実の物理・視覚の差（ドメインギャップ）のため、そのまま移すと性能が崩れます。🎥 [NVIDIA sim-to-real ロボティクスショーケース](https://www.youtube.com/watch?v=sffNvv3GkRA)
[^physeng]: **物理エンジン（physics engine）** — 剛体動力学・接触・摩擦・衝突を数値的に計算するシミュレーターの中核ソフトウェアです。エンジンの精度・速度のトレードオフがシミュレーター選択（Isaac/MuJoCo/Genesis）を左右します。
[^mcp]: **MCP（Model Context Protocol）** — エージェントとツール・データソースをつなぐオープン標準プロトコルです。「エージェント用 USB-C」に例えられ、ロボットスキルを MCP サーバーとして公開する実験が増えています。
[^ros]: **ROS 2 (Robot Operating System 2)** — ロボットソフトウェアの事実上の標準オープンソースミドルウェアです。センサー・制御ノードがトピック（topic）で通信する分散構造で、産業・研究ロボットスタックの共通基盤です。
[^agent]: **LLM エージェント** — 大規模言語モデルが自ら計画を立て、ツール（API・ロボットスキル）を選んで呼び出し、多段階のタスクを遂行するソフトウェアです。単純な質疑応答と異なり「行動」がある点が核心です。
[^vla]: **VLA (Vision-Language-Action)** — カメラ映像（Vision）と自然言語の指示（Language）を入力に、ロボットの動作（Action）を直接出力する基盤モデルです。「コップを掴んで」と言えば関節の動きを生成する、という具合です。🎥 [NVIDIA Isaac GR00T N1 紹介](https://www.youtube.com/watch?v=m1CH-mgpdYg)
[^lbm]: **Large Behavior Models (LBM)** — LLM の「ロボット行動」版。大規模な実演データで学習し、1 つのモデルで多様なマニピュレーションタスクを実行するロボット基盤モデルを指す Toyota Research Institute の用語です。
[^diffpol]: **Diffusion Policy** — 画像生成に使われる拡散（diffusion）モデルでロボットの動作シーケンスを生成するポリシーアーキテクチャです。複数の有効なやり方を含む実演データを安定して学習でき、模倣学習の事実上の標準になりました。
[^umi]: **UMI (Universal Manipulation Interface)** — ロボットなしで、人がカメラ付きのハンドヘルドグリッパーを持って実演データを集める収集方式です。ロボットを投入せずに実世界データを大量に確保できます。
[^sdg]: **合成データ生成（SDG, Synthetic Data Generation）** — シミュレーターで学習用画像とアノテーション（ラベル）を自動生成する技法です。ラベリングコストがゼロに収束するのが最大の利点です。🎥 [Isaac Sim Replicator SDG チュートリアル](https://www.youtube.com/watch?v=HHzNIh72B_Y)
