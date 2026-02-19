import requests

#업비트 실시간 가격 퍼오기



url = 'https://crix-api.upbit.com/v1/crix/trends/change_rate'

response = requests.get(url).json()

print(response[0])
