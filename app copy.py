import time
import random
import os
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException, TimeoutException

# --- CONFIGURATION ---
TARGET_URL = "https://sites.google.com/iit.ac.lk/launchpilot-ai/home"
DOMAIN_FILTER = "sites.google.com/iit.ac.lk/launchpilot-ai"

def cleanup_chrome():
    """Force closes any existing Chrome processes to unlock the profile."""
    print("🧹 Cleaning up background Chrome processes...")
    try:
        subprocess.run(["taskkill", "/F", "/IM", "chrome.exe", "/T"], 
                       capture_output=True, text=True, check=False)
        time.sleep(2) # Give Windows a moment to release the files
    except Exception:
        pass

def get_stealth_driver():
    chrome_options = Options()
    
    # Locate your real Chrome Profile
    user_home = os.path.expanduser("~")
    profile_path = os.path.join(user_home, "AppData", "Local", "Google", "Chrome", "User Data")
    
    # Use your real profile (Change 'Default' to 'Profile 1' if needed)
    chrome_options.add_argument(f"--user-data-dir={profile_path}")
    chrome_options.add_argument("--profile-directory=Default") 

    # --- CRITICAL FIXES FOR CRASHES ---
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    
    # Stealth: Hide automation flags
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Anti-Analytics: Remove 'navigator.webdriver' flag
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    })
    
    driver.set_page_load_timeout(30)
    return driver

def scroll_and_click(driver):
    print("  📜 Scrolling and interacting...")
    
    # Human-like staggered scroll
    total_height = driver.execute_script("return document.body.scrollHeight")
    current_pos = 0
    while current_pos < total_height:
        step = random.randint(400, 800)
        current_pos += step
        driver.execute_script(f"window.scrollTo(0, {current_pos});")
        time.sleep(random.uniform(0.6, 1.2))
    
    # Safety Ignore List (to avoid 'Report Abuse' or 'Logout')
    ignore_list = ["report", "abuse", "logout", "sign out", "feedback", "google", "terms", "privacy"]
    
    buttons = driver.find_elements(By.CSS_SELECTOR, "button, [role='button'], input[type='button']")
    
    for btn in buttons:
        try:
            btn_text = btn.text.lower().strip()
            if any(word in btn_text for word in ignore_list) or btn_text == "":
                continue
                
            if btn.is_displayed() and btn.is_enabled():
                print(f"  🔘 Clicking: {btn_text[:20]}")
                driver.execute_script("arguments[0].click();", btn)
                time.sleep(random.uniform(2, 4)) 
        except:
            continue

def run_automation():
    cleanup_chrome() # Ensure a clean start
    
    driver = None
    visited = set()
    to_visit = [TARGET_URL]

    print("🚀 Bot started. Using your Chrome Profile in Stealth Mode...")

    try:
        driver = get_stealth_driver()
        
        while to_visit:
            current = to_visit.pop(0)
            if current in visited:
                continue
            
            print(f"\n🌐 Visiting: {current}")
            try:
                driver.get(current)
            except TimeoutException:
                print("  ⏳ Page took too long, attempting to proceed...")
            
            visited.add(current)
            time.sleep(random.uniform(3, 5)) 

            scroll_and_click(driver)

            # Discover internal links
            links = driver.find_elements(By.TAG_NAME, "a")
            for link in links:
                href = link.get_attribute("href")
                if href and DOMAIN_FILTER in href:
                    clean_url = href.split('#')[0].rstrip('/')
                    if clean_url not in visited and clean_url not in to_visit:
                        to_visit.append(clean_url)

    except WebDriverException as e:
        print(f"❌ CHROME ERROR: {e}")
        print("👉 FIX: Close all Chrome windows manually and try again.")
    except Exception as e:
        print(f"❌ ERROR: {e}")
    finally:
        if driver:
            driver.quit()
            print(f"\n✨ Task Complete. Visited {len(visited)} pages.")

if __name__ == "__main__":
    run_automation()import time
import random
import os
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException, TimeoutException

# --- CONFIGURATION ---
TARGET_URL = "https://sites.google.com/iit.ac.lk/launchpilot-ai/home"
DOMAIN_FILTER = "sites.google.com/iit.ac.lk/launchpilot-ai"

def cleanup_chrome():
    """Force closes any existing Chrome processes to unlock the profile."""
    print("🧹 Cleaning up background Chrome processes...")
    try:
        subprocess.run(["taskkill", "/F", "/IM", "chrome.exe", "/T"], 
                       capture_output=True, text=True, check=False)
        time.sleep(2) # Give Windows a moment to release the files
    except Exception:
        pass

def get_stealth_driver():
    chrome_options = Options()
    
    # Locate your real Chrome Profile
    user_home = os.path.expanduser("~")
    profile_path = os.path.join(user_home, "AppData", "Local", "Google", "Chrome", "User Data")
    
    # Use your real profile (Change 'Default' to 'Profile 1' if needed)
    chrome_options.add_argument(f"--user-data-dir={profile_path}")
    chrome_options.add_argument("--profile-directory=Default") 

    # --- CRITICAL FIXES FOR CRASHES ---
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    
    # Stealth: Hide automation flags
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Anti-Analytics: Remove 'navigator.webdriver' flag
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    })
    
    driver.set_page_load_timeout(30)
    return driver

def scroll_and_click(driver):
    print("  📜 Scrolling and interacting...")
    
    # Human-like staggered scroll
    total_height = driver.execute_script("return document.body.scrollHeight")
    current_pos = 0
    while current_pos < total_height:
        step = random.randint(400, 800)
        current_pos += step
        driver.execute_script(f"window.scrollTo(0, {current_pos});")
        time.sleep(random.uniform(0.6, 1.2))
    
    # Safety Ignore List (to avoid 'Report Abuse' or 'Logout')
    ignore_list = ["report", "abuse", "logout", "sign out", "feedback", "google", "terms", "privacy"]
    
    buttons = driver.find_elements(By.CSS_SELECTOR, "button, [role='button'], input[type='button']")
    
    for btn in buttons:
        try:
            btn_text = btn.text.lower().strip()
            if any(word in btn_text for word in ignore_list) or btn_text == "":
                continue
                
            if btn.is_displayed() and btn.is_enabled():
                print(f"  🔘 Clicking: {btn_text[:20]}")
                driver.execute_script("arguments[0].click();", btn)
                time.sleep(random.uniform(2, 4)) 
        except:
            continue

def run_automation():
    cleanup_chrome() # Ensure a clean start
    
    driver = None
    visited = set()
    to_visit = [TARGET_URL]

    print("🚀 Bot started. Using your Chrome Profile in Stealth Mode...")

    try:
        driver = get_stealth_driver()
        
        while to_visit:
            current = to_visit.pop(0)
            if current in visited:
                continue
            
            print(f"\n🌐 Visiting: {current}")
            try:
                driver.get(current)
            except TimeoutException:
                print("  ⏳ Page took too long, attempting to proceed...")
            
            visited.add(current)
            time.sleep(random.uniform(3, 5)) 

            scroll_and_click(driver)

            # Discover internal links
            links = driver.find_elements(By.TAG_NAME, "a")
            for link in links:
                href = link.get_attribute("href")
                if href and DOMAIN_FILTER in href:
                    clean_url = href.split('#')[0].rstrip('/')
                    if clean_url not in visited and clean_url not in to_visit:
                        to_visit.append(clean_url)

    except WebDriverException as e:
        print(f"❌ CHROME ERROR: {e}")
        print("👉 FIX: Close all Chrome windows manually and try again.")
    except Exception as e:
        print(f"❌ ERROR: {e}")
    finally:
        if driver:
            driver.quit()
            print(f"\n✨ Task Complete. Visited {len(visited)} pages.")

if __name__ == "__main__":
    run_automation()