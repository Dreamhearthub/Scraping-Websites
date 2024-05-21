from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 17
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    time.sleep(4)
    
    items = driver.find_elements(By.CSS_SELECTOR, 'a[title="Apply"]')
    
    data = []
    
    for item in items:
        link = item.get_attribute("href").strip()
        location = item.find_element(By.CSS_SELECTOR, "li.location").text.strip()
            
        if location.split(',')[-1].strip() in ["GB", "USA"]:
            data.append([
                item.find_element(By.CSS_SELECTOR, "h2").text.strip(),
                com,
                location,
                link
            ])
                
    updateDB(key, data)


if __name__ == "__main__":
    main()
    