import requests
from bs4 import BeautifulSoup

url = 'https://news.v.daum.net/v/20200629121255144'
resp = requests.get(url)

html = resp.text

soup = BeautifulSoup(html,'html.parser')

a = soup.find('div',id="harmonyContainer")
b = a.find_all('p')

c = ''
for i in b:
    c += i.get_text().strip()


print(c)