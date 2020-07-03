import requests

serviceKey = 'WVz8Qwna42IOzPx0qDOTbzazA2qKi%2BnUg2GqbG1hAFgqzmEINIuPtfOKQkBRoel4WjRirmhB8kREG5CykSL2jA%3D%3D'

endpoint = 'http://api.visitkorea.or.kr/openapi/service/rest/EngService/areaCode?serviceKey={}&numOfRows=10&pageSize=10&pageNo={}&MobileOS=ETC&MobileApp=AppTest&_type=json'.format(serviceKey,1)

resp = requests.get(endpoint)
print(resp.status_code)
print(resp.text)

data = resp.json()

print(data['response']['body']['items']['item'][0])

