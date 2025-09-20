### How it works

If a file name (like `utils.py`) is in `.bl`, that file will be excluded from the prompt. If a folder name (like `secret`) is in `.bl`, that folder and all its contents will be excluded. All other files and folders will be included in the prompt output.

# Prompt Creator

A tool for generating prompts from programming projects, allowing you to select files and folders via config files and produce a structured output for LLMs or documentation.

## Installation

### Install from GitHub (Public)

```bash
pip install git+https://github.com/KhtaAi/Prompt-Creator-from-projects.git
```

### Install from GitHub (Private)

```bash
pip install git+https://<YOUR_PAT>@github.com/KhtaAi/Prompt-Creator-from-projects.git
```

Or with SSH:

```bash
pip install git+ssh://git@github.com/KhtaAi/Prompt-Creator-from-projects.git
```

## Quick Start

1. Go to your project root.
2. Run:
   ```bash
   prompt-creator --markdown
   ```
3. The `prompt-creator` folder and `.wl`, `.bl`, `.treeignore` files will be created.
4. Add your desired patterns to these files and run the command again.
5. The `prompt-creator` folder and `.bl`, `.treeignore` files will be created.
6. Add your desired patterns to these files and run the command again.

### Example Config Files

#### .bl (Blacklist)

```
secret
utils.py
__pycache__
*.pyc
node_modules
```

#### .treeignore

```
node_modules
.git
```

## Output

The result will be saved in `project_prompt.md` or `project_prompt.txt` inside the `prompt-creator` folder.

## Package Management

```bash
prompt-creator --upgrade
```

```bash
prompt-creator --uninstall
```

# پرامپت کریتور

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

```bash
prompt-creator --upgrade
```

```bash
prompt-creator --uninstall
```

<<<<<<< HEAD

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
`bash
    prompt-creator
    `
یا برای فرمت Markdown:
`bash
    prompt-creator --markdown
    `
۳. بار اولی که دستور را اجرا می‌کنید، یک پوشه به نام `prompt-creator` در ریشه پروژه شما ایجاد می‌شود که شامل سه فایل خالی است: `.wl`، `.bl` و `.treeignore`.
۴. این فایل‌ها را با قوانین مورد نظر خود پر کنید (بخش **پیکربندی** را ببینید).
۵. دستور را دوباره اجرا کنید تا پرامپت بر اساس قوانین شما ساخته شود. فایل خروجی در داخل پوشه `prompt-creator` ذخیره خواهد شد.

### ۲. پیکربندی

رفتار ابزار توسط سه فایل داخل پوشه `prompt-creator` کنترل می‌شود:

- `.wl` (لیست سفید): فایل‌ها و پوشه‌هایی که باید در پرامپت گنجانده شوند را مشخص کنید. در هر خط یک الگو وارد کنید (مثلاً `src/main.py` یا `components/`).
- `.bl` (لیست سیاه): فایل‌ها و پوشه‌هایی که محتوای آن‌ها باید نادیده گرفته شود را مشخص کنید.
- `.treeignore`: فایل‌ها و پوشه‌هایی که باید از نمایش ساختار درختی پروژه حذف شوند را مشخص کنید (مانند `node_modules` یا `.git`).

اگر هر یک از این فایل‌ها خالی باشد، ابزار قبل از ادامه به شما هشدار خواهد داد.

### ۳. مدیریت بسته

- **ارتقا (Upgrade):** برای دریافت آخرین نسخه از ریپازیتوری:
  ```bash
  prompt-creator --upgrade
  ```
- **حذف (Uninstall):** برای حذف کامل بسته از سیستم:
  ```bash
  prompt-creator --uninstall
  ```
  =======
  > > > > > > > ed7609b (docs: English section first, Persian section second in Readme.md)
