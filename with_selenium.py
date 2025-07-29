from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

# Setup headless Chrome
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Optional: comment out to see browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open W3Schools homepage
driver.get("https://www.w3schools.com/")

# ✅ Wait until tutorial links appear
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "w3-bar-item"))
)

# Get page source after content has loaded
soup = BeautifulSoup(driver.page_source, "html.parser")

# Extract tutorial links
tutorials = soup.find_all("a")

print("Number of tutorials found:", len(tutorials))


for tutorial in tutorials:
    title = tutorial.text.strip()
    link = tutorial['href']
    if link.startswith('/'):
        link = "https://www.w3schools.com" + link
    print(f"{title}: {link}")

# Quit browser
driver.quit()
