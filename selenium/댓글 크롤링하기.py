import requests
from bs4 import BeautifulSoup

url = 'https://comment.daum.net/apis/v1/posts/@20200629121255144'

headers = {'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb3J1bV9rZXkiOiJuZXdzIiwiZ3JhbnRfdHlwZSI6ImFsZXhfY3JlZGVudGlhbHMiLCJzY29wZSI6W10sImV4cCI6MTU5MzU1NjAyMywiYXV0aG9yaXRpZXMiOlsiUk9MRV9DTElFTlQiXSwianRpIjoiOWMxYTc3NzgtMGI5YS00YWIxLThkMWItZjJhOWM4OGY3NGRkIiwiZm9ydW1faWQiOi05OSwiY2xpZW50X2lkIjoiMjZCWEF2S255NVdGNVowOWxyNWs3N1k4In0.9LALSrQpkJoETccVRIzMn1deyF6_nZKmwe_tBwjuLLE','Host':'comment.daum.net','Cookie':'webid=99aab2cb80284e908484bbad4c34b180; webid_ts=1592040520203; _TI_NID=iok9mjEFfnWoNqMjDA5hhUesz9qLHlqEPY5RegNUSSraOJtFGa0qkJyXzbjFsn3z4rxWQB+HvZuXOv99siQxFg==; webid_sync=1593512823723; TIARA=q544aPGpiIRyg4-rXE9yIvcn6PM3rUYEtHSNVFsekM.4TxMtllHLRGXN3grhWE5EcniTO6ZJp32SPfU8jvX..RjPGPuyRqpe'}

resp = requests.get(url,headers=headers)
print(resp.json())
print(resp.json()['commentCount'])
