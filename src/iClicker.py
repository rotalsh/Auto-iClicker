
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

s = Service('chromedriver.exe')

driver = webdriver.Chrome(service=s)  # Optional argument, if not specified will search path.
# driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('http://www.google.com/');

time.sleep(5) # Let the user actually see something!

search_box = driver.find_element_by_name('q')

search_box.send_keys('ChromeDriver')

search_box.submit()

time.sleep(5) # Let the user actually see something!

driver.quit()