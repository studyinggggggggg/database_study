import requests
from bs4 import BeautifulSoup

#로그인 endpoint

url = 'https://www.kangcom.com/member/member_check.asp'

data = {'id':'smc3843','pwd':'dripxo!419'}

s = requests.Session()

resp = s.post(url, data=data)

my_page = 'https://www.kangcom.com/mypage/'
resp = s.get(my_page)

soup = BeautifulSoup(resp.text,'html.parser')

td = soup.select('td.a_bbslist55')[2]

m = td.get_text()

print(m)

