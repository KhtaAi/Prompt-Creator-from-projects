import os
import sys
import argparse
import subprocess
from pathlib import Path

# --- ثابت‌های پروژه ---
# نام پوشه و فایل‌های پیکربندی که در مسیر اجرای دستور ایجاد می‌شوند
CONFIG_DIR_NAME = "prompt-creator"
WHITELIST_FILENAME = ".wl"
BLACKLIST_FILENAME = ".bl" # فایل لیست سیاه برای نادیده گرفتن محتوای فایل‌ها
TREE_IGNORE_FILENAME = ".treeignore" # فایل نادیده گرفتن برای ساختار درختی

# نام فایل خروجی
OUTPUT_FILENAME_MD = "project_prompt.md"
OUTPUT_FILENAME_TXT = "project_prompt.txt"

# لطفا این مقادیر را با اطلاعات صحیح ریپازیتوری خود جایگزین کنید
# این برای دستور --upgrade استفاده می‌شود
GITHUB_REPO_URL = "git+https://github.com/KhtaAi/Prompt-Creator-from-projects.git"

# --- توابع اصلی برنامه ---

def handle_special_commands(args):
    """مدیریت دستورات خاص مانند --upgrade و --uninstall."""
    if args.uninstall:
        print("Uninstalling 'prompt-creator'...")
        # اجرای دستور uninstall و درخواست تایید از کاربر
        subprocess.run([sys.executable, "-m", "pip", "uninstall", "-y", "prompt-creator"])
        print("Package uninstalled.")
        sys.exit(0)

    if args.upgrade:
        if "YourUsername" in GITHUB_REPO_URL:
            print("Error: Please configure the GITHUB_REPO_URL in main.py first.", file=sys.stderr)
            sys.exit(1)
        
        print("Upgrading 'prompt-creator' from GitHub...")
        # برای ریپازیتوری خصوصی، نیاز به توکن دسترسی دارید.
        # کاربر باید توکن را در URL قرار دهد یا از کلید SSH استفاده کند.
        print("Note: For private repositories, you need a Personal Access Token in the URL or SSH keys configured.")
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", GITHUB_REPO_URL])
        print("Upgrade complete.")
        sys.exit(0)

def ensure_config_files(config_dir: Path):
    """اطمینان از وجود پوشه و فایل‌های پیکربندی؛ در صورت عدم وجود، آن‌ها را ایجاد می‌کند."""
    print(f"Checking for config directory: {config_dir}")
    config_dir.mkdir(exist_ok=True)
    
    config_files = [
        config_dir / WHITELIST_FILENAME,
        config_dir / BLACKLIST_FILENAME,
        config_dir / TREE_IGNORE_FILENAME
    ]
    
    for f_path in config_files:
        if not f_path.exists():
            print(f"Creating missing config file: {f_path}")
            f_path.touch()

def check_empty_config_files(config_dir: Path):
    """بررسی می‌کند که آیا فایل‌های پیکربندی خالی هستند و از کاربر تاییدیه می‌گیرد."""
    empty_files = []
    for filename in [WHITELIST_FILENAME, BLACKLIST_FILENAME, TREE_IGNORE_FILENAME]:
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
    """یک فایل پیکربندی (مانند .wl یا .treeignore) را می‌خواند و خطوط آن را برمی‌گرداند."""
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
    # نادیده گرفتن‌های پیش‌فرض
    default_ignores = {"CONFIG_DIR_NAME", ".git", "__pycache__", ".vscode", "node_modules", "venv"}
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
    # تطبیق مستقیم فایل یا پوشه
    for pattern in whitelist:
        if path.match(pattern):
            return True
    return False

def create_prompt(root_dir: Path, config_dir: Path, markdown: bool):
    """تابع اصلی برای تولید پرامپت."""
    print("\nStarting prompt generation...")
    
    # خواندن فایل‌های پیکربندی
    whitelist = read_config_file(config_dir / WHITELIST_FILENAME)
    blacklist = read_config_file(config_dir / BLACKLIST_FILENAME) # برای استفاده در آینده
    tree_ignore = read_config_file(config_dir / TREE_IGNORE_FILENAME)

    if not whitelist:
        print("Warning: Whitelist is empty. No files will be included in the prompt.", file=sys.stderr)

    # تولید ساختار درختی
    tree_structure = generate_tree(root_dir, tree_ignore)
    
    # آماده‌سازی محتوای خروجی
    output_content = []
    output_content.append("# Project Structure\n\n" if markdown else "========== Project Structure ==========\n\n")
    output_content.append(f"```\n{tree_structure}\n```\n\n" if markdown else f"{tree_structure}\n\n")

    # پردازش فایل‌ها بر اساس لیست سفید
    output_content.append("---\n\n# File Contents\n\n" if markdown else "========== File Contents ==========\n\n")

    # TODO: منطق لیست سیاه (blacklist) در اینجا باید پیاده‌سازی شود.
    # در حال حاضر فقط فایل‌های موجود در لیست سیاه نادیده گرفته می‌شوند.
    
    for filepath in sorted(root_dir.rglob('*')):
        if not filepath.is_file():
            continue

        relative_path = filepath.relative_to(root_dir)
        
        # نادیده گرفتن فایل‌های پیکربندی و فایل‌های موجود در لیست سیاه
        if relative_path.name in (OUTPUT_FILENAME_MD, OUTPUT_FILENAME_TXT) or any(part in blacklist for part in relative_path.parts):
            continue

        if is_path_whitelisted(relative_path, whitelist):
            print(f"Including file: {relative_path}")
            try:
                content = filepath.read_text(encoding='utf-8')
                lang = filepath.suffix.lstrip('.')
                
                if markdown:
                    output_content.append(f"## File: `{relative_path}`\n\n")
                    output_content.append(f"```{lang}\n{content}\n```\n\n")
                else:
                    output_content.append(f"--- File: {relative_path} ---\n\n")
                    output_content.append(f"{content}\n\n")
            except Exception as e:
                print(f"Warning: Could not read file {relative_path}: {e}", file=sys.stderr)

    # نوشتن فایل خروجی
    output_filename = OUTPUT_FILENAME_MD if markdown else OUTPUT_FILENAME_TXT
    output_path = config_dir / output_filename
    
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("".join(output_content))
        print(f"\n✅ Prompt successfully created at: {output_path.resolve()}")
    except Exception as e:
        print(f"\nError writing output file: {e}", file=sys.stderr)


def run():
    """نقطه ورود اصلی برنامه."""
    parser = argparse.ArgumentParser(
        description="Create a project prompt from files, or manage the installation.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "--markdown", 
        action="store_true", 
        help="Format output as Markdown."
    )
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
    
    # ابتدا دستورات خاص را مدیریت کن
    handle_special_commands(args)
    
    # اگر دستور خاصی نبود، پروسه اصلی را اجرا کن
    current_working_dir = Path.cwd()
    config_dir = current_working_dir / CONFIG_DIR_NAME
    
    # 1. اطمینان از وجود فایل‌های کانفیگ
    ensure_config_files(config_dir)
    
    # 2. بررسی خالی بودن فایل‌های کانفیگ
    check_empty_config_files(config_dir)
    
    # 3. ایجاد پرامپت
    # اسکن از ریشه پوشه‌ای که دستور در آن اجرا شده انجام می‌شود
    create_prompt(current_working_dir, config_dir, args.markdown)

if __name__ == "__main__":
    run()
