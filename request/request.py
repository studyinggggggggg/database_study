import requests
'''
<get 사용하기>

url = 'https://news.v.daum.net/v/20190728165812603'
resp = requests.get(url)

print(resp)
#오류가 있으면 response 값이 300으로 나옴

print(resp.text)

<post 사용하기>

url = 'https://www.kangcom.com/member/member_check.asp'

data = {
    'id' : 'test',
    'pwd' : '1234'
}

resp = requests.post(url, data = data)
print(resp.text)

<header 사용하기>

url = 'https://news.v.daum.net/v/20190728165812603'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
resp = requests.get(url, headers = headers)
print(resp.text)
'''

url = 'https://news.v.daum.net/v/20190728165812603'
resp = requests.get(url)

if resp.status_code == 200:
    print(resp.text)
else:
    print("error")