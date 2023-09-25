import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from setup import USERNAME, PASSWORD, CLASS_NAME, CLASS_URL

s = Service(r"./chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get('https://student.iclicker.com/#/login');

time.sleep(4) # Delay for the website to load

search = driver.find_element(By.ID, "userEmail")
search.send_keys(USERNAME)
search.submit()

search = driver.find_element(By.ID, "userPassword")
search.send_keys(PASSWORD)
search.submit()

search = driver.find_element(By.ID, "sign-in-button")
search.click()

time.sleep(6) # Delay for the page to load

driver.find_element(By.XPATH, '//*[text()="'+CLASS_NAME+'"]').click()

time.sleep(6) # Delay for the page to load

try: 
    search = driver.find_element(By.XPATH, '//*[@id="btnJoin"]').click()
    print("joined")
    time.sleep(7) # Delay
    while (driver.current_url != CLASS_URL):
        if (driver.current_url == 'https://student.iclicker.com/#/polling'):
            driver.find_element(By.XPATH, '//*[@id="multiple-choice-a"]').click()
        time.sleep(10)


except Exception as e:
    print("all good")

time.sleep(5)


driver.quit()
