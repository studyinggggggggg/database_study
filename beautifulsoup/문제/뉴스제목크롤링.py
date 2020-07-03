import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup


def get_naver_news_title(url):

    resp = requests.get(url)

    soup = BeautifulSoup(resp.text,'html.parser')

    news_headline = soup.select_one('h3.tit_view')

    if news_headline :
        return print(news_headline.get_text())
    return print("")

get_naver_news_title('https://news.v.daum.net/v/20200702222731666')

def get_naver_news_contents(url):
    resp = requests.get(url)

    soup = BeautifulSoup(resp.text,'html.parser')

    news_content = soup.select('div._article_body_contents')

    news_contents = ''

    for i in news_content:
        news_contents += (i.get_text() +'\n')

    print(news_contents)

get_naver_news_contents('https://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=277&aid=0004711010&date=20200702&type=1&rankingSeq=1&rankingSectionId=100')

def get_naver_news_comments(url):
    chrome_driver = 'C:/Users/a3624/Desktop/chromedriver.exe'

    driver = webdriver.Chrome(chrome_driver)

    driver.get(url)

    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.u_cbox_text_wrap')))

    src = driver.page_source

    soup = BeautifulSoup(src,'html.parser')

    driver.close()

    comment = soup.select('div.u_cbox_text_wrap')

    comments = ''
    for i in comment:
        comments += (i.get_text()+'\n')

    print(comments)

get_naver_news_comments('https://sports.news.naver.com/news.nhn?oid=003&aid=0009948083')