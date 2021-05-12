import requests
import config

url = 'http://www.renren.com/PLogin.do'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
}
data = {
    'email': config.email,
    'password': config.password
}

response = requests.post(url, headers=headers, data=data)
with open('renrenwang.html', 'wb')as f:
    f.write(response.content)
