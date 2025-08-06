# راهنمای جامع Prompt Creator

---

## فارسی

### معرفی

Prompt Creator ابزاری برای تولید پرامپت از پروژه‌های برنامه‌نویسی است که با انتخاب فایل‌ها و پوشه‌ها به کمک فایل‌های پیکربندی، خروجی ساختارمند و قابل استفاده برای مدل‌های زبانی یا مستندسازی پروژه ارائه می‌دهد.

### نصب

#### نصب از گیتهاب (عمومی)

```bash
pip install git+https://github.com/KhtaAi/Prompt-Creator-from-projects.git
```

#### نصب از گیتهاب (خصوصی)

```bash
pip install git+https://<YOUR_PAT>@github.com/KhtaAi/Prompt-Creator-from-projects.git
```

یا با SSH:

```bash
pip install git+ssh://git@github.com/KhtaAi/Prompt-Creator-from-projects.git
```

### شروع سریع

1. به ریشه پروژه بروید.
2. دستور زیر را اجرا کنید:
   ```bash
   prompt-creator --markdown
   ```
3. پوشه `prompt-creator` و فایل‌های `.wl`, `.bl`, `.treeignore` ساخته می‌شوند.
4. الگوهای مورد نظر را در این فایل‌ها قرار دهید و مجدد دستور را اجرا کنید.

### مثال فایل‌های پیکربندی

#### .wl (لیست سفید)

```
src/*
main.py
README.md
```

#### .bl (لیست سیاه)

```
__pycache__
*.pyc
node_modules
```

#### .treeignore

```
node_modules
.git
```

### اجرای ابزار

```bash
python -m prompt_creator.main --markdown --include-summary
```

### فلگ‌ها و مثال‌ها

- `--markdown`: خروجی را با فرمت مارک‌داون تولید می‌کند.
  ```bash
  prompt-creator --markdown
  ```
- `--remove-blanks`: خطوط خالی را از خروجی حذف می‌کند.
  ```bash
  prompt-creator --remove-blanks
  ```
- `--include-summary`: فایل summary.md را به ابتدای خروجی اضافه می‌کند.
  ```bash
  prompt-creator --include-summary
  ```
- `--upgrade`: ارتقای بسته به آخرین نسخه گیتهاب.
  ```bash
  prompt-creator --upgrade
  ```
- `--uninstall`: حذف کامل بسته.
  ```bash
  prompt-creator --uninstall
  ```

### نکات مهم

- اگر فقط نام پوشه را در `.wl` قرار دهید، فایل‌های داخل آن انتخاب نمی‌شوند. برای انتخاب همه فایل‌ها از `/*` یا `/**` استفاده کنید.
- اگر فایل‌های پیکربندی خالی باشند، ابزار هشدار می‌دهد و ادامه نمی‌دهد مگر با تایید شما.
- خروجی در فایل `project_prompt.md` یا `project_prompt.txt` ذخیره می‌شود.

### مثال خروجی

پس از اجرا، فایل `project_prompt.md` شامل ساختار پروژه و محتوای فایل‌های انتخاب‌شده خواهد بود.

---

## English

### Introduction

Prompt Creator is a tool for generating prompts from programming projects, allowing you to select files and folders via config files and produce a structured output for LLMs or documentation.

### Installation

#### Install from GitHub (Public)

```bash
pip install git+https://github.com/KhtaAi/Prompt-Creator-from-projects.git
```

#### Install from GitHub (Private)

```bash
pip install git+https://<YOUR_PAT>@github.com/KhtaAi/Prompt-Creator-from-projects.git
```

Or with SSH:

```bash
pip install git+ssh://git@github.com/KhtaAi/Prompt-Creator-from-projects.git
```

### Quick Start

1. Go to your project root.
2. Run:
   ```bash
   prompt-creator --markdown
   ```
3. The `prompt-creator` folder and `.wl`, `.bl`, `.treeignore` files will be created.
4. Add your desired patterns to these files and run the command again.

### Example Config Files

#### .wl (Whitelist)

```
src/*
main.py
README.md
```

#### .bl (Blacklist)

```
__pycache__
*.pyc
node_modules
```

#### .treeignore

```
node_modules
.git
```

### Usage

```bash
python -m prompt_creator.main --markdown --include-summary
```

### Flags & Examples

- `--markdown`: Output in Markdown format.
  ```bash
  prompt-creator --markdown
  ```
- `--remove-blanks`: Remove blank lines from output.
  ```bash
  prompt-creator --remove-blanks
  ```
- `--include-summary`: Prepend summary.md to output.
  ```bash
  prompt-creator --include-summary
  ```
- `--upgrade`: Upgrade package from GitHub.
  ```bash
  prompt-creator --upgrade
  ```
- `--uninstall`: Uninstall the package.
  ```bash
  prompt-creator --uninstall
  ```

### Important Notes

- If you only put a folder name in `.wl`, its files will not be included. Use `/*` or `/**` to include all files.
- If config files are empty, the tool will warn and not continue unless you confirm.
- Output is saved in `project_prompt.md` or `project_prompt.txt`.

### Example Output

After running, `project_prompt.md` will contain the project structure and selected file contents.

---

For further questions, refer to the documentation or source code.
