# Setup & Run Guide

## Prerequisites

- Python 3.10 or higher installed
- Google Chrome browser installed

---

## Step 1 — Clone or Download the Project

Make sure you have the project folder with `app.py` inside it.

---

## Step 2 — Create a Virtual Environment

Open a terminal in the project folder and run:

```bash
python -m venv .venv
```

---

## Step 3 — Install Dependencies

```bash
.venv\Scripts\python.exe -m pip install selenium webdriver-manager
```

---

## Step 4 — Close All Chrome Windows

> **Important:** Before running the script, make sure all Chrome windows are fully closed.
> The script launches its own Chrome session — if Chrome is already open it will fail.

---

## Step 5 — Run the Script

```bash
PYTHONUTF8=1 .venv\Scripts\python.exe app.py
```

---

## What Happens When You Run It

1. Chrome opens maximized automatically
2. The bot visits the target website
3. On each page it scrolls from top to bottom using PAGE_DOWN steps
4. It stays on each page for 10–20 seconds
5. It follows internal links and visits all pages on the site
6. Chrome closes automatically when done

---

## Expected Output

```
🚀 Bot started using your Chrome Profile...

📄 Visiting: https://sites.google.com/iit.ac.lk/launchpilot-ai/home
⏳ Checking if login is required...
  📜 Scrolling and looking for buttons...
    scrolling top -> bottom (11 steps)
    step 1/11
    step 2/11
    ...
  ⏱ Staying on page for 15 seconds...

📄 Visiting: https://sites.google.com/iit.ac.lk/launchpilot-ai/features
...

✨ Done. Visited 5 pages.
```

---

## Troubleshooting

| Error | Fix |
|-------|-----|
| `DevToolsActivePort file doesn't exist` | Close all Chrome windows and try again |
| `session deleted as the browser has closed` | Do not close Chrome while the script is running |
| `python` not found | Make sure Python is installed and added to PATH |
| `ModuleNotFoundError` | Re-run Step 3 to install dependencies |
