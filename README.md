<div align="center">

# 🚀 CopyFlow - 内容生产自动化引擎

### 一个主题 → 10 种风格文案 + AI 配图 + 可发布素材，3 分钟搞定

**为内容运营团队设计**：省下 80% 重复劳动，专注创意和策略

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](./LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![CI](https://img.shields.io/github/actions/workflow/status/AIPMAndy/copyflow/ci.yml?branch=main&label=CI)](https://github.com/AIPMAndy/copyflow/actions)

**简体中文** | [English](./README_EN.md)

</div>

---

## 💡 解决什么问题

你是否遇到过：

- ❌ **一个选题要写 10 遍不同风格的文案**（专业版、轻松版、故事版...）
- ❌ **每套文案要单独找图、设计、AI 出图**（重复劳动）
- ❌ **团队协作时复制粘贴到处飞**（效率低下）
- ❌ **发布到多平台要手动适配格式**（容易出错）

CopyFlow 把这些串成一条自动化流水线：

```bash
python copyflow.py run --topic "AI 如何改变内容创作"

# ✅ 3 分钟后得到：
#    - 10 套不同风格的文案（数据型/故事型/观点型...）
#    - 10 张 AI 生成的配图
#    - 1 份图文整理好的 Markdown 文档（可直接审核/修改）
```

**真实案例**：[查看完整输出示例](./examples/ai-awakening-output.md)

---

## ⚡ 效率对比

### 手动操作 vs CopyFlow

| 任务 | 手动操作 | CopyFlow | 节省时间 |
|------|---------|----------|---------|
| 写 10 套不同风格文案 | 2 小时 | 2 分钟 | 98% ⬇️ |
| 找图/AI 出图 | 1 小时 | 1 分钟 | 98% ⬇️ |
| 整理排版/审核文档 | 30 分钟 | 自动生成 | 100% ⬇️ |
| **总计** | **3.5 小时** | **3 分钟** | **效率提升 70 倍** |

**真实数据**：Andy 使用 CopyFlow 30 天，从每天写内容 5 小时 → 15 分钟，省下 4.75 小时/天 = 142 小时/月。

### CopyFlow vs 其他方案

| 对比项 | ChatGPT | 商业 SaaS | **CopyFlow** |
|--------|---------|-----------|-------------|
| 多风格文案 | ⚠️ 需要手动写 10 次 Prompt | ✅ 有模板 | ✅ 一键 10 种风格 |
| AI 配图 | ❌ 需要单独用 MidJourney | ⚠️ 有限制/收费 | ✅ 自动生成 |
| 素材整理 | ❌ 需要手动复制粘贴 | ⚠️ 平台锁定 | ✅ Markdown 文档 |
| 自动化发布 | ❌ 不支持 | ⚠️ 平台限制 | ✅ 可扩展 |
| 数据隐私 | ⚠️ 上传到平台 | ⚠️ 上传到平台 | ✅ 本地运行 |
| 成本 | 💰 API 费用 | 💰 $50-200/月 | ✅ 开源免费 |
| 可定制性 | ❌ 不能改 | ❌ 不能改 | ✅ 完全开源 |

---

## ✨ 核心能力

### 1️⃣ 多风格文案生成

一个主题，自动生成 10 种风格，适配不同场景：

| 风格 | 适用场景 | 示例 |
|------|---------|------|
| 📊 数据驱动型 | B 端/专业内容 | "3 个数据告诉你..." |
| 🎭 故事叙述型 | 品牌/情感内容 | "接触 AI 30 天，我告别了..." |
| 💡 观点输出型 | KOL/思想领袖 | "为什么说 AI 是..." |
| 🔥 热点追踪型 | 蹭流量 | "ChatGPT 爆火背后..." |
| 📚 知识科普型 | 教育/科普 | "一文读懂..." |
| 🎨 创意脑洞型 | 创意/娱乐 | "如果 AI 会做梦..." |
| 💼 商务专业型 | 企业/官方 | "企业如何利用..." |
| 🌟 励志鸡汤型 | 个人成长 | "每天 30 分钟，一年后..." |
| 🤔 反思质疑型 | 深度内容 | "我们真的需要..." |
| 😄 轻松幽默型 | 娱乐/社交 | "AI 学会了..." |

### 2️⃣ AI 配图生成

- 基于 PonyFlash SDK 自动生成配图
- 支持多种风格（写实/插画/3D/概念艺术）
- 自动匹配文案主题和情绪

### 3️⃣ 素材整理

- 自动生成图文对照的 Markdown 文档
- 支持导出到飞书文档（团队协作）
- 可直接审核/修改/批注

### 4️⃣ 自动化发布（开发中）

- GitHub Actions 定时执行
- 支持公众号/小红书/知乎（接口骨架已完成）
- 发布结果回收与数据看板（规划中）

---

## 🚀 快速开始

### 安装

```bash
git clone https://github.com/AIPMAndy/copyflow.git
cd copyflow
pip install -r requirements.txt
playwright install chromium
```

### 配置 API Key

```bash
# 设置 OpenAI API Key（用于文案生成）
export OPENAI_API_KEY="your-key-here"

# 设置 PonyFlash API Key（用于图片生成）
export PONYFLASH_API_KEY="your-key-here"
```

### 生成第一套内容

```bash
# 一键生成完整内容包（文案 + 配图 + 文档）
python copyflow.py run --topic "AI 如何改变内容创作"

# 查看结果
ls ./output/
# ├── copies.json          # 10 套文案
# ├── images/              # 配图
# └── content-review.md    # 图文整理后的审核文档
```

### 分步执行（可选）

```bash
# 只生成文案
python copyflow.py generate --topic "你的主题" --output ./output

# 只生成配图
python copyflow.py generate-images --config ./output/copies.json --output ./output/images

# 生成可审核的 Markdown 文档
python copyflow.py create-doc --content ./output/copies.json --images ./output/images --output ./output
```

---

## 📊 真实案例

**输入主题**：AI 醒觉社

**输出结果**：

<table>
<tr>
<td width="50%">

**干货型文案**

标题：AI醒觉社：3步开启你的成长之路

想学AI但不知从何开始？

AI醒觉社帮你：
- ❶ 破除信息焦虑，聚焦核心技能
- ❷ 实战项目驱动，边做边学
- ❸ 同频伙伴同行，告别单打独斗

30天，从AI小白到能独立解决问题。

</td>
<td width="50%">

**故事型文案**

标题：接触AI醒觉社30天，我告别了低效加班

以前每天加班到深夜，却做不出成绩。

接触AI醒觉社后，学会了用AI做信息筛选、内容初稿、决策辅助。

现在上午10点完成全天工作，下午用来学习和思考。

效率翻倍，生活终于有掌控感。

</td>
</tr>
</table>

**完整示例**：[examples/ai-awakening-output.md](./examples/ai-awakening-output.md)

**耗时**：约 3 分钟（取决于 AI 接口速度）

---

## 🎯 适合谁

| 用户类型 | 使用场景 | 核心价值 |
|---------|---------|---------|
| 📝 **内容运营团队** | 批量生产内容，提升效率 | 一个人干 10 个人的活 |
| 👤 **个人创作者** | 省下找图/排版时间 | 专注创作，不做重复劳动 |
| 🤖 **AI 工作流玩家** | 改造成自己的内容引擎 | 可扩展的自动化框架 |
| 📱 **自媒体矩阵** | 一套内容适配多平台 | 降低多平台运营成本 |
| 🏢 **企业品牌** | 快速产出多风格营销素材 | 提升营销响应速度 |

---

## 📂 项目结构

```text
copyflow/
├── copyflow.py                   # CLI 主入口
├── scripts/
│   ├── copy_generator.py         # 多风格文案生成
│   ├── image_generator.py        # AI 配图生成
│   ├── feishu_doc_creator.py     # 飞书文档生成
│   └── publisher.py              # 平台发布器（骨架）
├── styles/                       # 文案风格模板
├── tests/                        # 单元测试
├── examples/                     # 示例输出
│   └── ai-awakening-output.md    # 真实案例
├── .github/workflows/            # 自动化工作流
│   ├── auto-publish.yml          # 自动发布
│   └── ci.yml                    # CI/CD
└── README.md
```

---

## 🛣️ Roadmap

### ✅ 已完成
- [x] 多风格文案生成（10 种风格）
- [x] AI 配图生成（PonyFlash）
- [x] 素材文档自动整理
- [x] GitHub Actions 自动化链路
- [x] 飞书文档生成

### 🚧 开发中
- [ ] 完整平台发布器（公众号/小红书/知乎）
- [ ] 平台账号管理
- [ ] 发布结果回收与看板

### 📋 规划中
- [ ] 更多平台适配（抖音/B 站/Twitter）
- [ ] 内容策略层（选题推荐/热点追踪）
- [ ] 更强的文案模板库
- [ ] 图片生成重试策略
- [ ] 素材审核流程优化

---

## 🤝 贡献

欢迎贡献：

- 🔌 **平台适配器**：接入更多发布平台
- 📝 **文案模板**：补充更多风格模板
- 🎨 **配图策略**：优化图片生成逻辑
- 🔄 **工作流优化**：改进自动化流程
- 📚 **文档完善**：补充使用案例

详见 [CONTRIBUTING.md](./CONTRIBUTING.md)

---

## 🌟 为什么选择 CopyFlow

### vs. 纯 AI 文案工具
- ✅ 不只是生成文案，而是**完整的内容生产流水线**
- ✅ 自动配图 + 素材整理 + 发布自动化

### vs. 手动操作
- ✅ 省下 **80% 重复劳动**
- ✅ 一个主题 3 分钟生成 10 套内容

### vs. 商业 SaaS
- ✅ **开源免费**，可自定义
- ✅ 数据在本地，隐私可控
- ✅ 可改造成自己的内容引擎

---

## 📄 License

Apache-2.0

---

## ⭐ 如果这个项目对你有帮助

1. 给个 **Star** ⭐ 支持一下
2. 提个 **Issue** 💬 说说你的使用场景
3. 提个 **PR** 🔧 贡献你的改进

**让内容生产从手工作坊，变成自动化工厂。**

---

<div align="center">

Made with ❤️ by [Andy | AI酋长](https://github.com/AIPMAndy)

[GitHub](https://github.com/AIPMAndy/copyflow) • [Issues](https://github.com/AIPMAndy/copyflow/issues) • [Discussions](https://github.com/AIPMAndy/copyflow/discussions)

</div>
