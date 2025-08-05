# Prompt Creator

A versatile command-line tool to generate detailed prompts from your project's source code. It creates a project summary including a directory tree and the content of whitelisted files, which is ideal for providing context to Large Language Models (LLMs).

This tool is configured via a `prompt-creator` directory in your project's root, where you can specify which files to include (`.wl`), which to ignore in the tree (`.treeignore`), and which to exclude from content processing (`.bl`).

---

# English

## 🚀 Installation

Installation instructions vary depending on whether the repository is public or private.

**On Windows:** These commands work in terminals like Command Prompt or PowerShell, but you must install **[Git for Windows](https://git-scm.com/download/win)** first.

### For Public Repositories

If the repository is public, you can install it with this simple command:

```bash
pip install git+https://github.com/KhtaAi/Prompt-Creator-from-projects.git
```

### For Private Repositories

If the repository is set to private, you need to authenticate using a Personal Access Token (PAT) or an SSH key.

**1. Using a Personal Access Token (PAT):**

1.  [Generate a PAT](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) with `repo` scope.
2.  Run the command below, replacing `<YOUR_PAT>` with your token:

    ```bash
    pip install git+https://<YOUR_PAT>@github.com/KhtaAi/Prompt-Creator-from-projects.git
    ```

**2. Using SSH:**

If you have SSH keys configured with your GitHub account, you can use the SSH URL:

```bash
pip install git+ssh://git@github.com/KhtaAi/Prompt-Creator-from-projects.git
```

## ⚙️ Usage

After installation, the `prompt-creator` command will be available globally in your terminal.

### 1. Generating a Prompt

1.  Navigate to the root directory of the project you want to create a prompt for.
2.  Run the command:
    ```bash
    prompt-creator
    ```
    Or for Markdown format:
    ```bash
    prompt-creator --markdown
    ```
3.  The first time you run it, a `prompt-creator` directory will be created in your project root, containing three empty files: `.wl`, `.bl`, and `.treeignore`.
4.  Populate these files with your desired rules (see **Configuration** below).
5.  Run the command again to generate the prompt based on your rules. The output will be saved inside the `prompt-creator` directory.

### 2. Configuration

The behavior of the tool is controlled by three files inside the `prompt-creator` directory:

-   `.wl` (Whitelist): Specify files and directories to be included in the prompt. Add one pattern per line (e.g., `src/main.py`, `components/`).
-   `.bl` (Blacklist): Specify files and directories whose content should be ignored.
-   `.treeignore`: Specify files and directories to be excluded from the project tree structure view (e.g., `node_modules`, `.git`).

If any of these files are empty, the tool will warn you before proceeding.

### 3. Managing the Package

-   **Upgrade:** To get the latest version from your repository:
    ```bash
    prompt-creator --upgrade
    ```
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
