import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from setup import USERNAME, PASSWORD, CLASS_NAME, CLASS_URL

s = Service(r"./chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get('https://student.iclicker.com/#/login');

time.sleep(4) # Delay for the website to load

search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "userEmail")))
search.send_keys(USERNAME)
search.submit()

search = driver.find_element(By.ID, "userPassword")
search.send_keys(PASSWORD)
search.submit()

search = driver.find_element(By.ID, "sign-in-button")
search.click()

search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[text()="'+CLASS_NAME+'"]')))
search.click()

try: 
    search = WebDriverWait(driver, 600).until( # 10 minute delay (600 seconds)
        EC.element_to_be_clickable((By.XPATH, '//*[@id="btnJoin"]')))
    search.click()
    time.sleep(7) # Delay
    while (driver.current_url != CLASS_URL):
        if (driver.current_url == 'https://student.iclicker.com/#/polling'):
            driver.find_element(By.XPATH, '//*[@id="multiple-choice-a"]').click()
        time.sleep(10)                         # how often this refreshes to click a poll


except Exception as e:
    print("Try again")

finally:
    driver.quit()
