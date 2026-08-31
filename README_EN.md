<div align="center">

# 🚀 CopyFlow - Content Production Automation Engine

### One Topic → 10 Styles of Copy + AI Images + Ready-to-Publish Materials in 3 Minutes

**Designed for Content Operations Teams**: Save 80% repetitive work, focus on creativity and strategy

[![License](https://img.shields.io/badge/License-PostSkill%201.0.0-blue.svg)](./LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![CI](https://img.shields.io/github/actions/workflow/status/AIPMAndy/copyflow/ci.yml?branch=main&label=CI)](https://github.com/AIPMAndy/copyflow/actions)
[![codecov](https://codecov.io/gh/AIPMAndy/copyflow/branch/main/graph/badge.svg)](https://codecov.io/gh/AIPMAndy/copyflow)

[简体中文](./README.md) | **English**

</div>

---

## 💡 What Problem Does It Solve

Have you ever encountered:

- ❌ **Writing the same topic 10 times in different styles** (professional, casual, storytelling...)
- ❌ **Finding images, designing, or generating AI images for each copy separately** (repetitive work)
- ❌ **Copy-pasting everywhere during team collaboration** (inefficient)
- ❌ **Manually adapting formats for multiple platforms** (error-prone)

CopyFlow automates this entire pipeline:

```bash
python copyflow.py run --topic "How AI is Changing Content Creation"

# ✅ After 3 minutes, you get:
#    - 10 copies in different styles (data-driven, storytelling, opinion-based...)
#    - 10 AI-generated images
#    - 1 Markdown document with organized text and images (ready for review/editing)
```

**Real Example**: [View complete output sample](./examples/ai-awakening-output.md)

---

## ✨ Core Capabilities

### 1️⃣ Multi-Style Copy Generation

One topic, automatically generates 10 styles for different scenarios:

| Style | Use Case | Example |
|-------|----------|---------|
| 📊 Data-Driven | B2B/Professional | "3 data points tell you..." |
| 🎭 Storytelling | Brand/Emotional | "After 30 days with AI, I..." |
| 💡 Opinion-Based | KOL/Thought Leader | "Why AI is..." |
| 🔥 Trending | Viral Content | "Behind ChatGPT's explosion..." |
| 📚 Educational | Education/Explainer | "Understanding AI in one article..." |
| 🎨 Creative | Creative/Entertainment | "If AI could dream..." |
| 💼 Business Professional | Enterprise/Official | "How enterprises leverage..." |
| 🌟 Inspirational | Personal Growth | "30 minutes daily, after a year..." |
| 🤔 Critical Thinking | Deep Content | "Do we really need..." |
| 😄 Casual & Humorous | Entertainment/Social | "AI learned to..." |

### 2️⃣ AI Image Generation

- Powered by PonyFlash SDK for automatic image generation
- Supports multiple styles (realistic, illustration, 3D, concept art)
- Automatically matches copy theme and mood

### 3️⃣ Material Organization

- Automatically generates Markdown documents with text-image alignment
- Supports export to Feishu Docs (team collaboration)
- Ready for review/editing/annotation

### 4️⃣ Automated Publishing (In Development)

- GitHub Actions scheduled execution
- Supports WeChat Official Account/Xiaohongshu/Zhihu (API skeleton completed)
- Publishing result collection and dashboard (planned)

---

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/AIPMAndy/copyflow.git
cd copyflow
pip install -r requirements.txt
playwright install chromium
```

### Configure API Keys

```bash
# Set OpenAI API Key (for copy generation)
export OPENAI_API_KEY="your-key-here"

# Set PonyFlash API Key (for image generation)
export PONYFLASH_API_KEY="your-key-here"
```

### Generate Your First Content

```bash
# One-click generation of complete content package (copy + images + document)
python copyflow.py run --topic "How AI is Changing Content Creation"

# View results
ls ./output/
# ├── copies.json          # 10 copies
# ├── images/              # Images
# └── content-review.md    # Organized review document
```

### Step-by-Step Execution (Optional)

```bash
# Generate copy only
python copyflow.py generate --topic "Your Topic" --output ./output

# Generate images only
python copyflow.py generate-images --config ./output/copies.json --output ./output/images

# Generate reviewable Markdown document
python copyflow.py create-doc --content ./output/copies.json --images ./output/images --output ./output
```

---

## 📊 Real Case Study

**Input Topic**: AI Awakening Community

**Output Results**:

<table>
<tr>
<td width="50%">

**Practical Copy**

Title: AI Awakening: 3 Steps to Start Your Growth Journey

Want to learn AI but don't know where to start?

AI Awakening helps you:
- ❶ Break through information anxiety, focus on core skills
- ❷ Project-driven practice, learn by doing
- ❸ Connect with like-minded peers, no more solo struggle

30 days, from AI beginner to problem solver.

</td>
<td width="50%">

**Storytelling Copy**

Title: After 30 Days with AI Awakening, I Said Goodbye to Inefficient Overtime

Used to work overtime until midnight with little results.

After joining AI Awakening, learned to use AI for information filtering, content drafting, and decision support.

Now finish daily work by 10 AM, spend afternoons learning and thinking.

Doubled efficiency, finally feel in control of life.

</td>
</tr>
</table>

**Complete Example**: [examples/ai-awakening-output.md](./examples/ai-awakening-output.md)

**Time Cost**: ~3 minutes (depends on AI API speed)

---

## 🎯 Who Is It For

| User Type | Use Case | Core Value |
|-----------|----------|------------|
| 📝 **Content Operations Teams** | Batch content production, efficiency boost | One person does the work of 10 |
| 👤 **Individual Creators** | Save time on image sourcing/formatting | Focus on creation, not repetitive work |
| 🤖 **AI Workflow Enthusiasts** | Customize your own content engine | Extensible automation framework |
| 📱 **Multi-Platform Media** | One content set for multiple platforms | Reduce multi-platform operation costs |
| 🏢 **Enterprise Brands** | Rapidly produce multi-style marketing materials | Improve marketing response speed |

---

## 📂 Project Structure

```text
copyflow/
├── copyflow.py                   # CLI entry point
├── scripts/
│   ├── copy_generator.py         # Multi-style copy generation
│   ├── image_generator.py        # AI image generation
│   ├── feishu_doc_creator.py     # Feishu document generation
│   └── publisher.py              # Platform publisher (skeleton)
├── styles/                       # Copy style templates
├── tests/                        # Unit tests
├── examples/                     # Example outputs
│   └── ai-awakening-output.md    # Real case
├── .github/workflows/            # Automation workflows
│   ├── auto-publish.yml          # Auto-publish
│   └── ci.yml                    # CI/CD
└── README.md
```

---

## 🛣️ Roadmap

### ✅ Completed
- [x] Multi-style copy generation (10 styles)
- [x] AI image generation (PonyFlash)
- [x] Automatic material organization
- [x] GitHub Actions automation pipeline
- [x] Feishu document generation

### 🚧 In Development
- [ ] Complete platform publisher (WeChat/Xiaohongshu/Zhihu)
- [ ] Platform account management
- [ ] Publishing result collection and dashboard

### 📋 Planned
- [ ] More platform adapters (Douyin/Bilibili/Twitter)
- [ ] Content strategy layer (topic recommendation/trending tracking)
- [ ] Enhanced copy template library
- [ ] Image generation retry strategy
- [ ] Material review workflow optimization

---

## 🤝 Contributing

Contributions welcome:

- 🔌 **Platform Adapters**: Integrate more publishing platforms
- 📝 **Copy Templates**: Add more style templates
- 🎨 **Image Strategy**: Optimize image generation logic
- 🔄 **Workflow Optimization**: Improve automation processes
- 📚 **Documentation**: Add more use cases

See [CONTRIBUTING.md](./CONTRIBUTING.md)

---

## 🌟 Why Choose CopyFlow

### vs. Pure AI Copywriting Tools
- ✅ Not just copy generation, but a **complete content production pipeline**
- ✅ Automatic image generation + material organization + publishing automation

### vs. Manual Operations
- ✅ Save **80% repetitive work**
- ✅ Generate 10 content sets in 3 minutes from one topic

### vs. Commercial SaaS
- ✅ **Open source and free**, customizable
- ✅ Data stays local, privacy controlled
- ✅ Can be customized into your own content engine

---

## 📄 License

PostSkill License 1.0.0 (based on Apache 2.0 with improvements)

**About PostSkill**: CopyFlow is a core component of the [PostSkill](https://github.com/AIPMAndy/postskill) content production toolchain. PostSkill is dedicated to building complete AI-driven content production solutions.

**License Highlights**:
- ✅ Free for personal and internal enterprise use
- ✅ Free to modify for your own needs
- ⚠️ SaaS services prohibited without authorization
- ⚠️ Must retain PostSkill brand identifiers

See [LICENSE](./LICENSE) for details

---

## ⭐ If This Project Helps You

1. Give a **Star** ⭐ to support
2. Open an **Issue** 💬 to share your use case
3. Submit a **PR** 🔧 to contribute improvements

**Transform content production from manual workshop to automated factory.**

---

<div align="center">

Made with ❤️ by [Andy | AI Chief](https://github.com/AIPMAndy)

[GitHub](https://github.com/AIPMAndy/copyflow) • [Issues](https://github.com/AIPMAndy/copyflow/issues) • [Discussions](https://github.com/AIPMAndy/copyflow/discussions)

</div>
