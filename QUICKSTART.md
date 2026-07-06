# 🚀 CopyFlow Quick Start Guide

Get started with CopyFlow in under 3 minutes!

## Prerequisites

- Python 3.10 or higher
- OpenAI API Key (for text generation)
- PonyFlash API Key (for image generation, optional)

## Step 1: Install

```bash
# Clone the repository
git clone https://github.com/AIPMAndy/copyflow.git
cd copyflow

# Install dependencies
pip install -r requirements.txt
```

## Step 2: Configure

Set your API keys as environment variables:

```bash
# Required: OpenAI API Key
export OPENAI_API_KEY="your_openai_api_key_here"

# Optional: PonyFlash API Key (for image generation)
export PONYFLASH_API_KEY="your_ponyflash_api_key_here"
```

**💡 Tip**: Add these to your `~/.zshrc` or `~/.bashrc` to persist them.

## Step 3: Run Your First Generation

```bash
python copyflow.py run --topic "AI改变内容创作"
```

**That's it!** 🎉

In 2-3 minutes, you'll get:
- ✅ 10 different style copies in `output/copies.json`
- ✅ 10 AI-generated images in `output/images/`
- ✅ A beautifully formatted Markdown document in `output/content-review.md`

## Step 4: Explore the Output

```bash
# View the generated copies
cat output/copies.json | python -m json.tool | less

# Open the review document
open output/content-review.md  # macOS
xdg-open output/content-review.md  # Linux
```

## Common Use Cases

### Generate more copies
```bash
python copyflow.py run --topic "你的主题" --count 20
```

### Use a different AI model
```bash
python copyflow.py run --topic "你的主题" --model gpt-4o
```

### Test without generating images (faster & free)
```bash
python copyflow.py run --topic "你的主题" --dry-run
```

### Parallel generation (faster)
```bash
python copyflow.py run --topic "你的主题" --concurrent 3
```

### Adversarial mode (higher quality)
```bash
python copyflow.py run --topic "你的主题" --adversarial --iterations 5
```

## Next Steps

- 📚 Read the [full documentation](./README.md)
- 🎯 Check out [real examples](./DEMO.md)
- 💬 Join the [discussions](https://github.com/AIPMAndy/copyflow/discussions)
- 🐛 Report [issues](https://github.com/AIPMAndy/copyflow/issues)

## Troubleshooting

### "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### "OPENAI_API_KEY not set"
```bash
export OPENAI_API_KEY="your_key_here"
```

### "Rate limit exceeded"
```bash
# Use lower concurrency
python copyflow.py run --topic "your topic" --concurrent 1 --rate-limit 0.5
```

## Need Help?

- 💬 Ask in [Discussions](https://github.com/AIPMAndy/copyflow/discussions)
- 🐛 Report bugs in [Issues](https://github.com/AIPMAndy/copyflow/issues)
- 📧 Contact: [Your contact info]

Happy creating! 🎨✨
