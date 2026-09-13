---
ko_hash: d53c0728060cfa89492e70e1df51bf30ecea741a
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

## 🆕 最新スキャン流入（2026-09-13 · 一次検証完了 2026-07-21）

<!-- 自動スキャン（arXiv/ウェブ）の流入分。2026-07-21 に一次ソース検証完了（検証エージェント 4 式、公式発表・arXiv 原文と照合）—— 昇格 0 件、訂正 6 件。THE FILTER を通過するまで顧客提案での使用禁止。定期更新は scripts/radar_scan.md を参照。 -->

| 項目 | ラベル | 要点 | 昇格条件 |
|---|---|---|---|
| **[GHOST](https://arxiv.org/abs/2608.29080)**（オンボードカメラのみで 1 人が 2 台のロボットを同時遠隔操作する VR テレオペレーション） | 🔵 Research | ✨ **注目**: Brown University（Tellex lab）が Amazon の資金支援を受けて開発 — 外部モーションキャプチャなしでオンボード RGB-D のみを使い、1 人のオペレーターが Boston Dynamics Spot 2 台を VR で同時遠隔操作、IEEE RA-L に掲載(peer-review 通過)。初心者の成功率 1.6~4 倍、エキスパートの作業速度 1.47 倍向上を実測 — テレオペレーションによるロボットデータ収集パイプラインのコストを下げうるオープンソース事例<br>⏳ **待機**: arXiv 2608.29080（2026-08-29、IEEE RA-L 2026-08 accept）`[4]` — エキスパート評価者は論文著者本人 3 名（バイアスの可能性）、初心者評価は n=15（9 タスク中 2 タスクのみ実施）、Boston Dynamics Spot 専用ハードウェア・専用 Wi-Fi 環境（本番環境での信頼性は未検証） | 独立ユーザー評価の拡大 + 多様なハードウェア・ネットワーク環境での検証 |
| **[Perceptron Isaac 0.5](https://github.com/perceptron-ai-inc/isaac)**（オープンウェイト埋め込み型ファウンデーションモデル、360 億パラメータ） | 🔵 Research | ✨ **注目**: 動画理解・エンボディード推論・ロボット制御を単一のスパースバックボーンに統合し、オープンウェイトとして公開 — 35 以上のロボットシステム・10 万時間超のロボット経験・100 万時間の動画・3T のマルチモーダルトークンで学習、π0.5・GR00T N1.7 を上回ると自己申告し、コード・重みを同時公開（コードは Apache-2.0）<br>⏳ **待機**: 公式発表 + GitHub 公式リポジトリ（2026-08-27/28、元 Meta 研究者によるスタートアップ Perceptron AI）`[4]` —— 自己申告ベンチマークで、独立再現・peer-review なし。重み自体のライセンス条件は Hugging Face リポジトリに別途記載（本調査ではアクセス未確認） | 独立ベンチマーク再現 + 実導入事例 |
| **[ABEJA×村田製作所 GR00T N1.7 双腕 PoC](https://prtimes.jp/main/html/rd/p/000000229.000010628.html)**（VLA ベースの物理AI技術検証） | 🟡 Preview | ✨ **注目**: 日本の製造大手・村田製作所が NVIDIA GR00T N1.7（商用ライセンスのオープン VLA）で双腕ロボットの部品受け渡し・姿勢転換・挿入という連続動作を実機で検証 —— 実際の製造大手が商用ライセンスのオープン VLA を検証した初期事例、ラボオートメーションの角度<br>⏳ **待機**: ABEJA・村田製作所の公式発表（2026-08-31、PR TIMES）`[4]` —— 数百件のテレオペレーション実演データで模倣学習、検証（テスト）環境下で実機成功。量産規模の展開・自律性能の独立検証はなし。⚠️ リンクは PR TIMES の公式発表だが、本実行環境の egress 制限により curl 200 の手動確認は未実施（コミットメッセージ・issue 参照） | 量産ラインへの展開 + 独立検証 |
| **[NEURA Robotics 4NE1 / Neuraverse × AWS](https://press.aboutamazon.com/aws/2026/4/neura-robotics-and-aws-enter-strategic-collaboration-to-accelerate-physical-ai-at-scale)**（ドイツのフルスタックロボティクス企業、AWS 戦略的協業） | ⚪ ロードマップ | ✨ **注目**: AWS が Neuraverse の主要クラウドプロバイダーとなり、Gym トレーニング環境を SageMaker と統合、NEURA が AWS Partner Network に参加 — サービス名まで具体的な AWS パートナーシップで、Radar 内でも特に具体性が高い「AWS 自社」物理 AI 事例のひとつで、注目すべき欧州ヒューマノイドトラック<br>⏳ **待機**: AWS・NEURA の公式発表（2026-04-21、press.aboutamazon.com）`[4]` — Amazon フルフィルメントセンターへの配備は「検討中」段階に過ぎず実デプロイではない。最大 14 億ドルのシリーズ C（2026-06-10、Amazon・NVIDIA・Tether などが参加、フルスタックロボティクス企業史上最大の調達額）と IFA ベルリン 2026 キーノート（2026-09-05、4NE1 実機展示）で話題が再燃、第三者検証なし。⚠️ リンクは press.aboutamazon.com の公式発表だが、本実行環境の egress 制限により curl 200 の手動確認は未実施（コミットメッセージ・issue 参照） | Amazon フルフィルメントセンターなどの公開デプロイ事例 + 独立した性能検証 |
| **[RLWRLD RLDX-1](https://arxiv.org/abs/2605.03269)**（81 億パラメータのデクステリティ[^dext]基盤モデル、AWS Generative AI Accelerator 参加） | 🔵 Research | ✨ **注目**: KAIST 出身のソウルのスタートアップが AWS Generative AI Accelerator のコンピュートで学習したオープンロボティクス基盤モデルを AWS 公式ブログが直接紹介 — 5 指ハンドによる精密操作に特化し、GR00T N1.6・π0.5 に対する優位性を自社ベンチマークで主張する韓国発の「AWS 自社」パートナーシップ事例（NEURA と並ぶ Radar 内の公式 AWS 協業事例）<br>⏳ **待機**: RLWRLD 公式発表 + arXiv 技術レポート（2026-05、arXiv 2605.03269）`[4]` — 8 件の公開ベンチマークでの自己測定値（例: GR-1 Tabletop 58.7 点、GR00T N1.6 比 +10.7pt）、独立再現・peer-review なし。AWS との関係は accelerator 参加段階、実導入は LOTTE HOTEL & RESORT との 2030 年目標（初期段階）。⚠️ リンクは arXiv 原文だが、本実行環境の egress 制限により curl 200 の手動確認は未実施（コミットメッセージ・issue 参照） | 独立ベンチマーク再現 + 実導入事例 |
| **[Figure Index](https://www.figure.ai/index-app)**（人間の映像をもとにしたクラウドソーシング型ロボットデータ収集アプリ） | 🟡 Preview | ✨ **注目**: Figure AI が自社 VLA「Helix」の学習データを、ベンダーからの購入ではなく一般人向けの有料クラウドソーシングアプリで直接収集 — 2026-08-25 の公開後、108 か国で週間アクティブユーザー 4.4 万人超、アップロード映像 1,600 万本超（毎秒約 30 分相当）、今後 12 か月でデータ・コンピュートに 10 億ドル超を投資すると公表 — 実世界映像データパイプラインを自社運営する稀有な事例<br>⏳ **待機**: Figure 公式（figure.ai）`[4]` —— コントリビューターへの累計支払いは 1,500 万ドルとの発表のみで、収集映像が Helix のポリシー性能に実際どれだけ寄与しているかの定量成果・品質管理方式は独立検証されていない。⚠️ 本実行環境の egress 制限により curl 200 の手動確認は未実施（コミットメッセージ・issue 参照） | Helix ポリシー性能改善の実測公開 + 独立検証 |
| **[KIMM KAIROS V0.7](https://www.kimm.re.kr/eng/sub011001/view/id/1565)**（K-Moonshot 国家戦略技術課題による国産 AI ヒューマノイド） | ⚪ ロードマップ | ✨ **注目**: 韓国機械研究院（KIMM）が科学技術情報通信部支援の「AI ヒューマノイド・グローバルトップ研究団」として開発する国策ヒューマノイド —— 2026-09-07 の「2026 グローバル機械技術フォーラム」で V0.7 を公開、国民体操や伝統仮面舞（タルチュム）の動作まで実演（4 月の V0.5 は握手・手振りのみ）—— 韓国の顧客対話で直接挙がりうる「国策研究機関発」ヒューマノイドのトラック（現代・BD Atlas とは異なる角度）<br>⏳ **待機**: KIMM 公式発表 `[4]`（二次: 韓国国内の複数メディアで交差確認 —— 体操・仮面舞の実演は自己申告。⚠️ 本実行環境の egress 制限により kimm.re.kr の curl 200 手動確認は未実施、コミットメッセージ・issue 参照）—— V1.0 公開は 2027-04 目標、追加開発費（約 30 億ウォン）が必要と報じられている。商用化・自律性能は現状ゼロ、まだデモ段階 | V1.0 公開 + 自動車組立・家庭用の実証事例公開 |
| **[Generalist AI GEN-1.5](https://generalistai.com/blog/gen-1.5)**（物理相互作用データで 8 か月以上事前学習したエンボディード基盤モデル。単一の 3~12 秒デモだけで、勾配更新やファインチューニングなしに新タスクを即座に実行するワンショット学習） | 🔵 Research | ✨ **注目**: 3~12 秒のデモ映像を「物理的プロンプト」としてコンテキストに挿入し、ファインチューニングなしで新タスクを即座に試行 —— VLA のタスクごとのファインチューニング依存を下げうる軸で、複数メディアが「ロボティクスの GPT-3 モーメント」と評価<br>⏳ **待機**: 会社の公式発表のみ（2026-08-19、generalistai.com）`[4]` —— 10 タスクでの自己申告ベンチマーク（ワンショット平均成功率 59%、5 分のデータ+10 勾配ステップ後に 83%）、独立再現・peer-review なし。⚠️ 本実行環境の egress 制限により generalistai.com の curl 200 手動確認は未実施（コミットメッセージ・issue 参照） | 独立ベンチマーク再現 + 多様なタスク・ハードウェアでの検証 |
| **[NVIDIA Isaac GR00T Reference Humanoid Robot](https://nvidianews.nvidia.com/news/nvidia-open-humanoid-robot-reference-design)**（オープンなレファレンスヒューマノイドハードウェア、GTC Taipei で発表） | 🟡 Preview | ✨ **注目**: NVIDIA が初めて発表した完全なレファレンスヒューマノイドハードウェア —— Unitree H2 Plus シャシー（31 DOF）+ Sharpa Wave 触覚 5 指ハンド（22 DOF）+ Jetson AGX Thor T5000 オンボードコンピュート + Isaac GR00T ソフトウェアスタックで構成 —— Radar に既にある NEURA Robotics・1X などが GR00T エコシステムのパートナーとして参加し、GR00T がソフトウェアからハードウェアまで垂直統合される兆候<br>⏳ **待機**: NVIDIA 公式発表（2026-06-01、GTC Taipei）`[4]`（一次ソース nvidianews.nvidia.com —— 本実行環境の egress 制限により curl 200 の手動確認は未実施、コミットメッセージ・issue 参照）—— Unitree 経由の出荷は「2026 年末」予定で対象は学術研究用（Stanford・ETH Zurich・Ai2・UC San Diego がローンチパートナー）、実際の出荷・研究成果は 0 件 | 実際の出荷 + 研究機関での活用成果の公開 |
| **[UBTech UWORLD U1](https://www.prnewswire.com/news-releases/ubtech-launches-uworld-u1-the-worlds-first-full-size-mass-produced-ultra-bionic-humanoid-robot-302815272.html)**（中国発の家庭用コンパニオンヒューマノイド、88 DOF） | 🟡 Preview | ✨ **注目**: UBTECH が「世界初のフルサイズ量産型」家庭用コンパニオンヒューマノイドとして公開 —— 3 モデルライン（1 万 7,600〜14 万 5,000 ドル）、予約 1.3 万台超を確保後 2026-09-16 に初回配送開始予定 —— 消費者向けヒューマノイド量産トラックで 1X Neo とは異なる角度（中国発の大量生産・量産価格公開）<br>⏳ **待機**: UBTECH 公式発表（2026-06-30）`[4]`（一次ソースは PRNewswire の公式発表だが、本実行環境の egress 制限により curl 200 の手動確認は未実施、コミットメッセージ・issue 参照）—— 「量産」の主張は発表・予約段階にとどまり、実際の配送・自律性能（遠隔操作比率など）の独立検証はまだない | 配送完了 + 独立したユーザーレビュー・自律性能検証 |

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
[^dext]: **デクステリティ（dexterity）** — ロボットの手・アームが人の手のように精緻かつ器用に物体を扱う能力です。単純なグリッパーの把持・配置とは異なり、5 指ハンドで物体を回転させたり道具を操作したりするなど、接触の多い複雑な操作を指します。
