# 导入所需的库
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 定义目标URL
url = "http://quotes.toscrape.com"

# 发送HTTP请求获取网页内容
response = requests.get(url)
if response.status_code != 200:
    print("请求失败，状态码：", response.status_code)
    exit()

# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(response.text,"html.parser")

# 抓取前5条引用的文本和作者
quotes = []
authors = []

# 找到所有引用和作者
quote_elements = soup.find_all("div",class_="quote")[:5]# 每条引用都在<div class="quote">中
for quote in quote_elements:
    # 提取引用文本
    quote_text = quote.find("span",class_="text").text.strip()

    # 提取作者
    author = quote.find("small",class_="author").text.strip()

    # 添加到列表
    quotes.append(quote_text)
    authors.append(author)

# 创建Pandas DataFrame
df = pd.DataFrame({
    "Quote": quotes,
    "Author": authors
})

# 打印前5条引用
print("前五条引用：\n",df)

# 保存为CSV文件
df.to_csv("quotes.csv",index=False,encoding="utf-8")
print("\n保存的文件名为:quotes.csv文件")