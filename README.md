# 大模型编年图

一张可交互的 AI 大模型发布时间线：横轴是时间（2018 年至今），纵轴是 18 家公司。每家公司按产品系列拆成多条轨道，每个色块是一个模型，从发布那天开始，到同系列下一代发布为止。

- 缩放（按钮或 Ctrl + 滚轮），三个预设视图：全景 / 2023 起 / 近 18 个月
- 按地区（海外 / 中国）、模型类型、关键词筛选
- 悬停查看发布日期、接替者、在位天数和备注
- 导出完整大图（PNG 或 SVG），导出时沿用当前的筛选条件
- 底部有全部模型的表格视图、可点击官方来源和核验状态
- 支持浅色 / 深色主题和手机屏幕

在线查看：**https://wenhaoquestion.github.io/AI-Model-Timeline/**

<a href="https://wenhaoquestion.github.io/AI-Model-Timeline/">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/screenshot-dark.png">
    <img alt="大模型编年图截图：横轴为 2023–2026 年时间轴，纵轴为 OpenAI、Anthropic、Google 等公司及其模型系列，每个色块是一个模型的在位时长" src="docs/screenshot-light.png">
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
| `d` | 发布日期 `YYYY-MM-DD`（也可以只写 `YYYY-MM`） |
| `t` | 类型：`flagship` 旗舰 / `reasoning` 推理 / `small` 轻量 / `open` 开源权重 / `media` 图像视频语音 / `code` 代码专项 |
| `n` | 备注，建议 25 字以内 |
| `end` | 可选。官方明确的停止服务日期；色块止于接替、停止服务、核验截至日三者中最早者 |
| `s` | 官方发布、官方模型卡或官方更新日志的 HTTPS 链接 |
| `verification` | 可选：`unverified` 表示存在模型/日期等未能核验的细节，保留记录并明确标注 |

同一 `lane` 只放真正的代际系列。并行的旗舰/轻量、图片/视频、语音识别/合成应分开；同日发布的兄弟模型会自动分行。待核验记录不会截断已核验版本。

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

本次核验截至 **2026-09-30**，重点复核 2026 年发布、补齐近期遗漏，并为已核验记录保存官方链接。包含 9 月 28 日的 Claude Sonnet 5.5、9 月 29 日的 GPT-6.1 Sol，以及各公司遗漏的并行模型系列。

日期按首次正式公开发布或开放使用计；研究预览、受限发布、仅公布而尚未开放的情况在备注中说明。后续 API 上线或博客更新不重复算作新模型。不同地区的日期差异需以链接中的原始发布记录为准。

- 附来源且无 `unverified`：本次对照官方发布/模型卡/更新日志核验
- `unverified`：保留原记录或月级日期，并标明具体不确定性；不代表已确认发布
- 无来源的早期历史记录：沿用旧数据，页面明确显示“待补来源”，不宣称逐条核验

构建会拒绝截至日之后的发布、无效日期、重复模型名、不安全的来源链接，以及既无来源也无待核验标记的 2026 年及以后记录。色块表示本图中的系列版本跨度，不等同于在售、API 可用或停止维护状态。

依赖：Python 3.8+（仅构建时需要，只用标准库）。
