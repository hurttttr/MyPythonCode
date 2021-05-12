import requests
import cookie

url = 'http://www.renren.com/PLogin.do'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
}
Cookie = cookie.Cookie
data = Cookie.split('; ')
cookies = {x.split('=')[0]:x.split('=')[1] for x in data}

response = requests.get(url, headers=headers,cookies=cookies)
with open('renrenwang2.html', 'wb')as f:
    f.write(response.content)
