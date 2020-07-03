import requests
from bs4 import BeautifulSoup

url = 'https://news.v.daum.net/v/20200629121255144'

resp = requests.get(url)

soup = BeautifulSoup(resp.text,'html.parser')

print(soup.select('h3[class*="_"]'))

a = soup.select('span.txt_info')

print(a)