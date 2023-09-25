import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from setup import USERNAME, PASSWORD, CLASS_ORDER, CLASS_NAME

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

driver.get('https://student.iclicker.com/#/login');

time.sleep(4) # Let the user actually see something!

search = driver.find_element(By.ID, "userEmail")
search.send_keys(USERNAME)
search.submit()

search = driver.find_element(By.ID, "userPassword")
search.send_keys(PASSWORD)
search.submit()

search = driver.find_element(By.ID, "sign-in-button")
search.click()

time.sleep(6)

search = driver.find_element(By.XPATH, '//*[text()="'+CLASS_NAME+'"]').click()

time.sleep(5) # Let the user actually see something!

driver.quit()