from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

import time

chrome_driver = 'C:/Users/a3624/Desktop/chromedriver.exe'
driver = webdriver.Chrome(chrome_driver)

url = 'https://news.v.daum.net/v/20200630153008123'

driver.get(url)

src = driver.page_source

soup = BeautifulSoup(src,'html.parser')
comment_area = soup.select_one('span.alex-count-area')

# chrome driver 사용 후, close 함수로 종료
driver.close()

print(comment_area.get_text())
