import requests
import json

url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
}
key = input('请输入要翻译的数据:')
data ={
    'i':key,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION',
}

response = requests.post(url,headers=headers,data=data)
data = response.content.decode()
data = json.loads(data)
print(data['translateResult'][0][0]['tgt'])
