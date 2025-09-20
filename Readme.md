
# ابزار ساخت پرامپت (Prompt Creator)

ابزاری قدرتمند برای خط فرمان که به شما کمک می‌کند تا ساختار و محتوای کامل یک پروژه برنامه‌نویسی را در یک فایل متنی واحد جمع‌آوری کنید. این فایل خروجی برای ارائه به مدل‌های زبان بزرگ (LLMs)، مستندسازی پروژه یا بازبینی کد ایده‌آل است.

## ویژگی‌های کلیدی

- **پیکربندی آسان:** با استفاده از فایل‌های ساده، مشخص کنید کدام بخش‌های پروژه نادیده گرفته شوند.
- **نمایش ساختار درختی:** به صورت خودکار یک نمودار درختی تمیز از ساختار پروژه شما ایجاد می‌کند.
- **خلاصه پروژه:** امکان اضافه کردن یک فایل خلاصه در ابتدای خروجی نهایی.
- **فرمت‌های متنوع:** خروجی را به صورت فایل متنی (`.txt`) یا Markdown (`.md`) دریافت کنید.
- **مدیریت ساده:** ابزار را به راحتی از طریق خط فرمان آپدیت یا حذف کنید.

---

## 🚀 نصب

**پیش‌نیاز:** برای نصب، ابتدا باید **[Git](https://git-scm.com/downloads)** روی سیستم شما نصب شده باشد.

دستور زیر را در ترمینال خود اجرا کنید تا بسته از ریپازیتوری عمومی گیت‌هاب نصب شود:

```bash
pip install git+https://github.com/KhtaAi/Prompt-Creator-from-projects.git
```

### نصب از ریپازیتوری خصوصی (Private)

- **با توکن دسترسی شخصی (PAT):**
  ```bash
  pip install git+https://<YOUR_PAT>@github.com/KhtaAi/Prompt-Creator-from-projects.git
  ```
- **با SSH:**
  ```bash
  pip install git+ssh://git@github.com/KhtaAi/Prompt-Creator-from-projects.git
  ```

---

## ⚙️ راهنمای استفاده سریع

۱. **به ریشه پروژه بروید:** با ترمینال وارد پوشه اصلی پروژه‌ای شوید که می‌خواهید برای آن پرامپت بسازید.

۲. **دستور را اجرا کنید:** برای دریافت خروجی Markdown، دستور زیر را اجرا کنید:
   ```bash
   prompt-creator --markdown
   ```
   با اجرای این دستور برای اولین بار، یک پوشه به نام `prompt-creator` در ریشه پروژه شما ایجاد می‌شود که شامل فایل‌های پیکربندی اولیه است.

۳. **فایل‌ها را پیکربندی کنید:** فایل‌های داخل پوشه `prompt-creator` را مطابق نیاز خود ویرایش کنید (توضیحات کامل در بخش بعد آمده است).

۴. **دستور را دوباره اجرا کنید:** پس از تنظیم پیکربندی، دستور را مجدداً اجرا کنید تا فایل خروجی نهایی بر اساس قوانین شما ساخته شود.

---

## 🔧 پیکربندی

رفتار ابزار توسط فایل‌های داخل پوشه `prompt-creator` کنترل می‌شود:

#### `.bl` (لیست سیاه - Blacklist)
فایل‌ها یا پوشه‌هایی که می‌خواهید **محتوای آن‌ها به طور کامل نادیده گرفته شود** را در این فایل لیست کنید. در هر خط یک الگو بنویسید.

**مثال:**
```
# پوشه‌ها
.git
.vscode
__pycache__
node_modules

# فایل‌های خاص
.env
secret_keys.json

# الگوهای فایل
*.pyc
*.log
```

#### `.treeignore`
فایل‌ها یا پوشه‌هایی که می‌خواهید **فقط از نمایش ساختار درختی پروژه حذف شوند** را در این فایل لیست کنید. این کار به تمیزتر شدن نمودار درختی کمک می‌کند.

**مثال:**
```
node_modules
.git
.vscode
```

#### `summary.md` (اختیاری)
می‌توانید به صورت دستی این فایل را بسازید و خلاصه‌ای از پروژه خود را در آن بنویسید. اگر هنگام اجرای دستور از فلگ `--include-summary` استفاده کنید، محتوای این فایل در ابتدای خروجی نهایی قرار می‌گیرد.

---

## 💡 دستورات خط فرمان (Flags)

می‌توانید از فلگ‌های زیر برای سفارشی‌سازی خروجی استفاده کنید:

- `--markdown`: خروجی را در فرمت Markdown (`project_prompt.md`) ایجاد می‌کند. (در غیر این صورت، خروجی به صورت متن ساده در `project_prompt.txt` خواهد بود).
- `--include-summary`: محتوای فایل `prompt-creator/summary.md` را به ابتدای پرامپت اضافه می‌کند.
- `--remove-blanks`: تمام خطوط خالی را از محتوای فایل‌ها حذف می‌کند تا خروجی فشرده‌تر شود.

---

## 📦 مدیریت بسته

- **ارتقا (Upgrade):** برای دریافت آخرین نسخه از گیت‌هاب:
  ```bash
  prompt-creator --upgrade
  ```
- **حذف (Uninstall):** برای حذف کامل بسته از سیستم:
  ```bash
  prompt-creator --uninstall
  ```

---

# Prompt Creator (English)

A powerful command-line tool to generate a single, comprehensive text file from the structure and content of a programming project. This output file is ideal for feeding to Large Language Models (LLMs), documenting a project, or for code reviews.

## Key Features

- **Easy Configuration:** Use simple files to specify which parts of the project to ignore.
- **Tree Structure Display:** Automatically generates a clean tree diagram of your project structure.
- **Project Summary:** Option to prepend a summary file to the final output.
- **Multiple Formats:** Get the output as a plain text file (`.txt`) or in Markdown (`.md`).
- **Simple Management:** Easily update or uninstall the tool via the command line.

---

## 🚀 Installation

**Prerequisite:** You must have **[Git](https://git-scm.com/downloads)** installed on your system.

Run the following command in your terminal to install the package from the public GitHub repository:

```bash
pip install git+https://github.com/KhtaAi/Prompt-Creator-from-projects.git
```

### For Private Repositories

- **With a Personal Access Token (PAT):**
  ```bash
  pip install git+https://<YOUR_PAT>@github.com/KhtaAi/Prompt-Creator-from-projects.git
  ```
- **With SSH:**
  ```bash
  pip install git+ssh://git@github.com/KhtaAi/Prompt-Creator-from-projects.git
  ```

---

## ⚙️ Quick Start Guide

1.  **Navigate to your project root:** Open your terminal in the main directory of the project for which you want to create a prompt.

2.  **Run the command:** To get a Markdown output, run:
    ```bash
    prompt-creator --markdown
    ```
    The first time you run this, a `prompt-creator` directory containing initial configuration files will be created in your project root.

3.  **Configure the files:** Edit the files inside the `prompt-creator` directory to match your needs (see the next section for a full explanation).

4.  **Run the command again:** Once you've set up your configuration, run the command again to generate the final output file based on your rules.

---

## 🔧 Configuration

The tool's behavior is controlled by files within the `prompt-creator` directory:

#### `.bl` (Blacklist)
List the files or folders whose **content should be completely ignored** in this file. Add one pattern per line.

**Example:**
```
# Folders
.git
.vscode
__pycache__
node_modules

# Specific files
.env
secret_keys.json

# File patterns
*.pyc
*.log
```

#### `.treeignore`
List files or folders that you want to **exclude only from the tree structure view**. This helps keep the tree diagram clean.

**Example:**
```
node_modules
.git
.vscode
```

#### `summary.md` (Optional)
You can manually create this file and write a summary of your project in it. If you use the `--include-summary` flag when running the command, its content will be prepended to the final output.

---

## 💡 Command-Line Flags

You can use the following flags to customize the output:

- `--markdown`: Creates the output in Markdown format (`project_prompt.md`). (Otherwise, the output will be plain text in `project_prompt.txt`).
- `--include-summary`: Adds the content of `prompt-creator/summary.md` to the beginning of the prompt.
- `--remove-blanks`: Removes all blank lines from the file contents for a more compact output.

---

## 📦 Package Management

- **Upgrade:** To get the latest version from GitHub:
  ```bash
  prompt-creator --upgrade
  ```
- **Uninstall:** To completely remove the package from your system:
  ```bash
  prompt-creator --uninstall
  ```