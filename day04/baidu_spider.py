import requests
from bs4 import BeautifulSoup

url = 'http://www.baidu.com'
response = requests.get(url)
response.encoding  = 'utf-8' 
if response.status_code == 200:
    print('请求成功！')
    soup = BeautifulSoup(response.text,"html.parser")
    title = soup.title.text
    print(f"标题是:{title}")
    print(response.text[:200])
else:
    print(f"打印失败，状态码：{response.status_code}")