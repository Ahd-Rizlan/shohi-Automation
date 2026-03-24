# 🚀 LaunchPilot AI - Advanced Web Automation Bot




An intelligent, stealth-based automation script designed to navigate, scroll, and interact with every page of the **LaunchPilot AI** Google Site. This bot is specifically tuned for the `iit.ac.lk` domain and utilizes local Chrome profiles to maintain institutional login sessions.

## ✨ Key Features

* **👤 Session Persistence:** Uses your local Google Chrome profile so you stay logged in as your IIT user (no "Guest" mode).
* **🕵️ Stealth Mode:** Bypasses bot detection by stripping the `navigator.webdriver` flag and using randomized human-like delays.
* **📜 Auto-Scroll:** Performs a smooth, staggered scroll from top to bottom on every page to trigger lazy-loaded animations and content.
* **🔘 Intelligent Clicker:** Identifies and clicks all interactive buttons while ignoring system-level popups (e.g., "Report Abuse" or "Logout").
* **🔄 Recursive Crawling:** Automatically discovers and queues every internal link found on the site.

---



## 🛠️ Setup & Installation

### 1. Prerequisites
* **Python 3.10+**
* **Google Chrome** (Latest version)
* **VS Code** with Python Extension

### 2. Prepare the Environment

Right-click your project folder in the left sidebar.

Select New File and name it README.md.

Paste the content below into that file and save (Ctrl + S).


---


3. Verify your Chrome Profile
To ensure the bot uses your logged-in account, verify your profile name:

Open Chrome and type chrome://version/ in the search bar.

Look for Profile Path.

If it ends in \Default, keep the script as is.

If it ends in \Profile 1 (or another number), update the code in app.py:
chrome_options.add_argument("--profile-directory=Profile 1")

---

Open your terminal in the project folder and run:
```powershell
# Create the virtual environment
python -m venv .venv

# Activate and install the automation engine
.\.venv\Scripts\python.exe -m pip install selenium webdriver-manager




### 1. RUN

.\.venv\python.exe app.py