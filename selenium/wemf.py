from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

import time

chrome_driver = 'C:/Users/a3624/Desktop/chromedriver.exe'

driver = webdriver.Chrome(chrome_driver)

driver.get('https://www.naver.com/')

search = driver.find_element_by_id('query')

time.sleep(2)

search.clear()

time.sleep(2)
search.send_keys('조유리')

time.sleep(2)
search.send_keys(Keys.RETURN)

time.sleep(2)

driver.close()