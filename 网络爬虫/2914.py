import requests
import cookie

url = 'http://www.renren.com/PLogin.do'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
}
data = {
    'email':cookie.email,
    'password':cookie.password
}

session = requests.Session()
session.post(url,headers=headers,data=data)

url2 = 'http://www.renren.com/870183297/profile'
response =session.get(url2,headers=headers)
with open('renrenwang3.html', 'wb')as f:
    f.write(response.content)
