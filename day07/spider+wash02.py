import requests
from bs4 import BeautifulSoup
import logging

# 设置简单的日志，只记录关键信息
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def fetch_quotes(page):
    try:
        # 构造网页地址
        url = f"http://quotes.toscrape.com/page/{page}/"
        logging.info(f"开始爬取第{page}页")
        
        # 发送请求获取网页内容
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # 如果请求失败会抛出异常
        
        # 解析网页
        soup = BeautifulSoup(response.text, "html.parser")
        
        # 找到所有引言
        quotes = soup.find_all("span", class_="text")
        
        # 提取每条引言的文本
        quote_list = [quote.text for quote in quotes]
        
        logging.info(f"第{page}页爬取成功，共{len(quote_list)}条引言")
        return quote_list
    
    except Exception as e:
        # 如果出错，记录错误并返回空列表
        logging.error(f"爬取第{page}页失败：{e}")
        return []

def main():
    all_quotes = []
    # 爬取前2页
    for page in range(1, 3):
        quotes = fetch_quotes(page)
        all_quotes.extend(quotes)
    
    # 打印所有引言
    if all_quotes:
        print("\n爬取到的所有引言如下：")
        for i, quote in enumerate(all_quotes, 1):
            print(f"{i}. {quote}")
    else:
        print("没有爬取到任何引言")
    
    print(f"\n总共爬取{len(all_quotes)}条引言")

if __name__ == "__main__":
    main()