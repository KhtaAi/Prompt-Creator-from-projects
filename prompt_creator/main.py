import os
import sys
import argparse
import subprocess
import fnmatch
from pathlib import Path
from importlib import metadata

# --- ثابت‌های پروژه ---
CONFIG_DIR_NAME = "prompt-creator"
 # حذف whitelist
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
        # اضافه کردن --no-cache-dir برای اطمینان از دریافت نسخه جدید
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "--no-cache-dir", GITHUB_REPO_URL])
        print("Upgrade complete.")
        sys.exit(0)

def ensure_config_files(config_dir: Path):
    """اطمینان از وجود پوشه و فایل‌های پیکربندی."""
    print(f"Checking for config directory: {config_dir}")
    config_dir.mkdir(exist_ok=True)
    default_contents = {
        BLACKLIST_FILENAME: (
            "__pycache__\n*.pyc\n*.pyo\n*.log\n*.tmp\n*.bak\nnode_modules\ndist\nbuild\n.env\n.vscode\n.idea\n.git\n.DS_Store\nThumbs.db\n"
        ),
        TREE_IGNORE_FILENAME: (
            "__pycache__\nnode_modules\ndist\nbuild\n.env\n.vscode\n.idea\n.git\n.DS_Store\nThumbs.db\n"
        ),
    }

    config_files = [
        config_dir / BLACKLIST_FILENAME,
        config_dir / TREE_IGNORE_FILENAME,
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
    for filename in [BLACKLIST_FILENAME, TREE_IGNORE_FILENAME]:
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

def create_prompt(root_dir: Path, config_dir: Path, args):
    """تابع اصلی برای تولید پرامپت."""
    print("\nStarting prompt generation...")

    blacklist = read_config_file(config_dir / BLACKLIST_FILENAME)
    tree_ignore = read_config_file(config_dir / TREE_IGNORE_FILENAME)

    output_content = []
    markdown = args.markdown

    # بخش ۱: اضافه کردن خلاصه
    if args.include_summary:
        summary_file_path = config_dir / SUMMARY_FILENAME
        if summary_file_path.is_file():
            print(f"Including summary from: {summary_file_path}")
            summary_text = summary_file_path.read_text(encoding='utf-8')
            processed_summary = process_content(summary_text, args.remove_blanks)
            if markdown:
                output_content.append(f"# Project Summary ({SUMMARY_FILENAME})\n\n{processed_summary}\n\n---\n\n")
            else:
                output_content.append(f"========== Project Summary ({SUMMARY_FILENAME}) ==========\n\n{processed_summary}\n\n=========================================\n\n")
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

        # --- START: Final Blacklist Logic ---
        skip = False
        for pattern in blacklist:
            p = pattern.strip()
            if not p:
                continue

            # Case 1: Pattern is a path-like spec (contains a separator).
            # Use the robust `pathlib.match` which handles OS differences.
            if '/' in p or '\\' in p:
                if relative_path.match(p):
                    skip = True
                    break
            # Case 2: Pattern is a simple name (e.g., node_modules, *.log).
            # Match it against any part of the path.
            else:
                if any(fnmatch.fnmatch(part, p) for part in relative_path.parts):
                    skip = True
                    break
        # --- END: Final Blacklist Logic ---

        if relative_path.name in (OUTPUT_FILENAME_MD, OUTPUT_FILENAME_TXT) or skip:
            continue

        print(f"Including file: {relative_path}")
        try:
            content = filepath.read_text(encoding='utf-8')
            processed_content = process_content(content, args.remove_blanks)
            lang = filepath.suffix.lstrip('.')
            if markdown:
                output_content.append(f"## File: `{relative_path}`\n\n```{lang}\n{processed_content}\n```\n\n")
            else:
                output_content.append(f"--- File: {relative_path} ---\n\n{processed_content}\n\n")
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
    try:
        app_version = metadata.version('prompt-creator')
    except metadata.PackageNotFoundError:
        app_version = "dev"

    parser = argparse.ArgumentParser(
        description="Create a project prompt from files, or manage the installation.",
        formatter_class=argparse.RawTextHelpFormatter
    )

    # فلگ‌های اصلی
    parser.add_argument("--markdown", action="store_true", help="Format output as Markdown.")
    parser.add_argument("--remove-blanks", action="store_true", help="Remove blank lines from all included files.")
    parser.add_argument("--include-summary", action="store_true", help=f"Prepend content from '{CONFIG_DIR_NAME}/{SUMMARY_FILENAME}' to the prompt.")

    # فلگ‌های مدیریتی
    parser.add_argument('--upgrade', action='store_true', help='Upgrade the script from the GitHub repository.')
    parser.add_argument('--uninstall', action='store_true', help='Uninstall the prompt-creator package.')
    parser.add_argument('--version', action='version', version=f'%(prog)s {app_version}', help="Show program's version number and exit.")

    args = parser.parse_args()
    handle_special_commands(args)

    current_working_dir = Path.cwd()
    config_dir = current_working_dir / CONFIG_DIR_NAME

    ensure_config_files(config_dir)
    check_empty_config_files(config_dir)

    create_prompt(current_working_dir, config_dir, args)

if __name__ == "__main__":
    run()