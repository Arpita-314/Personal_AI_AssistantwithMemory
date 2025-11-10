"""
Simple test to verify code structure
"""
import sys
import os

def test_file_exists():
    """Test if all required files exist"""
    required_files = [
        'config.py',
        'memory.py',
        'screen_capture.py',
        'ai_assistant.py',
        'overlay_ui.py',
        'interview_assistant.py',
        'requirements.txt',
        '.env.example',
        '.gitignore',
        'README.md',
        'USAGE_GUIDE.md',
        'setup.py'
    ]
    
    print("Checking file structure...")
    all_exist = True
    for file in required_files:
        if os.path.exists(file):
            print(f"  ✅ {file}")
        else:
            print(f"  ❌ {file} - NOT FOUND")
            all_exist = False
    
    return all_exist

def test_python_syntax():
    """Test if Python files have valid syntax"""
    python_files = [
        'config.py',
        'memory.py',
        'screen_capture.py',
        'ai_assistant.py',
        'overlay_ui.py',
        'interview_assistant.py',
        'setup.py',
        'test_demo.py'
    ]
    
    print("\nChecking Python syntax...")
    all_valid = True
    for file in python_files:
        try:
            with open(file, 'r') as f:
                compile(f.read(), file, 'exec')
            print(f"  ✅ {file}")
        except SyntaxError as e:
            print(f"  ❌ {file} - Syntax Error: {e}")
            all_valid = False
        except FileNotFoundError:
            print(f"  ⚠️  {file} - Not found")
    
    return all_valid

def test_documentation():
    """Test if documentation files are complete"""
    print("\nChecking documentation...")
    
    # Check README
    with open('README.md', 'r') as f:
        readme = f.read()
        sections = [
            'Features',
            'Quick Start',
            'Installation',
            'Usage',
            'Configuration'
        ]
        for section in sections:
            if section in readme:
                print(f"  ✅ README has {section} section")
            else:
                print(f"  ⚠️  README missing {section} section")
    
    # Check USAGE_GUIDE
    with open('USAGE_GUIDE.md', 'r') as f:
        guide = f.read()
        if len(guide) > 1000:
            print(f"  ✅ USAGE_GUIDE.md is comprehensive ({len(guide)} chars)")
        else:
            print(f"  ⚠️  USAGE_GUIDE.md might be incomplete ({len(guide)} chars)")
    
    return True

def count_lines_of_code():
    """Count lines of code"""
    python_files = [
        'config.py',
        'memory.py',
        'screen_capture.py',
        'ai_assistant.py',
        'overlay_ui.py',
        'interview_assistant.py'
    ]
    
    print("\nCounting lines of code...")
    total = 0
    for file in python_files:
        try:
            with open(file, 'r') as f:
                lines = len(f.readlines())
                print(f"  {file}: {lines} lines")
                total += lines
        except FileNotFoundError:
            pass
    
    print(f"  Total: {total} lines of code")
    return total

def main():
    print("=" * 60)
    print("Interview Assistant - Structure Test")
    print("=" * 60 + "\n")
    
    # Run tests
    files_ok = test_file_exists()
    syntax_ok = test_python_syntax()
    doc_ok = test_documentation()
    loc = count_lines_of_code()
    
    print("\n" + "=" * 60)
    if files_ok and syntax_ok:
        print("✅ All structure tests passed!")
        print(f"📊 Total: {loc} lines of code across 6 main modules")
        print("\n✨ The invisible interview assistant is ready!")
        print("\nNext steps:")
        print("  1. Install dependencies: pip install -r requirements.txt")
        print("  2. Configure .env with API keys")
        print("  3. Run: python interview_assistant.py")
    else:
        print("❌ Some tests failed")
        return 1
    
    print("=" * 60 + "\n")
    return 0

if __name__ == "__main__":
    sys.exit(main())
