import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

import time

chrome_driver = 'C:/Users/a3624/Desktop/chromedriver.exe'
driver = webdriver.Chrome(chrome_driver)

url = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=437&aid=0000241821'

driver.get(url)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.u_cbox_count')))

src = driver.page_source
soup = BeautifulSoup(src,'html.parser')

driver.close()

comment = soup.select_one('span.u_cbox_count')

a = comment.get_text()

print(a)
