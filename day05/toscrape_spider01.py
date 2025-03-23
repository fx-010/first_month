import requests
from bs4 import BeautifulSoup

# 目标URL
url = "http://quotes.toscrape.com"

# 发送HTTP请求获取网页内容
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    print("网页请求成功！")
else:
    print(f"网页请求失败，状态码：{response.status_code}")
    exit()

# 使用BeautifulSoup解析网页内容,切片操作取前五项，查找所有class="text"的span标签（即引用内容）
soup = BeautifulSoup(response.text,"html.parser")
quotes = soup.find_all("span",class_="text")[:5]

# 循环打印前5条引用
for i,quote in enumerate(quotes,1):
    print(f"引用{i}:{quote.text}")