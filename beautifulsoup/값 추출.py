import requests
import re
from bs4 import BeautifulSoup


url = 'https://news.v.daum.net/v/20200629121255144'

resp = requests.get(url)

soup = BeautifulSoup(resp.text,'html.parser')

print(soup.find_all(re.compile('h\d')))
print(soup.find_all('img',attrs={'src':re.compile('.+\.jpg')}))

print(soup.find_all("h3",class_=re.compile('^tit')))