import requests

url = 'https://www.baidu.com/s?wd=hello'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
}
response = requests.get(url, headers=headers)
content = response.content
with open('1.html', 'wb') as f:
    f.write(content)
