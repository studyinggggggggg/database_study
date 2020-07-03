import requests
from bs4 import BeautifulSoup

url ='https://www.kangcom.com/member/member_check.asp'

data = {'id':'smc3843','pwd':'dripxo!419'}

s = requests.Session()

resp = s.post(url,data=data)

my_page = 'https://www.kangcom.com/mypage/'

resp = s.get(my_page)

soup = BeautifulSoup(resp.text,'html.parser')

user_grade = soup.select('td.a_bbslist555')[2]

print(user_grade.get_text())





