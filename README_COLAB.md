# 🚀 在 Google Colab 中试用 CopyFlow

不想本地安装？在浏览器中即刻体验 CopyFlow 的完整功能！

## 🎯 一键启动

点击下方按钮，在 Google Colab 中打开交互式 Notebook：

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AIPMAndy/copyflow/blob/main/CopyFlow_Demo.ipynb)

## ⚡ 快速体验流程

**总耗时**: 约 5 分钟

1. **安装依赖** (1 分钟)
   - 自动克隆仓库
   - 安装所需 Python 包

2. **配置 API Keys** (1 分钟)
   - 输入 OpenAI API Key
   - 输入 PonyFlash API Key
   - 💡 首次试用可申请免费额度

3. **运行生成** (2-3 分钟)
   - 修改主题和数量
   - 执行生成命令
   - 实时查看进度

4. **查看结果** (1 分钟)
   - 预览生成的文案
   - 查看 AI 配图
   - 下载完整内容包

## 📋 需要准备的

### OpenAI API Key
- 🔗 获取地址: https://platform.openai.com/api-keys
- 💰 费用: 约 $0.50-1.00 生成 10 套内容
- 🆓 新用户通常有 $5-18 免费额度

### PonyFlash API Key
- 🔗 获取地址: https://console.ponyflash.com
- 💰 费用: 约 ¥0.5-1.0 生成 10 张图
- 🆓 新用户有免费额度

## ✨ 功能特性

在 Colab 中可以完整体验：

- ✅ 多风格文案生成（3-10 套）
- ✅ AI 智能配图
- ✅ 审核文档生成
- ✅ 结果打包下载
- ✅ 实时进度显示

## 🆚 Colab vs 本地安装

| 特性 | Google Colab | 本地安装 |
|-----|-------------|---------|
| 🚀 启动速度 | 快（无需配置环境） | 需要安装依赖 |
| 💻 系统要求 | 仅需浏览器 | Python 3.8+ |
| 🔄 数据持久化 | 需手动下载 | 自动保存本地 |
| ⚡ 运行速度 | 中等（云端资源） | 快（本地资源） |
| 🔧 自定义 | 有限 | 完全自由 |
| 💰 成本 | 免费（Google） | 仅 API 费用 |

## 🎓 适用场景

### 适合在 Colab 使用
- ✅ 首次试用，快速体验功能
- ✅ 临时需求，偶尔生成内容
- ✅ 没有 Python 环境的用户
- ✅ 在外出差，需要应急使用

### 推荐本地安装
- ✅ 日常高频使用
- ✅ 需要批量生成
- ✅ 自定义风格和配置
- ✅ 团队协作使用

## 🚀 本地安装

体验满意后，推荐安装到本地获得更好性能：

### 方式 1: 自动安装脚本（推荐）

```bash
git clone https://github.com/AIPMAndy/copyflow.git
cd copyflow
./install.sh
```

### 方式 2: 手动安装

```bash
git clone https://github.com/AIPMAndy/copyflow.git
cd copyflow
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# 编辑 .env 填入 API Keys
python copyflow.py run --topic "你的主题"
```

### 方式 3: Docker（最简单）

```bash
git clone https://github.com/AIPMAndy/copyflow.git
cd copyflow
# 编辑 docker-compose.yml 填入 API Keys
docker-compose up -d
```

## 📚 更多资源

- [📖 完整文档](../README.md)
- [❓ 常见问题](docs/FAQ.md)
- [🎯 快速开始](QUICKSTART.md)
- [🔧 高级配置](docs/ADVANCED.md)

## 💬 获取帮助

遇到问题？我们很乐意帮助：

- 🐛 [报告 Bug](https://github.com/AIPMAndy/copyflow/issues/new?template=bug_report.yml)
- 💡 [功能建议](https://github.com/AIPMAndy/copyflow/issues/new?template=feature_request.yml)
- 💬 [社区讨论](https://github.com/AIPMAndy/copyflow/discussions)

## ⭐ 觉得有用？

如果 CopyFlow 帮到了你：

- ⭐ 给项目一个 Star
- 📣 分享给更多朋友
- 🤝 贡献你的代码或想法

---

**准备好了吗？** [👉 立即在 Colab 中试用](https://colab.research.google.com/github/AIPMAndy/copyflow/blob/main/CopyFlow_Demo.ipynb)
