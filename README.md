# 大模型编年图

一张可交互的 AI 大模型发布时间线：横轴是时间（2018 年至今），纵轴是 33 家公司。每家公司按产品系列拆成多条轨道，每个色块是一条模型或命名版本记录，从公开日期开始，到同系列下一代发布为止。名称不等于独立训练模型；API 别名、公告及正式开放里程碑另行说明。

- 缩放（按钮或 Ctrl + 滚轮），三个预设视图：全景 / 2023 起 / 近 18 个月
- 按地区（海外 / 中国）、模型类型、关键词筛选；支持忽略空格、连字符的搜索与旧名称别名
- 短时长和截至日当天发布的模型仍显示完整名称，标签重叠时自动分行
- 悬停、键盘聚焦或点击查看发布日期、接替者、在位天数和备注
- 导出完整大图（PNG 或 SVG），导出时沿用当前的筛选条件
- 底部有全部模型表格、日期待核验目录、官方来源与逐公司核验进度
- 支持浅色 / 深色主题和手机屏幕

在线查看：**https://wenhaoquestion.github.io/AI-Model-Timeline/**

<a href="https://wenhaoquestion.github.io/AI-Model-Timeline/">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/screenshot-dark.png">
    <img alt="历史版本示例截图（当前数据以在线页面为准）：横轴为 2023–2026 年时间轴，纵轴为 OpenAI、Anthropic、Google 等公司及其模型系列，每个色块是一个模型的在位时长" src="docs/screenshot-light.png">
  </picture>
</a>

## 使用

直接用浏览器打开 `dist/index.html` 即可，不需要服务器。页面只从 Google Fonts 加载字体，离线时会退回系统字体。

## 部署

推送到 `main` 分支后，GitHub Actions（`.github/workflows/pages.yml`）会运行 `build.py` 校验数据、生成页面，并发布到 GitHub Pages。数据有错误时构建会失败，线上页面保持上一个版本。所以在 GitHub 网页上直接改 `data/*.json` 也能自动更新网站。

## 目录结构

```
ai-model-timeline/
├── build.py            # 校验数据并生成 dist/index.html
├── site.json           # 数据截至日期 asOf
├── src/template.html   # 页面模板（样式、交互、导出逻辑）
├── data/
│   ├── companies.json  # 公司列表，顺序即页面上的行顺序
│   ├── openai.json     # 每家公司一个文件，文件名 = companies.json 里的 key
│   └── ...
└── dist/index.html     # 生成的单文件页面
```

## 修改数据

每个公司文件是一个数组，每条记录一个模型：

```json
{"lane": "GPT 主线", "m": "GPT-4o", "d": "2024-05-13", "t": "flagship", "n": "原生多模态", "s": "https://openai.com/index/hello-gpt-4o/"}
```

| 字段 | 含义 |
|---|---|
| `lane` | 所属系列（同一系列的模型画在同一条轨道上，前后相接） |
| `m` | 模型名 |
| `d` | 发布日期 `YYYY-MM-DD`；只有月级证据时写 `YYYY-MM` 并标记待核验，未知时写 `null` |
| `t` | 类型：`flagship` 旗舰 / `reasoning` 推理 / `small` 轻量 / `open` 开源权重 / `media` 图像视频语音 / `code` 代码专项 / `specialized` 嵌入安全等专项 |
| `n` | 备注，建议 25 字以内 |
| `end` | 可选。官方明确的停止服务日期；色块止于接替、停止服务、核验截至日三者中最早者 |
| `s` | 官方发布、官方模型卡或官方更新日志的 HTTPS 链接 |
| `verification` | 可选：`unverified` 表示存在模型/日期等未能核验的细节，保留记录并明确标注 |
| `aliases` | 可选：旧名称或官方 API 别名数组，维持旧名称可搜索 |
| `events` | 可选：后续公开预览、API 开放或 GA 里程碑，每条含 `d`、`n`、`s` |

同一 `lane` 只放真正的代际系列。并行的旗舰/轻量、图片/视频、语音识别/合成应分开；同日发布的兄弟模型会自动分行。待核验记录不会截断已核验版本。月级或未知日期的记录保留在列表与日期待核验目录，不将推测的某一天放到时间轴；未知日期必须附官方身份来源。

新增公司：在 `data/companies.json` 里加一行（`key`、`name`、`sub`、`region`、`china`），再新建 `data/<key>.json`。

改完后运行：

```bash
python3 build.py            # 校验并生成 dist/index.html
python3 build.py --check    # 只校验
python3 -m unittest discover -s tests -v  # 校验器回归测试
node tests/test_timeline.js              # 时间轴接替与导出回归测试
```

更新数据后记得把 `site.json` 里的 `asOf` 改成新的日期。页面上的“截至”红线、时间轴的右端和“数据截至”都以它为准，不会随浏览器日期自动前移。

## 数据来源与说明

本轮来源核对的收录截止日为 **2026-09-29**，最终复核于 **2026-09-30**。覆盖原有 18 家公司并新增 15 家：AI2、AI21 Labs、Apple、Black Forest Labs、Cohere、ElevenLabs、IBM、Kuaishou、Liquid AI、Luma AI、NVIDIA、Perplexity、Runway、Stability AI、TII。

[逐公司范围、修正与验证结果](docs/audit-2026-09-29.md)列明各公司记录数、已核验来源、日期不确定项与研究边界。收录包括公开命名家族、并行型号、明确命名的版本或快照；不等于独立训练模型数，也不宣称全球所有公司、历史研究模型、量化及内部型号均无遗漏。

[旧记录映射](docs/record-audit-first-update.md)及回归测试保证最初 484 条记录和第一轮更新的 579 条记录均可按原名称或别名找到。GPT-6 Sol、GPT-6 Astra 和 GPT-6.1 Sol 已核对并保留，短色块及搜索定位问题也已修复。
日期按可证实的首次公开事件计，公告、研究发布、预览、API 上线、GA 和开放权重需按来源区分；受限或尚未开放的情况在备注中说明。后续 API 上线或博客更新不重复算作新模型。不同地区的日期差异需以链接中的原始发布记录为准。

- 附来源且无 `unverified`：本次对照官方发布/模型卡/更新日志核验
- `unverified`：保留原记录或月级日期，并标明具体不确定性；不代表已确认发布
- 无来源的早期历史记录：沿用旧数据，页面明确显示“待补来源”，不宣称逐条核验

构建会拒绝截至日之后的发布、无效日期、重复模型名、不安全的来源链接，以及既无来源也无待核验标记的 2026 年及以后记录。色块表示本图中的系列版本跨度，不等同于在售、API 可用或停止维护状态。

导出全量 1,500 余条记录时建议使用 SVG：它保留可放大的文字。PNG 会为避开浏览器画布大小上限自动缩小，完整大图中的文字可能很小；可先筛选再导出。

依赖：Python 3.8+（仅构建时需要，只用标准库）。
