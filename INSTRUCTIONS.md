# Command-Line Flags Guide

## راهنمای پروژه Prompt-Creator-from-projects

### فارسی

این پروژه ابزاری برای تولید پرامپت از فایل‌های پروژه بر اساس قوانین مشخص‌شده در فایل‌های پیکربندی است.

#### مراحل استفاده:

1. پوشه `prompt-creator` را در ریشه پروژه داشته باشید.
2. فایل `.wl` را در پوشه `prompt-creator` بسازید و نام فایل‌ها یا پوشه‌هایی که می‌خواهید در خروجی پرامپت باشند را در آن بنویسید.
   - اگر فقط نام یک پوشه (مثلاً `prompt_creator`) را بنویسید، فقط خود پوشه انتخاب می‌شود و فایل‌های داخل آن انتخاب نمی‌شوند.
   - برای انتخاب همه فایل‌های داخل یک پوشه، باید الگو را به صورت `prompt_creator/*` یا `prompt_creator/**` بنویسید.
   - مثال:
     ```
     prompt_creator/*
     setup.py
     ```
3. فایل‌های دیگر مانند `.bl` (لیست سیاه)، `.treeignore` (لیست نادیده‌گیری ساختار درختی)، و `summary.md` (خلاصه پروژه) را در صورت نیاز بسازید.
4. اسکریپت را اجرا کنید:
   ```bash
   python -m prompt_creator.main --markdown --include-summary
   ```
5. خروجی در فایل `project_prompt.md` یا `project_prompt.txt` در پوشه `prompt-creator` ذخیره می‌شود.

#### نکات مهم:

- اگر فقط نام پوشه را در `.wl` قرار دهید، هیچ‌یک از فایل‌های داخل آن پوشه در خروجی قرار نمی‌گیرند. برای انتخاب همه فایل‌ها، از الگوهای `/*` یا `/**` استفاده کنید.
- می‌توانید فایل‌های خاص را با نام کامل یا الگوهای دیگر اضافه کنید.
- اگر فایل‌های پیکربندی خالی باشند، برنامه هشدار می‌دهد و ادامه نمی‌دهد مگر با تایید شما.

---

### English

This project is a tool for generating prompts from project files based on rules specified in configuration files.

#### Usage Steps:

1. Make sure you have the `prompt-creator` folder at the project root.
2. Create a `.wl` file inside the `prompt-creator` folder and list the files or folders you want included in the prompt output.
   - If you only write the name of a folder (e.g., `prompt_creator`), only the folder itself is selected, not its contents.
   - To include all files inside a folder, use the pattern `prompt_creator/*` or `prompt_creator/**`.
   - Example:
     ```
     prompt_creator/*
     setup.py
     ```
3. Optionally, create other config files like `.bl` (blacklist), `.treeignore` (tree ignore list), and `summary.md` (project summary).
4. Run the script:
   ```bash
   python -m prompt_creator.main --markdown --include-summary
   ```
5. The output will be saved in `project_prompt.md` or `project_prompt.txt` inside the `prompt-creator` folder.

#### Important Notes:

- If you only put the folder name in `.wl`, none of its files will be included in the output. To include all files, use the `/*` or `/**` pattern.
- You can add specific files by their full name or use other patterns.
- If config files are empty, the program will warn and not continue unless you confirm.

---

برای سوالات بیشتر یا رفع اشکال، به مستندات پروژه یا کد منبع مراجعه کنید.
For further questions or troubleshooting, refer to the project documentation or source code.
This file provides a detailed explanation of all the command-line flags available for the `prompt-creator` tool.

---

# English

### `--markdown`

- **Purpose:** Formats the output file as a Markdown (`.md`) file.
- **Behavior:** When this flag is used, the generated prompt will include Markdown syntax for headers, code blocks, and separators. The output file will be named `project_prompt.md`. If omitted, the output will be a plain text (`.txt`) file.
- **Usage:**
  ```bash
  prompt-creator --markdown
  ```

### `--remove-blanks`

- **Purpose:** Removes all empty lines (or lines with only whitespace) from the content of the included files.
- **Behavior:** This helps to create a more compact prompt by reducing unnecessary vertical space.
- **Usage:**
  ```bash
  prompt-creator --remove-blanks
  ```

### `--include-summary`

- **Purpose:** Prepends a summary file to the beginning of the generated prompt.
- **Behavior:** The tool will look for a file named `summary.md` inside the `prompt-creator` configuration directory. If found, its content will be placed at the top of the final prompt. If the file is not found, a warning will be displayed.
- **Usage:**
  ```bash
  prompt-creator --include-summary
  ```

### `--upgrade`

- **Purpose:** Upgrades the `prompt-creator` package to the latest version from the GitHub repository.
- **Behavior:** This command uses `pip` to fetch and install the latest commit from the `main` branch of the repository.
- **Note:** If the repository is private, your environment must be configured with access credentials (e.g., a globally configured SSH key or a credential manager that stores your PAT) for the upgrade to work seamlessly.
- **Usage:**
  ```bash
  prompt-creator --upgrade
  ```

### `--uninstall`

- **Purpose:** Uninstalls the `prompt-creator` package from your system.
- **Behavior:** This command executes `pip uninstall prompt-creator` and automatically confirms the action. It's a convenient way to remove the tool completely.
- **Usage:**
  ```bash
  prompt-creator --uninstall
  ```

---

# فارسی

### `--markdown`

- **هدف:** فایل خروجی را با فرمت مارک‌داون (`.md`) ایجاد می‌کند.
- **رفتار:** با استفاده از این فلگ، پرامپت تولید شده شامل سینتکس مارک‌داون برای تیترها، بلوک‌های کد و جداکننده‌ها خواهد بود. فایل خروجی `project_prompt.md` نام خواهد گرفت. در صورت عدم استفاده، خروجی یک فایل متنی ساده (`.txt`) خواهد بود.
- **نحوه استفاده:**
  ```bash
  prompt-creator --markdown
  ```

### `--remove-blanks`

- **هدف:** تمام خطوط خالی (یا خطوطی که فقط شامل فضای خالی هستند) را از محتوای فایل‌های گنجانده شده حذف می‌کند.
- **رفتار:** این فلگ با کاهش فضای خالی عمودی، به ساخت یک پرامپت فشرده‌تر کمک می‌کند.
- **نحوه استفاده:**
  ```bash
  prompt-creator --remove-blanks
  ```

### `--include-summary`

- **هدف:** یک فایل خلاصه را به ابتدای پرامپت تولید شده اضافه می‌کند.
- **رفتار:** ابزار به دنبال فایلی به نام `summary.md` در داخل پوشه پیکربندی `prompt-creator` می‌گردد. اگر فایل پیدا شود، محتوای آن در بالای پرامپت نهایی قرار می‌گیرد. اگر فایل پیدا نشود، یک هشدار نمایش داده می‌شود.
- **نحوه استفاده:**
  ```bash
  prompt-creator --include-summary
  ```

### `--upgrade`

- **هدف:** بسته `prompt-creator` را به آخرین نسخه موجود در ریپازیتوری گیت‌هاب ارتقا می‌دهد.
- **رفتار:** این دستور از `pip` برای دریافت و نصب آخرین کامیت از شاخه `main` ریپازیتوری استفاده می‌کند.
- **نکته:** اگر ریپازیتوری خصوصی باشد، محیط شما باید با اطلاعات دسترسی (مانند کلید SSH یا یک مدیریت‌کننده اعتبار که توکن شما را ذخیره کرده) پیکربندی شده باشد تا ارتقا به درستی کار کند.
- **نحوه استفاده:**
  ```bash
  prompt-creator --upgrade
  ```

### `--uninstall`

- **هدف:** بسته `prompt-creator` را از سیستم شما حذف (uninstall) می‌کند.
- **رفتار:** این دستور `pip uninstall prompt-creator` را اجرا کرده و به صورت خودکار عمل حذف را تأیید می‌کند. این یک راه آسان برای حذف کامل ابزار است.
- **نحوه استفاده:**
  ```bash
  prompt-creator --uninstall
  ```
