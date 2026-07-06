#!/usr/bin/env python3
"""
CopyFlow Interactive Setup Wizard
Guides users through initial configuration
"""

import os
import sys
from pathlib import Path


def print_header():
    """Print welcome header"""
    print("\n" + "=" * 60)
    print("🚀 Welcome to CopyFlow Setup Wizard")
    print("=" * 60)
    print("\nThis wizard will help you configure CopyFlow in 3 minutes.\n")


def check_python_version():
    """Check Python version"""
    print("📋 Step 1/3: Checking Python version...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 10):
        print(f"❌ Python {version.major}.{version.minor} detected")
        print("   CopyFlow requires Python 3.10 or higher")
        print("   Please upgrade: https://www.python.org/downloads/")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} detected\n")
    return True


def setup_api_keys():
    """Setup API keys interactively"""
    print("📋 Step 2/3: Configuring API keys...")
    print("\nYou'll need:")
    print("  • OpenAI API Key (required) - https://platform.openai.com/api-keys")
    print("  • PonyFlash API Key (optional) - for image generation\n")
    
    # OpenAI
    openai_key = os.getenv("OPENAI_API_KEY", "")
    if openai_key:
        print(f"✅ OPENAI_API_KEY already set: {openai_key[:8]}...{openai_key[-4:]}")
    else:
        openai_key = input("Enter your OpenAI API Key (or press Enter to skip): ").strip()
        if openai_key:
            # Save to shell config
            shell_config = Path.home() / ".zshrc" if (Path.home() / ".zshrc").exists() else Path.home() / ".bashrc"
            with open(shell_config, "a") as f:
                f.write(f'\nexport OPENAI_API_KEY="{openai_key}"\n')
            os.environ["OPENAI_API_KEY"] = openai_key
            print(f"✅ Saved to {shell_config}")
        else:
            print("⚠️  Skipped. You can set it later:")
            print("   export OPENAI_API_KEY='your-key'")
    
    # PonyFlash
    pony_key = os.getenv("PONYFLASH_API_KEY", "")
    if pony_key:
        print(f"✅ PONYFLASH_API_KEY already set: {pony_key[:8]}...{pony_key[-4:]}")
    else:
        pony_key = input("\nEnter your PonyFlash API Key (or press Enter to skip): ").strip()
        if pony_key:
            shell_config = Path.home() / ".zshrc" if (Path.home() / ".zshrc").exists() else Path.home() / ".bashrc"
            with open(shell_config, "a") as f:
                f.write(f'\nexport PONYFLASH_API_KEY="{pony_key}"\n')
            os.environ["PONYFLASH_API_KEY"] = pony_key
            print(f"✅ Saved to {shell_config}")
        else:
            print("⚠️  Skipped. Image generation will be disabled.")
    
    print()


def run_test():
    """Run a test generation"""
    print("📋 Step 3/3: Testing CopyFlow...")
    
    test = input("\nWould you like to run a test generation? (y/n): ").strip().lower()
    if test == 'y':
        print("\n🚀 Running test generation (dry-run mode, no images)...\n")
        os.system('python copyflow.py run --topic "AI改变内容创作" --count 3 --dry-run')
        print("\n✅ Test complete! Check the output/ directory.\n")
    else:
        print("\n⏭️  Skipped. You can test later with:")
        print('   python copyflow.py run --topic "your topic" --dry-run\n')


def print_next_steps():
    """Print next steps"""
    print("=" * 60)
    print("✨ Setup Complete!")
    print("=" * 60)
    print("\n📚 Next steps:\n")
    print("  1. Generate your first content:")
    print('     python copyflow.py run --topic "AI内容创作"')
    print("\n  2. Read the quick start guide:")
    print("     cat QUICKSTART.md")
    print("\n  3. Explore examples:")
    print("     cat DEMO.md")
    print("\n  4. Join the community:")
    print("     https://github.com/AIPMAndy/copyflow/discussions")
    print("\n" + "=" * 60)
    print("Need help? Visit: https://github.com/AIPMAndy/copyflow")
    print("=" * 60 + "\n")


def main():
    """Main setup flow"""
    print_header()
    
    if not check_python_version():
        sys.exit(1)
    
    setup_api_keys()
    run_test()
    print_next_steps()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Setup cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Setup failed: {e}")
        print("Please report this issue: https://github.com/AIPMAndy/copyflow/issues")
        sys.exit(1)
