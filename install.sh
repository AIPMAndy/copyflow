#!/bin/bash
# CopyFlow Installation Script

set -e

echo "🚀 CopyFlow Installation Script"
echo "================================"
echo ""

# Check Python version
echo "📋 Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.10 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
REQUIRED_VERSION="3.10"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then 
    echo "❌ Python $PYTHON_VERSION found, but Python $REQUIRED_VERSION or higher is required."
    exit 1
fi

echo "✅ Python $PYTHON_VERSION detected"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi
echo ""

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install --upgrade pip > /dev/null 2>&1
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi
echo ""

# Check for API keys
echo "🔑 Checking API keys..."
if [ -z "$OPENAI_API_KEY" ]; then
    echo "⚠️  OPENAI_API_KEY not set"
    echo ""
    read -p "Enter your OpenAI API Key (or press Enter to skip): " openai_key
    if [ ! -z "$openai_key" ]; then
        export OPENAI_API_KEY="$openai_key"
        echo "export OPENAI_API_KEY='$openai_key'" >> ~/.zshrc 2>/dev/null || echo "export OPENAI_API_KEY='$openai_key'" >> ~/.bashrc
        echo "✅ OpenAI API Key saved"
    fi
else
    echo "✅ OPENAI_API_KEY is set"
fi

if [ -z "$PONYFLASH_API_KEY" ]; then
    echo "⚠️  PONYFLASH_API_KEY not set (optional for image generation)"
    echo ""
    read -p "Enter your PonyFlash API Key (or press Enter to skip): " pony_key
    if [ ! -z "$pony_key" ]; then
        export PONYFLASH_API_KEY="$pony_key"
        echo "export PONYFLASH_API_KEY='$pony_key'" >> ~/.zshrc 2>/dev/null || echo "export PONYFLASH_API_KEY='$pony_key'" >> ~/.bashrc
        echo "✅ PonyFlash API Key saved"
    fi
else
    echo "✅ PONYFLASH_API_KEY is set"
fi
echo ""

# Test installation
echo "🧪 Testing installation..."
python copyflow.py --version > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✅ Installation successful!"
else
    echo "⚠️  Installation complete but verification failed. You may need to configure API keys."
fi
echo ""

echo "================================"
echo "✨ CopyFlow is ready!"
echo ""
echo "Next steps:"
echo "  1. Activate the virtual environment:"
echo "     source venv/bin/activate"
echo ""
echo "  2. Run your first generation:"
echo "     python copyflow.py run --topic 'AI改变内容创作'"
echo ""
echo "  3. Check out the quick start guide:"
echo "     cat QUICKSTART.md"
echo ""
echo "Need help? Visit: https://github.com/AIPMAndy/copyflow"
echo "================================"
