# AI model timeline record and visibility audit

Compared `e02ecd6` (before update) with `23c4941` (September 30 update). This report describes the first update; subsequent fixes are documented in the follow-up audit. The paired [JSON artifact](record-audit-first-update.json) contains all 484 original records with full before/after values, not just changed names. Lifecycle results execute the actual inline modeling code from each commit.

## Conclusion

No original record is unmapped or demonstrably dropped at the model-identity level. Fifteen old display-name strings disappear: thirteen expand into separate variants, and two Wan names become more specific. All named components remain represented. GPT-6 Astra survives unchanged in name and date; GPT-6 Sol and Luna survive as separate records. The disappearance complaint is supported by clear discoverability regressions caused by the data reorganization interacting with unchanged layout/search behavior.

Important limits: this audit verifies record continuity and code behavior, not the truth of each linked external release claim. The generic Wan3.0 record changes its documented first date and stage, and Music-1.5 distinguishes beta from GA; these are semantic remappings that should not be described as simple unchanged records.

## Accounting, with identity mapping

- old_records: 484
- new_records: 579
- retained_exact_names: 469
- old_name_strings_absent: 15
- split_old_records: 13
- renamed_old_records: 2
- unmapped_old_records: 0
- new_name_strings: 110
- new_names_from_splits_or_renames: 28
- new_records_beyond_name_mapping: 82
- same_name_lane_changes: 185
- same_name_date_changes: 10
- all_mapped_date_changes: 12
- all_mapped_type_changes: 10
- old_records_newly_unverified: 13
- Same companies: 18 before and after. Original 83 lanes / 83 rendered rows become 213 lanes / 222 rendered rows.
- The 82 additions beyond absent-name replacements include Music-1.5 Beta under exact-name accounting; under release-event accounting, the old beta event is preserved and the formal Music-1.5 event is new instead. Total additions are unchanged by that interpretation.

## Every absent original display name: removed / renamed / split mapping

| Company | Old name, date, lane | Replacement record(s) | Interpretation |
| --- | --- | --- | --- |
| openai | GPT-5.6 Sol / Terra — 2026-06-26 — GPT 主线 | GPT-5.6 Sol — 2026-06-26 — GPT Sol [flagship]; GPT-5.6 Terra — 2026-06-26 — GPT Terra [flagship] | split:  |
| openai | GPT-4.1 mini / nano — 2025-04-14 — 轻量 mini/nano | GPT-4.1 mini — 2025-04-14 — GPT mini [small]; GPT-4.1 nano — 2025-04-14 — GPT nano [small] | split:  |
| openai | GPT-5 mini / nano — 2025-08-07 — 轻量 mini/nano | GPT-5 mini — 2025-08-07 — GPT mini [small]; GPT-5 nano — 2025-08-07 — GPT nano [small] | split:  |
| openai | GPT-5.4 mini / nano — 2026-03-17 — 轻量 mini/nano | GPT-5.4 mini — 2026-03-17 — GPT mini [small]; GPT-5.4 nano — 2026-03-17 — GPT nano [small] | split:  |
| openai | GPT-6 Sol / Luna — 2026-09-22 — 轻量 mini/nano | GPT-6 Sol — 2026-09-22 — GPT Sol [flagship]; GPT-6 Luna — 2026-09-22 — GPT Luna [small] | split: Both survive with the same 2026-09-22 launch. Sol changes from the combined small classification to flagship; Luna remains small. GPT-6.1 Sol, added on 2026-09-29, ends the Sol predecessor bar after 7 days. |
| openai | gpt-oss-120b / 20b — 2025-08-05 — 开源 gpt-oss | gpt-oss-120b — 2025-08-05 — gpt-oss 120B [open]; gpt-oss-20b — 2025-08-05 — gpt-oss 20B [open] | split:  |
| openai | GPT Image 2.5 — 2026-09-08 — 图像/视频 (DALL·E, Sora, gpt-image) | GPT Image 2.5 Flare — 2026-09-08 — 图像 GPT Image Flare [media]; GPT Image 2.5 Sunburst — 2026-09-08 — 图像 GPT Image Sunburst [media] | split: Family row is expanded to Flare and Sunburst at the same 2026-09-08 date. The previous Sketch feature note is removed, but there was no separate Sketch model record. |
| anthropic | Claude Fable 5 / Mythos 5 — 2026-06-09 — Mythos/Fable | Claude Fable 5 — 2026-06-09 — Fable [flagship]; Claude Mythos 5 — 2026-06-09 — Mythos 受限 [flagship] | split: Public Fable and restricted Mythos are preserved in separate lanes, both on 2026-06-09. |
| anthropic | Claude Fable 5.1 / Mythos 5.1 — 2026-09-01 — Mythos/Fable | Claude Fable 5.1 — 2026-09-01 — Fable [flagship]; Claude Mythos 5.1 — 2026-09-01 — Mythos 受限 [flagship] | split: Public Fable and restricted Mythos are preserved in separate lanes, both on 2026-09-01. |
| meta | Llama 4 Scout / Maverick — 2025-04-05 — Llama 开源 | Llama 4 Scout — 2025-04-05 — Llama Scout [open]; Llama 4 Maverick — 2025-04-05 — Llama Maverick [open] | split:  |
| mistral | Codestral Mamba / Mathstral — 2024-07-16 — 代码 Codestral/Devstral | Codestral Mamba — 2024-07-16 — 代码 Codestral Mamba [code]; Mathstral — 2024-07-16 — 数学 Mathstral [open] | split: Code and mathematics variants are both preserved. Mathstral changes from combined code classification to open. |
| deepseek | DeepSeek-V4 (Preview) — 2026-04-24 — V 系列通用 | DeepSeek-V4-Pro-Preview — 2026-04-24 — V4 Pro 旗舰 [flagship]; DeepSeek-V4-Flash-Preview — 2026-04-24 — V4 Flash 通用 [open] | split: Old note explicitly included both Pro and Flash. Pro remains flagship; Flash is now open. Both preserve 2026-04-24. |
| alibaba | Qwen3.8-2.4T-A95B / 27B — 2026-08-12 — Qwen 主线 | Qwen3.8-2.4T-A95B — 2026-08-12 — Qwen 主线 [open]; Qwen3.8-27B — 2026-08-14 — Qwen 27B 稠密 [open] | split: Both variants survive. The 27B variant moves from the shared 2026-08-12 date to its own 2026-08-14 date. |
| alibaba | Wan2.7 — 2026-04-03 — 万相 Wan/图像生成 | Wan2.7-Video — 2026-04-03 — 万相 Wan 视频 [media] | renamed: Old note describes video; Wan2.7-Video preserves the same date and note. Wan2.7-Image (2026-04-01) is a separate addition. |
| alibaba | Wan3.0 — 2026-08-24 — 万相 Wan/图像生成 | Wan3.0-Video (Beta) — 2026-08-06 — 万相 Wan 视频 [media] | renamed: Generic old video row is replaced by explicit Beta identity; recorded first date changes 2026-08-24 → 2026-08-06. Wan3.0-Video-Prime (2026-08-20) is a separate addition. Old 08-24 event is no longer represented as an independent milestone; its identity was ambiguous. |

## Every added record beyond those renamed / split replacements

These are explicit additions to the original inventory, grouped by company. Split-child identities from the previous table are excluded to avoid double counting.

### openai

- GPT-6.1 Sol — 2026-09-29 — GPT Sol [flagship]
- GPT-5.3 Instant — 2026-03-03 — GPT Instant [flagship]
- GPT-5.5 Instant — 2026-05-05 — GPT Instant [flagship]
- GPT-5.5 Instant Mini — 2026-07-06 — GPT Instant mini [small]
- GPT-5.3-Codex-Spark — 2026-02-12 — 编程 Codex Spark [code]
- GPT-Live-1 — 2026-07-08 — 语音 GPT Live [media]
- GPT-Live-1 mini — 2026-07-08 — 语音 GPT Live mini [media]

### anthropic

- Claude Sonnet 5.5 — 2026-09-28 — Sonnet [flagship]

### google

- Gemini 3.1 Flash-Lite — 2026-03-03 — Gemini Flash-Lite [small]
- Gemini 3.5 Flash-Lite — 2026-07-21 — Gemini Flash-Lite [small]
- Gemini 3.5 Flash Cyber — 2026-07-21 — Gemini Flash Cyber [code]
- Gemini 3.8 Flash Cyber — 2026-09-02 — Gemini Flash Cyber [code]
- Gemini 3.8 Live — 2026-09-15 — 语音 Gemini Live [media]
- Gemini 3.8 Live Extended Thinking — 2026-09-15 — 语音 Gemini Live Thinking [media]
- Gemini 3.5 Transcribe — 2026-08-26 — 语音 Gemini Transcribe [media]
- Gemini 3.5 Transcribe Live — 2026-08-26 — 语音 Gemini Transcribe Live [media]
- Lyria 3.5 — 2026-09-03 — 音乐 Lyria [media]

### meta

- Muse Video (preview) — 2026-07-07 — 视频 Muse Video [media]
- Muse Voice Transcribe — 2026-09-01 — 语音 Muse Transcribe [media]
- Muse Realtime Avatar — 2026-09-23 — 实时形象 Muse Avatar [media]

### xai

- Imagine Image 2.0 — 2026-08-07 — 图像 Imagine [media]
- Grok Voice Transcribe 2.0 — 2026-09-18 — 语音 Grok Transcribe [media]

### microsoft

- MAI-Image-2.6 — 2026-08-10 — MAI 图像 [media]
- MAI-Image-2.5-Pro — 2026-07-23 — MAI 图像 Pro [media]
- MAI-Image-2-Efficient — 2026-04-14 — MAI 图像快速版 [media]
- MAI-Image-2.5-Flash — 2026-06-02 — MAI 图像快速版 [media]
- MAI-Image-2.6-Flash — 2026-09-04 — MAI 图像快速版 [media]
- MAI-Cyber-1-Flash — 2026-08-13 — MAI 安全 [code]
- MAI-Code-1-Flash — 2026-06-02 — MAI 编程 [code]
- MAI-Code-1.1-Flash — 2026-08-11 — MAI 编程 [code]
- MAI-Voice-2-Flash — 2026-06-02 — MAI 语音合成 Flash [media]
- MAI-Transcribe-1.5 — 2026-06-02 — MAI 语音识别 [media]
- MAI-Transcribe-2 — 2026-09-03 — MAI 语音识别 [media]

### amazon

- Nova Act (GA) — 2025-12-02 — 浏览器智能体 (Act) [code]

### mistral

- Codestral 25.08 — 2025-07-30 — 代码 Codestral [code]
- Mistral Moderation 2603 — 2026-03-12 — 内容审核 [small]
- Mistral OCR 2 — 2025-05-22 — 文档识别 OCR [media]
- Mistral OCR 4.1 — 2026-07-16 — 文档识别 OCR [media]

### alibaba

- Qwen3.6-Max-Preview — 2026-04-18 — Qwen Max 旗舰 [flagship]
- Qwen3.8-Flash-Next — 2026-08-26 — Qwen Next 架构 [open]
- Qwen3.7-Plus — 2026-06-01 — Qwen Plus 通用 [flagship]
- Wan2.7-Image — 2026-04-01 — 万相 Wan 图像 [media]
- Qwen-Image-3.0 — 2026-07-21 — 图像 Qwen-Image [media]
- Qwen3.6-27B — 2026-04-22 — Qwen 27B 稠密 [open]
- Wan3.0-Video-Prime — 2026-08-20 — 万相 Wan 视频高速 [media]
- Qwen3.5-LiveTranslate-Flash — 2026-05-19 — 同声传译 LiveTranslate [media]
- Qwen3.8-LiveTranslate — 2026-09-18 — 同声传译 LiveTranslate [media]
- Qwen3.8-Omni-Flash-Realtime — 2026-09-21 — 实时全模态 Omni [media]
- Qwen-Audio-3.0-Realtime-Plus — 2026-07-14 — 实时语音 Audio Plus [media]
- Qwen-Audio-3.1-Realtime-Plus — 2026-09-20 — 实时语音 Audio Plus [media]
- Qwen-Audio-3.0-Realtime-Flash — 2026-07-14 — 实时语音 Audio Flash [media]
- HappyHorse-1.0-T2V — 2026-04-21 — HappyHorse 视频 [media]
- HappyHorse-1.1 — 2026-06-16 — HappyHorse 视频 [media]
- HappyOyster-1.0-Adventure — 2026-09-17 — 世界模型 HappyOyster Adventure [media]
- HappyOyster-1.0-Directing — 2026-09-17 — 世界模型 HappyOyster Directing [media]
- HappyOyster-1.0-Acting — 2026-09-17 — 世界模型 HappyOyster Acting [media]
- Decision-Model-Preview — 2026-09-24 — 结构化决策 [reasoning]

### bytedance

- Seed-2.1-Pro-Preview — 2026-06-19 — 豆包/Seed 通用 [flagship]
- Seed Audio 1.0 — 2026-07-20 — 音频生成 Seed Audio [media]
- SeedRealtime — 2026-08-05 — 实时交互 SeedRealtime [media]

### zhipu

- GLM-4.7-Flash — 2026-01-19 — 轻量语言 GLM Flash [small]
- GLM-OCR — 2026-02-03 — 文档理解 GLM-OCR [open]

### baidu

- ERNIE-Image — 2026-04-15 — 图像 ERNIE-Image [open]
- ERNIE-Image-Turbo — 2026-04-15 — 图像 ERNIE-Image Turbo [open]
- PaddleOCR-VL-1.5 — 2026-01-29 — 文档理解 PaddleOCR [open]

### tencent

- 混元3D 3.1 — 2026-01-16 — 3D 生成 [media]
- HY-World 2.1 — 2026-07 — 世界模型 [media] — unverified
- Hy ASR 3.0 preview — 2026-08-04 — 语音识别 [media] — unverified

### minimax

- Music-1.5 Beta — 2025-06-20 — 音乐生成 [media]
- Music-2.5+ — 2026-03-04 — 音乐生成 [media]
- Music-2.6 — 2026-04-10 — 音乐生成 [media]
- MiniMax-M2-her — 2026-01-27 — 角色扮演 [flagship]

### stepfun

- Step Image Edit 2 — 2026-04-29 — 图像编辑 [media]
- StepAudio 3 Realtime — 2026-09-12 — 语音交互 [media]
- Step-Audio-R1.1 — 2026-01-14 — 语音推理 [open]
- Step-Audio-R1.5 — 2026-04-29 — 语音推理 [reasoning]
- StepAudio 3 Gen — 2026-09-11 — 通用音频生成 [media]
- StepAudio 3 Music — 2026-09-11 — 音乐生成 [media]
- StepAudio 3 ASR — 2026-09-15 — 语音识别 [media]
- StepAudio 3 TTS — 2026-09-15 — 语音合成 [media]

### iflytek

- 星火 X2-Flash — 2026-04-29 — 星火 Flash [small]
- 星火 X2-VL — 2026-06-11 — 视觉理解 [flagship]

## Every same-name record moved to a different lane

The earlier mapping table includes all lane changes on renamed/split records. This table is the exhaustive list for names that stayed identical.
| Company | Model | Old lane | New lane |
| --- | --- | --- | --- |
| openai | GPT-6 Astra | GPT 主线 | GPT Astra |
| openai | GPT-4o mini | 轻量 mini/nano | GPT mini |
| openai | o1-mini | 轻量 mini/nano | o 系列 mini |
| openai | o3-mini | 轻量 mini/nano | o 系列 mini |
| openai | o4-mini | 轻量 mini/nano | o 系列 mini |
| openai | GPT-5.6 Luna | 轻量 mini/nano | GPT Luna |
| openai | GPT-2 1.5B (完整权重) | 开源 gpt-oss | GPT-2 开放权重 |
| openai | Whisper | 开源 gpt-oss | 语音识别 Whisper |
| openai | gpt-oss-safeguard | 开源 gpt-oss | gpt-oss 安全分类 |
| openai | DALL·E | 图像/视频 (DALL·E, Sora, gpt-image) | 图像 DALL·E |
| openai | DALL·E 2 | 图像/视频 (DALL·E, Sora, gpt-image) | 图像 DALL·E |
| openai | DALL·E 3 | 图像/视频 (DALL·E, Sora, gpt-image) | 图像 DALL·E |
| openai | Sora | 图像/视频 (DALL·E, Sora, gpt-image) | 视频 Sora |
| openai | GPT Image 1 (4o 生图) | 图像/视频 (DALL·E, Sora, gpt-image) | 图像 GPT Image |
| openai | Sora 2 | 图像/视频 (DALL·E, Sora, gpt-image) | 视频 Sora |
| openai | GPT Image 1.5 | 图像/视频 (DALL·E, Sora, gpt-image) | 图像 GPT Image |
| openai | GPT Image 2 | 图像/视频 (DALL·E, Sora, gpt-image) | 图像 GPT Image |
| anthropic | Claude Mythos Preview | Mythos/Fable | Mythos 受限 |
| google | Bard | Gemini Pro/Ultra | Bard 产品 |
| google | Gemini 1.0 Pro | Gemini Pro/Ultra | Gemini Pro |
| google | Gemini 1.0 Ultra | Gemini Pro/Ultra | Gemini Ultra |
| google | Gemini 1.5 Pro | Gemini Pro/Ultra | Gemini Pro |
| google | Gemini 2.0 Pro | Gemini Pro/Ultra | Gemini Pro |
| google | Gemini 2.5 Pro | Gemini Pro/Ultra | Gemini Pro |
| google | Gemini 3 Pro | Gemini Pro/Ultra | Gemini Pro |
| google | Gemini 3.1 Pro | Gemini Pro/Ultra | Gemini Pro |
| google | Gemma 3n | Gemma 开源 | Gemma 端侧 |
| google | Gemma 4 12B | Gemma 开源 | Gemma 12B |
| google | Imagen | Imagen/Nano Banana 图像 | 图像 Imagen |
| google | Imagen 2 | Imagen/Nano Banana 图像 | 图像 Imagen |
| google | Imagen 3 | Imagen/Nano Banana 图像 | 图像 Imagen |
| google | Imagen 4 | Imagen/Nano Banana 图像 | 图像 Imagen |
| google | Nano Banana (2.5 Flash Image) | Imagen/Nano Banana 图像 | 图像 Nano Banana Flash |
| google | Nano Banana Pro (3 Pro Image) | Imagen/Nano Banana 图像 | 图像 Nano Banana Pro |
| google | Nano Banana 2 (3.1 Flash Image) | Imagen/Nano Banana 图像 | 图像 Nano Banana Flash |
| google | Veo | Veo/Omni 视频 | 视频 Veo |
| google | Veo 2 | Veo/Omni 视频 | 视频 Veo |
| google | Veo 3 | Veo/Omni 视频 | 视频 Veo |
| google | Veo 3.1 | Veo/Omni 视频 | 视频 Veo |
| google | Gemini Omni Flash | Veo/Omni 视频 | 视频 Gemini Omni |
| meta | Muse Glimmer | Llama 开源 | Muse Glimmer 开放权重 |
| meta | Code Llama | 代码 Code Llama/CWM | 代码 Code Llama |
| meta | Code Llama 70B | 代码 Code Llama/CWM | 代码 Code Llama |
| meta | CWM (Code World Model) | 代码 Code Llama/CWM | 代码 CWM |
| meta | Make-A-Video | 图像/视频生成 | 视频研究 Make-A-Video |
| meta | Emu | 图像/视频生成 | 图像 Emu |
| meta | Movie Gen | 图像/视频生成 | 视频研究 Movie Gen |
| meta | Muse Image | 图像/视频生成 | 图像 Muse Image |
| meta | Muse Spark | Muse 闭源 (MSL) | Muse Spark |
| meta | Muse Spark 1.1 | Muse 闭源 (MSL) | Muse Spark |
| meta | Muse Spark 1.2 | Muse 闭源 (MSL) | Muse Spark |
| meta | Muse Spark 1.3 | Muse 闭源 (MSL) | Muse Spark |
| xai | Aurora | 图像/视频 (Aurora, Imagine) | 图像 Aurora |
| xai | Grok Imagine | 图像/视频 (Aurora, Imagine) | Imagine 图像/视频初代 |
| xai | Grok Imagine 1.0 | 图像/视频 (Aurora, Imagine) | 视频 Imagine |
| xai | Grok Imagine 1.5 (preview) | 图像/视频 (Aurora, Imagine) | 视频 Imagine |
| microsoft | Phi-4-mini-flash-reasoning | Phi 推理 | Phi 轻量推理 |
| microsoft | Phi-4-reasoning-vision-15B | Phi 推理 | Phi 视觉推理 |
| microsoft | MAI-1-preview | MAI 文本/推理 | MAI 文本 |
| microsoft | MAI-Thinking-1 | MAI 文本/推理 | MAI 推理 |
| microsoft | MAI-Voice-1 | MAI 语音 | MAI 语音合成 |
| microsoft | MAI-Transcribe-1 | MAI 语音 | MAI 语音识别 |
| microsoft | MAI-Voice-2 | MAI 语音 | MAI 语音合成 |
| amazon | Nova Act (preview) | 语音/智能体 (Sonic, Act) | 浏览器智能体 (Act) |
| amazon | Nova Sonic | 语音/智能体 (Sonic, Act) | 语音交互 (Sonic) |
| amazon | Nova 2 Sonic | 语音/智能体 (Sonic, Act) | 语音交互 (Sonic) |
| amazon | Titan Image Generator | 图像 (Titan Image, Canvas) | 图像 (Titan Image) |
| amazon | Titan Image Generator v2 | 图像 (Titan Image, Canvas) | 图像 (Titan Image) |
| amazon | Nova Canvas | 图像 (Titan Image, Canvas) | 图像 (Nova Canvas) |
| mistral | Mistral Medium | 旗舰 Large/Medium | 旗舰 Medium |
| mistral | Mistral Large | 旗舰 Large/Medium | 旗舰 Large |
| mistral | Mistral Large 2 | 旗舰 Large/Medium | 旗舰 Large |
| mistral | Mistral Large 24.11 | 旗舰 Large/Medium | 旗舰 Large |
| mistral | Mistral Medium 3 | 旗舰 Large/Medium | 旗舰 Medium |
| mistral | Mistral Medium 3.1 | 旗舰 Large/Medium | 旗舰 Medium |
| mistral | Mistral Large 3 | 旗舰 Large/Medium | 旗舰 Large |
| mistral | Mistral Medium 3.5 | 旗舰 Large/Medium | 旗舰 Medium |
| mistral | Mistral 7B | 开源/小模型 Mixtral·Small | 开源 Mistral 7B |
| mistral | Mixtral 8x7B | 开源/小模型 Mixtral·Small | Mixtral MoE |
| mistral | Mixtral 8x22B | 开源/小模型 Mixtral·Small | Mixtral MoE |
| mistral | Mistral NeMo 12B | 开源/小模型 Mixtral·Small | 开源 NeMo |
| mistral | Ministral 3B/8B | 开源/小模型 Mixtral·Small | 端侧 Ministral |
| mistral | Mistral Small 3 | 开源/小模型 Mixtral·Small | 通用 Small |
| mistral | Mistral Small 3.1 | 开源/小模型 Mixtral·Small | 通用 Small |
| mistral | Mistral Small 3.2 | 开源/小模型 Mixtral·Small | 通用 Small |
| mistral | Ministral 3 (3B/8B/14B) | 开源/小模型 Mixtral·Small | 端侧 Ministral |
| mistral | Mistral Small 4 | 开源/小模型 Mixtral·Small | 通用 Small |
| mistral | Codestral 22B | 代码 Codestral/Devstral | 代码 Codestral |
| mistral | Codestral 25.01 | 代码 Codestral/Devstral | 代码 Codestral |
| mistral | Devstral | 代码 Codestral/Devstral | 编程 Agent Devstral |
| mistral | Devstral Medium / Small 1.1 | 代码 Codestral/Devstral | 编程 Agent Devstral |
| mistral | Devstral 2 | 代码 Codestral/Devstral | 编程 Agent Devstral |
| mistral | Leanstral | 代码 Codestral/Devstral | 形式证明 Leanstral |
| mistral | Leanstral 1.5 | 代码 Codestral/Devstral | 形式证明 Leanstral |
| mistral | Pixtral 12B | 多模态/语音 Pixtral·Voxtral·OCR | 视觉 Pixtral |
| mistral | Pixtral Large | 多模态/语音 Pixtral·Voxtral·OCR | 视觉 Pixtral |
| mistral | Mistral OCR | 多模态/语音 Pixtral·Voxtral·OCR | 文档识别 OCR |
| mistral | Voxtral | 多模态/语音 Pixtral·Voxtral·OCR | 语音理解 Voxtral |
| mistral | Mistral OCR 3 | 多模态/语音 Pixtral·Voxtral·OCR | 文档识别 OCR |
| mistral | Voxtral Transcribe 2 | 多模态/语音 Pixtral·Voxtral·OCR | 语音转写 Voxtral |
| mistral | Voxtral TTS | 多模态/语音 Pixtral·Voxtral·OCR | 语音合成 Voxtral |
| mistral | Mistral OCR 4 | 多模态/语音 Pixtral·Voxtral·OCR | 文档识别 OCR |
| deepseek | DeepSeek-V4-Flash | V 系列通用 | V4 Flash 通用 |
| deepseek | DeepSeek-V4-Pro-0813 | V 系列通用 | V4 Pro 旗舰 |
| deepseek | DeepSeek-V4.1-Flash | V 系列通用 | V4 Flash 通用 |
| deepseek | DeepSeek-V3.2-Speciale | R 系列推理 | 专项推理 Speciale |
| deepseek | DeepSeek-Coder | 代码/数学专项 | 代码 Coder |
| deepseek | DeepSeek-Math | 代码/数学专项 | 数学 Math |
| deepseek | DeepSeek-Coder-V2 | 代码/数学专项 | 代码 Coder |
| deepseek | DeepSeek-Prover-V1.5 | 代码/数学专项 | 形式证明 Prover |
| deepseek | DeepSeek-Prover-V2 | 代码/数学专项 | 形式证明 Prover |
| deepseek | DeepSeek-Math-V2 | 代码/数学专项 | 数学 Math |
| deepseek | DeepSeek-VL | 多模态 VL/Janus/OCR | 视觉理解 VL |
| deepseek | Janus | 多模态 VL/Janus/OCR | 理解与生成 Janus |
| deepseek | DeepSeek-VL2 | 多模态 VL/Janus/OCR | 视觉理解 VL |
| deepseek | Janus-Pro | 多模态 VL/Janus/OCR | 理解与生成 Janus |
| deepseek | DeepSeek-OCR | 多模态 VL/Janus/OCR | 文档理解 OCR |
| deepseek | DeepSeek-OCR 2 | 多模态 VL/Janus/OCR | 文档理解 OCR |
| deepseek | DeepSeek-V4-Flash-Vision-Exp | 多模态 VL/Janus/OCR | V4 Flash 视觉实验 |
| alibaba | Qwen2.5-Max | Qwen 主线 | Qwen Max 旗舰 |
| alibaba | Qwen3-Next | Qwen 主线 | Qwen Next 架构 |
| alibaba | Qwen3-Max | Qwen 主线 | Qwen Max 旗舰 |
| alibaba | Qwen3.6-Plus | Qwen 主线 | Qwen Plus 通用 |
| alibaba | Qwen3.6-35B-A3B | Qwen 主线 | Qwen 中型 MoE |
| alibaba | Qwen3.7-Max | Qwen 主线 | Qwen Max 旗舰 |
| alibaba | Qwen3.8-Max | Qwen 主线 | Qwen Max 旗舰 |
| alibaba | QVQ-72B-Preview | 推理 QwQ/Thinking | 视觉推理 QVQ |
| alibaba | Qwen-VL | 多模态 VL/Omni | 视觉理解 VL |
| alibaba | Qwen2-VL | 多模态 VL/Omni | 视觉理解 VL |
| alibaba | Qwen2.5-VL | 多模态 VL/Omni | 视觉理解 VL |
| alibaba | Qwen2.5-Omni | 多模态 VL/Omni | 全模态 Omni |
| alibaba | Qwen3-Omni | 多模态 VL/Omni | 全模态 Omni |
| alibaba | Qwen3-VL | 多模态 VL/Omni | 视觉理解 VL |
| alibaba | Qwen3.5-Omni | 多模态 VL/Omni | 全模态 Omni |
| alibaba | Qwen3.8-Omni-Flash | 多模态 VL/Omni | 全模态 Omni |
| alibaba | 通义万相 | 万相 Wan/图像生成 | 万相 Wan 图像 |
| alibaba | Wan2.1 | 万相 Wan/图像生成 | 万相 Wan 视频 |
| alibaba | Wan2.2 | 万相 Wan/图像生成 | 万相 Wan 视频 |
| alibaba | Qwen-Image | 万相 Wan/图像生成 | 图像 Qwen-Image |
| alibaba | Wan2.5-Preview | 万相 Wan/图像生成 | 万相 Wan 视频 |
| alibaba | Wan2.6 | 万相 Wan/图像生成 | 万相 Wan 视频 |
| alibaba | Qwen-Image-2.0 | 万相 Wan/图像生成 | 图像 Qwen-Image |
| alibaba | Qwen-Image-2.1 | 万相 Wan/图像生成 | 图像 Qwen-Image 开源 |
| bytedance | UI-TARS | 开源/Agent UI-TARS·OSS | GUI Agent UI-TARS |
| bytedance | UI-TARS-1.5 | 开源/Agent UI-TARS·OSS | GUI Agent UI-TARS |
| bytedance | Seed-OSS-36B | 开源/Agent UI-TARS·OSS | 开源通用 Seed-OSS |
| bytedance | Seedream 5.0 Lite | 图像 Seedream | 图像 Seedream Lite |
| zhipu | GLM-Zero-Preview | 推理与视觉理解 | 文本推理 Zero/Z1 |
| zhipu | GLM-Z1 | 推理与视觉理解 | 文本推理 Zero/Z1 |
| zhipu | GLM-4.1V-Thinking | 推理与视觉理解 | 视觉理解 GLM-V |
| zhipu | GLM-4.5V | 推理与视觉理解 | 视觉理解 GLM-V |
| zhipu | GLM-4.6V | 推理与视觉理解 | 视觉理解 GLM-V |
| zhipu | GLM-5V-Turbo | 推理与视觉理解 | 视觉理解 GLM-V |
| zhipu | GLM-5.3-Flash | 推理与视觉理解 | 高效多模态 GLM Flash |
| zhipu | GLM-Image | CogView 图像生成 | 图像 GLM-Image |
| moonshot | Moonlight-16B-A3B | 开源研究模型 | 开源架构研究 |
| moonshot | Kimi-VL | 开源研究模型 | 视觉理解 Kimi-VL |
| moonshot | Kimi-Audio | 开源研究模型 | 音频 Kimi-Audio |
| moonshot | Kimi Linear | 开源研究模型 | 开源架构研究 |
| baidu | 文心一格 | 图像与视频生成 | 图像生成 |
| baidu | iRAG | 图像与视频生成 | 图像生成 |
| baidu | 百度蒸汽机 MuseSteamer | 图像与视频生成 | 蒸汽机视频生成 |
| baidu | 蒸汽机 2.0 | 图像与视频生成 | 蒸汽机视频生成 |
| tencent | Hunyuan-DiT | 图像与视频生成 | 图像生成 |
| tencent | HunyuanVideo | 图像与视频生成 | 视频生成 |
| tencent | 混元图像 2.0 | 图像与视频生成 | 图像生成 |
| tencent | HunyuanImage 2.1 | 图像与视频生成 | 图像生成 |
| tencent | HunyuanImage 3.0 | 图像与视频生成 | 图像生成 |
| tencent | HunyuanVideo 1.5 | 图像与视频生成 | 视频生成 |
| tencent | Hy Image 3.5 preview | 图像与视频生成 | 图像生成 |
| tencent | Hunyuan3D-1.0 | 3D 与世界模型 | 3D 生成 |
| tencent | Hunyuan3D 2.0 | 3D 与世界模型 | 3D 生成 |
| tencent | 混元3D v2.5 | 3D 与世界模型 | 3D 生成 |
| tencent | HunyuanWorld 1.0 | 3D 与世界模型 | 世界模型 |
| tencent | 混元3D 3.0 | 3D 与世界模型 | 3D 生成 |
| tencent | HunyuanWorld 1.5 | 3D 与世界模型 | 世界模型 |
| tencent | HY-World 2.0 | 3D 与世界模型 | 世界模型 |
| minimax | M3.1-Flash-Preview | abab / M 语言主线 | M Flash 编程 |
| stepfun | Step-1X | 图像与视频生成 | 图像生成 |
| stepfun | Step-Video-T2V | 图像与视频生成 | 视频生成 |
| stepfun | Step-Video-TI2V | 图像与视频生成 | 视频生成 |
| stepfun | Step1X-Edit | 图像与视频生成 | 图像编辑 |
| stepfun | Step-Audio | 语音 | 语音交互 |
| stepfun | Step-Audio 2 mini | 语音 | 语音交互 |
| stepfun | Step-Audio-R1 | 语音 | 语音推理 |

## Every recorded release-date change

These are changes in the repository’s asserted dates; source links are included for targeted re-verification. The audit does not independently certify those dates.
| Company | Original → final identity | Before | After | New explanation / source |
| --- | --- | --- | --- | --- |
| microsoft | MAI-Image-2 → MAI-Image-2 | 2026-04-02 | 2026-03-19 | Playground首发；4月Foundry上线 https://microsoft.ai/news/introducing-mai-image-2/ |
| mistral | Mistral Medium 3.5 → Mistral Medium 3.5 | 2026-04-29 | 2026-04-28 | 开放权重，推理与编程统一 https://docs.mistral.ai/resources/changelogs |
| mistral | Leanstral 1.5 → Leanstral 1.5 | 2026-07-02 | 2026-06-30 | Lean 4形式证明，9月30日退役 https://docs.mistral.ai/resources/changelogs |
| alibaba | Qwen3.8-2.4T-A95B / 27B → Qwen3.8-27B | 2026-08-12 | 2026-08-14 | 27B稠密模型权重开放 https://github.com/QwenLM/Qwen3.8 |
| alibaba | Qwen3.8-Omni-Flash → Qwen3.8-Omni-Flash | 2026-09-18 | 2026-09-17 | 全模态API上线；9月18日发布博客 https://www.alibabacloud.com/help/en/model-studio/newly-released-models |
| alibaba | Wan3.0 → Wan3.0-Video (Beta) | 2026-08-24 | 2026-08-06 | 30秒全模态参考视频，公测API https://www.alibabacloud.com/help/en/model-studio/newly-released-models |
| bytedance | Seedream 5.0 Lite → Seedream 5.0 Lite | 2026-02-24 | 2026-02-13 | 深度思考+联网搜索 https://seed.bytedance.com/en/blog/deeper-thinking-more-accurate-generation-introducing-seedream-5-0-lite |
| zhipu | GLM-5.2 → GLM-5.2 | 2026-06-13 | 2026-06-16 | 1M上下文，MIT开源 https://z.ai/blog/glm-5.2 |
| tencent | Hy Image 3.5 preview → Hy Image 3.5 preview | 2026-09-22 | 2026-09-21 | 官网首次发布；9/22 元宝全量上线 https://hy.tencent.com/ |
| minimax | MiniMax-M2.1 → MiniMax-M2.1 | 2025-12-23 | 2025-12-22 | 多语言编程增强 https://platform.minimax.io/docs/release-notes/models |
| minimax | Music-1.5 → Music-1.5 | 2025-06-20 | 2025-09-11 | 正式版，支持四分钟歌曲 https://platform.minimax.io/docs/release-notes/models |
| stepfun | Step-Audio-R1 → Step-Audio-R1 | 2025-11-27 | 2025-11-19 | 研究公开；11/27 开放权重 https://github.com/stepfun-ai/Step-Audio-R1 |

Music-1.5 special case: the original 2025-06-20 event survives verbatim as Music-1.5 Beta; the existing name Music-1.5 is repurposed for the 2025-09-11 formal event. Wan3.0 special case: the old generic 2026-08-24 row is no longer an independent event; the replacement Beta date is 2026-08-06 and the added Prime date is 2026-08-20.

## Every type change, including children of combined rows

| Company | Old → new identity | Old type | New type |
| --- | --- | --- | --- |
| openai | GPT-6 Sol / Luna → GPT-6 Sol | small | flagship |
| mistral | Codestral Mamba / Mathstral → Mathstral | code | open |
| deepseek | DeepSeek-V4 (Preview) → DeepSeek-V4-Flash-Preview | flagship | open |
| zhipu | GLM-5.3 → GLM-5.3 | open | flagship |
| moonshot | Kimi K3 → Kimi K3 | open | flagship |
| tencent | Hy4 preview → Hy4 preview | flagship | open |
| minimax | Music-3.0 → Music-3.0 | media | open |
| iflytek | 讯飞星火 X2 → 讯飞星火 X2 | flagship | reasoning |
| iflytek | 讯飞星火 X2.5 → 讯飞星火 X2.5 | flagship | reasoning |
| iflytek | 星火 X2.5-4B/1.7B → 星火 X2.5-4B/1.7B | small | open |

## Every explicit end-date change

| Company | Model | Before | After | New note |
| --- | --- | --- | --- | --- |
| amazon | Nova Premier | none | 2026-09-14 | 旗舰复杂任务；2026/9/14 退役 |
| amazon | Nova Sonic | none | 2026-09-14 | 语音到语音；2026/9/14 退役 |
| amazon | Nova Reel | none | 2026-09-30 | 6 秒视频；2026/9/30 退役 |
| mistral | Leanstral 1.5 | none | 2026-09-30 | Lean 4形式证明，9月30日退役 |
| deepseek | DeepSeek-V4-Flash | none | 2026-09-10 | API正式版，Agent能力升级 |

End dates do not remove bars. The new runtime ends each span at the earliest successor, explicit retirement, or as-of date. For Nova Premier / Sonic / Reel, retirement can be later than an already existing successor, so the retirement does not necessarily change the visible span. The clamp fixes the previous precedence behavior where an explicit later end overrode succession.

## Old records newly marked unverified

- xai: Grok 4.20 — Beta 日期待核验;API 3/10 可用
- xai: Grok 4.3 — 早期 Beta 日期待核验
- xai: Grok Imagine 1.0 — 版本发布日期待官方来源核验
- alibaba: Qwen3-Max-Thinking — 模型已核实；1月26日首发日期待核（官方博客显示1月25日）
- alibaba: Qwen3-Coder-Next — 80B-A3B；原2/3日期待核，官方博客2/2
- zhipu: GLM-5 — 744B；原2/11日期待核，国际官方2/12
- zhipu: GLM-5.1 — 3月27日首次上线日期待核；官方日志4月7日发布
- zhipu: GLM-5V-Turbo — 多模态编程模型；4月2日首发日期待核
- baidu: 文心 5.1 Preview — 模型已核实；4月29日首发日期待核（官方4月30日榜单公告）
- minimax: M3.1-Flash-Preview — Code 编程预览；首发日期待核
- stepfun: Step 3.5 Flash — 196B MoE；首发日期待核
- iflytek: 讯飞星火 X2 — 全国产推理；发布日与 API 文档不一致
- iflytek: 讯飞星火 X2.5 — 代码与智能体增强；首发日期待核

These records remain in both runtime data and the default table. New unverified styling lowers opacity to 0.65 and uses a dashed border. Confirmed predecessors no longer end at an unverified successor; additional stacked rows can result. Filters can still dim these records to 0.13 because .bar.dim follows .bar.unverified in CSS.

## GPT Sol / Astra runtime and viewport findings

| Commit | Model | Lane / row within OpenAI | Days / end | Next |
| --- | --- | --- | --- | --- |
| e02ecd6 | GPT-6 Astra | GPT 主线 / 1 of 6 | 25 days / 2026-09-28 | none |
| e02ecd6 | GPT-6 Sol / Luna | 轻量 mini/nano / 5 of 6 | 6 days / 2026-09-28 | none |
| 23c4941 | GPT-6 Sol | GPT Sol / 17 of 25 | 7 days / 2026-09-29 | GPT-6.1 Sol |
| 23c4941 | GPT-6.1 Sol | GPT Sol / 17 of 25 | 1 days / 2026-09-30 | none |
| 23c4941 | GPT-6 Astra | GPT Astra / 23 of 25 | 27 days / 2026-09-30 | none |
| 23c4941 | GPT-6 Luna | GPT Luna / 18 of 25 | 8 days / 2026-09-30 | none |

1. Vertical relocation is the strongest regression: Astra moves from OpenAI row 1 to row 23; Sol goes to row 17. OpenAI grows from 6 rows to 25 rows. The chart retains its own max-height: min(78vh, 1400px) scroller, so users must scroll inside the chart before these lanes appear. Whole-page scrolling may miss them.
2. The unchanged bar rule sets color: transparent whenever width <26px. Width is max(3, days × pixelsPerDay −2). The default remains 2023 view, actually November 1, 2022 → December 3, 2026. This is a 1493-day range.
   - At 1440px viewport (approximate, no scrollbar width): track 1222px; scale 0.818px/day; widths {'Astra (27d)': 20.1, 'Sol (7d)': 3.73, '6.1 Sol (1d)': 3}. Every name is hidden by .tiny, even on desktop. Their bars still exist.
   - At 390px viewport (approximate, no scrollbar width): track 248px; scale 0.166px/day; widths {'Astra (27d)': 3, 'Sol (7d)': 3, '6.1 Sol (1d)': 3}. Every name is hidden by .tiny, even on desktop. Their bars still exist.
3. GPT-6.1 Sol is one day old, so even at the hard maximum zoom of 14px/day its 12px bar remains .tiny. More zoom alone cannot expose its inline name. An alternate list/card or label strategy is required.
4. Persisted localStorage types are restored under the unchanged llm-timeline-v1 key. GPT-6 Sol now belongs to flagship, whereas the old combined Sol/Luna row belonged to small. Someone showing only light models can see Luna but lose Sol from the table/export and see Sol at 13% opacity on the chart. Astra remains flagship throughout, so no type migration explains Astra.
5. Search is literal lowercased substring matching over current model / lane / company names; no legacy aliases or punctuation normalization exist. Exact old composite queries such as GPT-6 Sol / Luna or GPT-5.6 Sol / Terra no longer match any new row. GPT6Sol also fails to match GPT-6 Sol. This can produce zero table rows despite preserved data.
6. Search only scrolls horizontally to the first match. It does not scroll vertically to the new lane, fit/zoom the result, or expand a tiny bar. A correct search for Astra therefore does not bring row 23 into view.
7. CSS mobile rules are unchanged between these commits. At ≤720px, label width becomes 108px and lanes 24px; smaller track width makes label loss much worse. Increased model/lane volume exposes the existing limitations rather than a new mobile display:none rule.
8. No release-range filter removes these records. Initial DATA filtering only rejects unknown companies, missing dates, or dates before 2018. The table uses region/type/query filters, not date-range filters. Region changes hide entire companies; type/query filters merely dim chart bars but fully exclude rows from the table and export.

## Semantic cautions and remaining conflation

- There is no unmapped original model record. Do not re-add the old composite strings as independent models; doing so duplicates represented variants and corrupts counts. Preserve aliases in search or audit metadata if compatibility is desired.
- Record counts are not a normalized count of distinct model artifacts: the update splits some combined model families while retaining other combined names. The following 11 combined names remain, all pre-existing:
  - microsoft: Phi-4-mini / multimodal — Phi 小模型
  - amazon: Nova Micro / Lite / Pro — Nova 主力
  - amazon: Nova 2 Lite / Pro / Omni — Nova 主力
  - mistral: Magistral Small/Medium — 推理 Magistral
  - mistral: Ministral 3B/8B — 端侧 Ministral
  - mistral: Ministral 3 (3B/8B/14B) — 端侧 Ministral
  - mistral: Devstral Medium / Small 1.1 — 编程 Agent Devstral
  - bytedance: 豆包大模型 (Doubao-pro/lite) — 豆包/Seed 通用
  - bytedance: 豆包视频生成 PixelDance/Seaweed — 视频 Seedance
  - baidu: ERNIE Speed/Lite/Tiny — 开源与轻量
  - iflytek: 星火 X2.5-4B/1.7B — 开源与端侧
- Music-1.5 and Nova Act distinguish release stages (beta / GA); those are useful milestones but should not automatically be interpreted as distinct underlying models.
- “Latest” now means latest in an isolated lane. Splitting a formerly broad lane can make an older terminal record appear ongoing because successors moved to new lanes. Examples include GPT-5.5 at the end of GPT 主线 and DeepSeek-V3.2 at the end of V 系列通用. This does not delete models, but family-transition semantics need deliberate handling if the UI implies overall company flagship succession.
- Date uncertainty is sometimes treated as uncertainty about succession: old GLM-5 / GLM-5.1 and Qwen3-Max-Thinking records are retained but no longer truncate verified predecessors. This is explicit in the update, yet can display overlapping latest-looking bars.
- Existing source labels say 官方来源 for every supplied URL, including an arXiv paper, government page, LinkedIn post, or company repository test. These may be appropriate evidence, but the UI label alone is not evidence of primary model-release verification.
- Small descriptive details were revised, e.g. Astra’s old 1.05M context remark and GPT Image 2.5’s Sketch remark are absent from the new notes. These are note/content edits, not deleted model rows.

## Recommended regression coverage / acceptance evidence

- Assert that every original record maps to one or more current identities, and that required GPT-6 Astra / GPT-6 Sol / GPT-6.1 Sol records each render and can be discovered in the normal UI.
- Cover initial desktop and mobile chart, search for Astra and punctuation-free GPT6Sol, legacy composite queries, persisted small-only filters, and latest one-day releases. Verify visual name discoverability, not only .bar counts.
- Current tests exercise lifecycle calculation and export uncertainty; they do not guard against vertical relocation, .tiny labels, legacy-name search, stored filter migration, or full inventory continuity.
- This audit executed both revisions’ actual model code and found 484 and 579 runtime items respectively, exactly matching all JSON rows. Browser verification of the subsequent fix is documented separately.

## Companion file

- [Exhaustive original-record mapping](record-audit-first-update.json), including before/after names, dates, lanes and sources
