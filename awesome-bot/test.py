import requests,json
city = "上海"
appid = '6cfc27bfb55d4548b0001b0ddd35251d'

url_v2 = 'https://geoapi.qweather.com/v2/city/' + 'lookup?location=' + city + '&key=' + appid
address = requests.get(url_v2).json()['location'][0]
city_id = address['id']


response = requests.get(r'https://devapi.qweather.com/v7/weather/now?location=%s&key=%s' % (city_id,appid))
response.raise_for_status()

weatherData = json.loads(response.text)
info = weatherData['now']
info_text = info['text']
info_temp = info['temp'] 
info_wind = info['windDir']

print(f'{city}今天天气是{info_text} 温度为{info_temp}℃  风向为{info_wind}')
    #此函数返回一句诗词
url = 'https://v2.jinrishici.com/one.json?'
response = requests.get(url)
response.raise_for_status()
poetryData = json.loads(response.text)
info = poetryData
print(poetryData)
poetryAuthor = poetryData['data']['origin']['author']
poetryContent = poetryData['data']['content']
poetryDynasty = poetryData['data']['origin']['dynasty']
print(poetryContent+'\n----by'+poetryDynasty +''+ poetryAuthor)
