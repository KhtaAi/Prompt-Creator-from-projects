# Project Structure

```
Project Tree (root: Prompt-Creator-from-projects):
├── prompt_creator
│   ├── __init__.py
│   └── main.py
├── .gitignore
├── .treeignore
├── INSTRUCTIONS.md
├── Prompt-Creator-from-projects.code-workspace
├── Readme.md
├── sample.py
└── setup.py
```

---

# File Contents

## File: `prompt_creator\main.py`

```py
import os
import sys
import argparse
import subprocess
from pathlib import Path

# --- ثابت‌های پروژه ---
CONFIG_DIR_NAME = "prompt-creator"
WHITELIST_FILENAME = ".wl"
BLACKLIST_FILENAME = ".bl"
TREE_IGNORE_FILENAME = ".treeignore"
SUMMARY_FILENAME = "summary.md"  # نام فایل خلاصه

OUTPUT_FILENAME_MD = "project_prompt.md"
OUTPUT_FILENAME_TXT = "project_prompt.txt"

GITHUB_REPO_URL = "git+https://github.com/KhtaAi/Prompt-Creator-from-projects.git"

# --- توابع کمکی ---

def process_content(content: str, remove_blanks: bool) -> str:
    """محتوای فایل را پردازش می‌کند (مثلاً حذف خطوط خالی)."""
    if not remove_blanks:
        return content
    lines = content.splitlines()
    processed_lines = [line for line in lines if line.strip()]
    return "\n".join(processed_lines)

# --- توابع اصلی برنامه ---

def handle_special_commands(args):
    """مدیریت دستورات خاص مانند --upgrade و --uninstall."""
    if args.uninstall:
        print("Uninstalling 'prompt-creator'...")
        subprocess.run([sys.executable, "-m", "pip", "uninstall", "-y", "prompt-creator"])
        print("Package uninstalled.")
        sys.exit(0)

    if args.upgrade:
        print("Upgrading 'prompt-creator' from GitHub...")
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", GITHUB_REPO_URL])
        print("Upgrade complete.")
        sys.exit(0)

def ensure_config_files(config_dir: Path):
    """اطمینان از وجود پوشه و فایل‌های پیکربندی."""
    print(f"Checking for config directory: {config_dir}")
    config_dir.mkdir(exist_ok=True)
    
    default_contents = {
        WHITELIST_FILENAME: (
            "src/*\nmain.*\napp.*\nsetup.*\nrequirements.*\nREADME.*\ndocs/*\n"
        ),
        BLACKLIST_FILENAME: (
            "__pycache__\n*.pyc\n*.pyo\n*.log\n*.tmp\n*.bak\nnode_modules\ndist\nbuild\n.env\n.vscode\n.idea\n.git\n.DS_Store\nThumbs.db\n"
        ),
        TREE_IGNORE_FILENAME: (
            "__pycache__\nnode_modules\ndist\nbuild\n.env\n.vscode\n.idea\n.git\n.DS_Store\nThumbs.db\n"
        ),
    }

    config_files = [
        config_dir / WHITELIST_FILENAME,
        config_dir / BLACKLIST_FILENAME,
        config_dir / TREE_IGNORE_FILENAME,
        # فایل summary.md به صورت پیش‌فرض ساخته نمی‌شود، کاربر باید خودش آن را بسازد
    ]

    for f_path in config_files:
        if not f_path.exists():
            print(f"Creating missing config file: {f_path}")
            content = default_contents.get(f_path.name, "")
            with open(f_path, "w", encoding="utf-8") as f:
                f.write(content)

def check_empty_config_files(config_dir: Path):
    """بررسی می‌کند که آیا فایل‌های پیکربندی خالی هستند و از کاربر تاییدیه می‌گیرد."""
    empty_files = []
    # فقط فایل‌های اصلی که انتظار محتوا دارند بررسی می‌شوند
    for filename in [WHITELIST_FILENAME, TREE_IGNORE_FILENAME]:
        filepath = config_dir / filename
        if filepath.exists() and filepath.stat().st_size == 0:
            empty_files.append(filename)
            
    if empty_files:
        print("\nWarning: The following configuration files are empty:")
        for f in empty_files:
            print(f" - {f}")
        
        try:
            choice = input("Do you want to continue with prompt generation? (y/n): ").lower().strip()
            if choice != 'y':
                print("Process aborted by user.")
                sys.exit(0)
        except KeyboardInterrupt:
            print("\nProcess aborted by user.")
            sys.exit(0)

def read_config_file(file_path: Path) -> set[str]:
    """یک فایل پیکربندی را می‌خواند."""
    if not file_path.is_file():
        return set()
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            patterns = {line.strip() for line in f if line.strip() and not line.startswith('#')}
        return patterns
    except Exception as e:
        print(f"Warning: Could not read config file '{file_path}': {e}", file=sys.stderr)
        return set()

def generate_tree(root_dir: Path, ignore_patterns: set[str]) -> str:
    """ساختار درختی پروژه را تولید می‌کند."""
    tree_lines = [f"Project Tree (root: {root_dir.name}):"]
    default_ignores = {CONFIG_DIR_NAME, ".git", "__pycache__", ".vscode", "node_modules", "venv"}
    all_ignores = ignore_patterns.union(default_ignores)

    def build_tree(current_path: Path, prefix: str = ""):
        try:
            entries = sorted(os.scandir(current_path), key=lambda e: (not e.is_dir(), e.name.lower()))
        except OSError:
            return

        valid_entries = [e for e in entries if e.name not in all_ignores]
        
        for i, entry in enumerate(valid_entries):
            connector = "└── " if i == len(valid_entries) - 1 else "├── "
            tree_lines.append(f"{prefix}{connector}{entry.name}")
            if entry.is_dir():
                new_prefix = prefix + ("    " if i == len(valid_entries) - 1 else "│   ")
                build_tree(Path(entry.path), new_prefix)

    build_tree(root_dir)
    return "\n".join(tree_lines)

def is_path_whitelisted(path: Path, whitelist: set[str]) -> bool:
    """بررسی می‌کند که آیا مسیر فایل در لیست سفید قرار دارد یا خیر."""
    if not whitelist:
        return False
    for pattern in whitelist:
        # اگر pattern فقط نام یک پوشه باشد، همه فایل‌های داخل آن پوشه را نیز شامل شود
        if path.match(pattern):
            return True
        # اگر pattern نام پوشه باشد و path داخل آن باشد
        if (not any(c in pattern for c in "*?[]!")) and pattern:
            # pattern فقط یک نام پوشه است
            if str(path).startswith(pattern + os.sep) or str(path).startswith(pattern + "/"):
                return True
    return False

def create_prompt(root_dir: Path, config_dir: Path, args):
    """تابع اصلی برای تولید پرامپت."""
    print("\nStarting prompt generation...")
    
    whitelist = read_config_file(config_dir / WHITELIST_FILENAME)
    blacklist = read_config_file(config_dir / BLACKLIST_FILENAME)
    tree_ignore = read_config_file(config_dir / TREE_IGNORE_FILENAME)

    if not whitelist:
        print("Warning: Whitelist is empty. No files will be included in the prompt.", file=sys.stderr)

    output_content = []
    markdown = args.markdown

    # بخش ۱: اضافه کردن خلاصه (در صورت درخواست)
    if args.include_summary:
        summary_file_path = config_dir / SUMMARY_FILENAME
        if summary_file_path.is_file():
            print(f"Including summary from: {summary_file_path}")
            summary_text = summary_file_path.read_text(encoding='utf-8')
            processed_summary = process_content(summary_text, args.remove_blanks)
            
            if markdown:
                output_content.append(f"# Project Summary ({SUMMARY_FILENAME})\n\n")
                output_content.append(processed_summary)
                output_content.append("\n\n---\n\n")
            else:
                output_content.append(f"========== Project Summary ({SUMMARY_FILENAME}) ==========\n\n")
                output_content.append(processed_summary)
                output_content.append("\n\n=========================================\n\n")
        else:
            print(f"Warning: --include-summary was used, but '{summary_file_path}' not found. Skipping.", file=sys.stderr)

    # بخش ۲: اضافه کردن ساختار درختی
    tree_structure = generate_tree(root_dir, tree_ignore)
    output_content.append("# Project Structure\n\n" if markdown else "========== Project Structure ==========\n\n")
    output_content.append(f"```\n{tree_structure}\n```\n\n" if markdown else f"{tree_structure}\n\n")

    # بخش ۳: پردازش فایل‌ها
    output_content.append("---\n\n# File Contents\n\n" if markdown else "========== File Contents ==========\n\n")
    
    for filepath in sorted(root_dir.rglob('*')):
        if not filepath.is_file():
            continue

        relative_path = filepath.relative_to(root_dir)
        
        if relative_path.name in (OUTPUT_FILENAME_MD, OUTPUT_FILENAME_TXT) or any(part in blacklist for part in relative_path.parts):
            continue

        if is_path_whitelisted(relative_path, whitelist):
            print(f"Including file: {relative_path}")
            try:
                content = filepath.read_text(encoding='utf-8')
                processed_content = process_content(content, args.remove_blanks)
                lang = filepath.suffix.lstrip('.')
                
                if markdown:
                    output_content.append(f"## File: `{relative_path}`\n\n")
                    output_content.append(f"```{lang}\n{processed_content}\n```\n\n")
                else:
                    output_content.append(f"--- File: {relative_path} ---\n\n")
                    output_content.append(f"{processed_content}\n\n")
            except Exception as e:
                print(f"Warning: Could not read file {relative_path}: {e}", file=sys.stderr)

    # نوشتن فایل خروجی
    output_filename = OUTPUT_FILENAME_MD if markdown else OUTPUT_FILENAME_TXT
    output_path = config_dir / output_filename
    
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("".join(output_content))
        print(f"\nPrompt successfully created at: {output_path.resolve()}")
    except Exception as e:
        print(f"\nError writing output file: {e}", file=sys.stderr)


def run():
    """نقطه ورود اصلی برنامه."""
    parser = argparse.ArgumentParser(
        description="Create a project prompt from files, or manage the installation.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    # فلگ‌های اصلی
    parser.add_argument(
        "--markdown", 
        action="store_true", 
        help="Format output as Markdown."
    )
    parser.add_argument(
        "--remove-blanks",
        action="store_true",
        help="Remove blank lines from all included files."
    )
    parser.add_argument(
        "--include-summary",
        action="store_true",
        help=f"Prepend content from '{CONFIG_DIR_NAME}/{SUMMARY_FILENAME}' to the prompt."
    )
    # فلگ‌های مدیریتی
    parser.add_argument(
        '--upgrade', 
        action='store_true', 
        help='Upgrade the script from the GitHub repository.'
    )
    parser.add_argument(
        '--uninstall', 
        action='store_true', 
        help='Uninstall the prompt-creator package.'
    )
    
    args = parser.parse_args()
    
    handle_special_commands(args)
    
    current_working_dir = Path.cwd()
    config_dir = current_working_dir / CONFIG_DIR_NAME
    
    ensure_config_files(config_dir)
    check_empty_config_files(config_dir)
    
    # ارسال تمام آرگومان‌ها به تابع اصلی
    create_prompt(current_working_dir, config_dir, args)

if __name__ == "__main__":
    run()
```

## File: `Readme.md`

```md

# Prompt Creator

ابزاری برای تولید پرامپت از پروژه‌های برنامه‌نویسی با قابلیت انتخاب فایل‌ها و پوشه‌ها به کمک فایل‌های پیکربندی.

## نصب

### نصب از گیتهاب (عمومی)
```bash
pip install git+https://github.com/KhtaAi/Prompt-Creator-from-projects.git
```

### نصب از گیتهاب (خصوصی)
```bash
pip install git+https://<YOUR_PAT>@github.com/KhtaAi/Prompt-Creator-from-projects.git
```
یا با SSH:
```bash
pip install git+ssh://git@github.com/KhtaAi/Prompt-Creator-from-projects.git
```

## استفاده سریع

1. به ریشه پروژه بروید.
2. دستور زیر را اجرا کنید:
   ```bash
   prompt-creator --markdown
   ```
3. پوشه `prompt-creator` و فایل‌های `.wl`, `.bl`, `.treeignore` ساخته می‌شوند.
4. الگوهای مورد نظر را در این فایل‌ها قرار دهید و مجدد دستور را اجرا کنید.

### مثال فایل .wl
```
src/*
main.py
README.md
```

### مثال فایل .bl
```
__pycache__
*.pyc
node_modules
```

### مثال فایل .treeignore
```
node_modules
.git
```

## خروجی

خروجی در فایل `project_prompt.md` یا `project_prompt.txt` در پوشه `prompt-creator` ذخیره می‌شود.

## مدیریت بسته

- ارتقا:
  ```bash
  prompt-creator --upgrade
  ```
- حذف:
  ```bash
  prompt-creator --uninstall
  ```

---
-   **Uninstall:** To remove the package from your system:
    ```bash
    prompt-creator --uninstall
    ```

---

# فارسی

## 🚀 نصب

دستورالعمل نصب بسته به عمومی یا خصوصی بودن ریپازیتوری متفاوت است.

**نصب در ویندوز:** این دستورات در ترمینال‌های ویندوز مانند Command Prompt یا PowerShell نیز کار می‌کنند، اما ابتدا باید **[Git for Windows](https://git-scm.com/download/win)** را نصب کنید.

### برای ریپازیتوری‌های عمومی (Public)

اگر ریپازیتوری عمومی باشد، می‌توانید آن را با این دستور ساده نصب کنید:

```bash
pip install git+https://github.com/KhtaAi/Prompt-Creator-from-projects.git
```

### برای ریپازیتوری‌های خصوصی (Private)

اگر ریپازیتوری خصوصی باشد، برای نصب باید با استفاده از توکن دسترسی شخصی (PAT) یا کلید SSH احراز هویت کنید.

**۱. استفاده از توکن دسترسی شخصی (PAT):**

۱. یک [PAT جدید](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) با دسترسی `repo` بسازید.
۲. دستور زیر را اجرا کرده و `<YOUR_PAT>` را با توکن خود جایگزین کنید:

```bash
pip install git+https://<YOUR_PAT>@github.com/KhtaAi/Prompt-Creator-from-projects.git
```

**۲. استفاده از SSH:**

اگر کلیدهای SSH را برای حساب گیت‌هاب خود تنظیم کرده‌اید، می‌توانید از آدرس SSH استفاده کنید:

```bash
pip install git+ssh://git@github.com/KhtaAi/Prompt-Creator-from-projects.git
```

## ⚙️ نحوه استفاده

پس از نصب، دستور `prompt-creator` به صورت سراسری در ترمینال شما در دسترس خواهد بود.

### ۱. ساخت پرامپت

۱. به پوشه ریشه پروژه‌ای که می‌خواهید برای آن پرامپت بسازید، بروید.
۲. دستور زیر را اجرا کنید:
    ```bash
    prompt-creator
    ```
    یا برای فرمت Markdown:
    ```bash
    prompt-creator --markdown
    ```
۳. بار اولی که دستور را اجرا می‌کنید، یک پوشه به نام `prompt-creator` در ریشه پروژه شما ایجاد می‌شود که شامل سه فایل خالی است: `.wl`، `.bl` و `.treeignore`.
۴. این فایل‌ها را با قوانین مورد نظر خود پر کنید (بخش **پیکربندی** را ببینید).
۵. دستور را دوباره اجرا کنید تا پرامپت بر اساس قوانین شما ساخته شود. فایل خروجی در داخل پوشه `prompt-creator` ذخیره خواهد شد.

### ۲. پیکربندی

رفتار ابزار توسط سه فایل داخل پوشه `prompt-creator` کنترل می‌شود:

-   `.wl` (لیست سفید): فایل‌ها و پوشه‌هایی که باید در پرامپت گنجانده شوند را مشخص کنید. در هر خط یک الگو وارد کنید (مثلاً `src/main.py` یا `components/`).
-   `.bl` (لیست سیاه): فایل‌ها و پوشه‌هایی که محتوای آن‌ها باید نادیده گرفته شود را مشخص کنید.
-   `.treeignore`: فایل‌ها و پوشه‌هایی که باید از نمایش ساختار درختی پروژه حذف شوند را مشخص کنید (مانند `node_modules` یا `.git`).

اگر هر یک از این فایل‌ها خالی باشد، ابزار قبل از ادامه به شما هشدار خواهد داد.

### ۳. مدیریت بسته

-   **ارتقا (Upgrade):** برای دریافت آخرین نسخه از ریپازیتوری:
    ```bash
    prompt-creator --upgrade
    ```
-   **حذف (Uninstall):** برای حذف کامل بسته از سیستم:
    ```bash
    prompt-creator --uninstall
    ```

```

## File: `setup.py`

```py
from setuptools import setup, find_packages

setup(
    name='prompt-creator',
    version='1.0.0',
    packages=find_packages(),
    author='Your Name',  # نام خود را اینجا وارد کنید
    author_email='your.email@example.com',  # ایمیل خود را اینجا وارد کنید
    description='A tool to create prompts from project files based on specified rules.',
    long_description=open('Readme.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/KhtaAi/Prompt-Creator-from-projects',
    entry_points={
        'console_scripts': [
            'prompt-creator=prompt_creator.main:run',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

```

