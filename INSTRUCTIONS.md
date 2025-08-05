# Command-Line Flags Guide

This file provides a detailed explanation of all the command-line flags available for the `prompt-creator` tool.

---

# English

### `--markdown`

-   **Purpose:** Formats the output file as a Markdown (`.md`) file.
-   **Behavior:** When this flag is used, the generated prompt will include Markdown syntax for headers, code blocks, and separators. The output file will be named `project_prompt.md`. If omitted, the output will be a plain text (`.txt`) file.
-   **Usage:**
    ```bash
    prompt-creator --markdown
    ```

### `--upgrade`

-   **Purpose:** Upgrades the `prompt-creator` package to the latest version from the GitHub repository.
-   **Behavior:** This command uses `pip` to fetch and install the latest commit from the `main` branch of the repository specified in the `GITHUB_REPO_URL` variable within the script.
-   **Note:** For this to work with a private repository, your environment must be configured with access credentials (e.g., a Personal Access Token in the URL or a configured SSH key).
-   **Usage:**
    ```bash
    prompt-creator --upgrade
    ```

### `--uninstall`

-   **Purpose:** Uninstalls the `prompt-creator` package from your system.
-   **Behavior:** This command executes `pip uninstall prompt-creator` and automatically confirms the action. It's a convenient way to remove the tool completely.
-   **Usage:**
    ```bash
    prompt-creator --uninstall
    ```

---

# فارسی

### `--markdown`

-   **هدف:** فایل خروجی را با فرمت مارک‌داون (`.md`) ایجاد می‌کند.
-   **رفتار:** با استفاده از این فلگ، پرامپت تولید شده شامل سینتکس مارک‌داون برای تیترها، بلوک‌های کد و جداکننده‌ها خواهد بود. فایل خروجی `project_prompt.md` نام خواهد گرفت. در صورت عدم استفاده، خروجی یک فایل متنی ساده (`.txt`) خواهد بود.
-   **نحوه استفاده:**
    ```bash
    prompt-creator --markdown
    ```

### `--upgrade`

-   **هدف:** بسته `prompt-creator` را به آخرین نسخه موجود در ریپازیتوری گیت‌هاب ارتقا می‌دهد.
-   **رفتار:** این دستور از `pip` برای دریافت و نصب آخرین کامیت از شاخه `main` ریپازیتوری که در متغیر `GITHUB_REPO_URL` داخل اسکریپت مشخص شده، استفاده می‌کند.
-   **نکته:** برای اینکه این دستور با یک ریپازیتوری خصوصی کار کند، محیط شما باید با اطلاعات دسترسی (مانند توکن دسترسی شخصی در URL یا کلید SSH تنظیم شده) پیکربندی شده باشد.
-   **نحوه استفاده:**
    ```bash
    prompt-creator --upgrade
    ```

### `--uninstall`

-   **هدف:** بسته `prompt-creator` را از سیستم شما حذف (uninstall) می‌کند.
-   **رفتار:** این دستور `pip uninstall prompt-creator` را اجرا کرده و به صورت خودکار عمل حذف را تأیید می‌کند. این یک راه آسان برای حذف کامل ابزار است.
-   **نحوه استفاده:**
    ```bash
    prompt-creator --uninstall
    ```
