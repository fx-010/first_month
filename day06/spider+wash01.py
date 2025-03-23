import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
import logging

# 日志
logging.basicConfig(level=logging.INFO,format="%(asctime)s-%(levelname)s-%(message)s")

# 爬取函数
def scrape_quotes(pages=3):
    quotes_data = []
    # 遍历页面
    for page in range(1,pages+1):
        url = f"https://quotes.toscrape.com/page/{page}/"
        logging.info(f"正在爬取第{page}页:{url}...")

        try:
            response = requests.get(url)
            response.raise_for_status()
            # 解析网页
            soup = BeautifulSoup(response.text,"html.parser")
            # 找到所有块
            quotes_blocks = soup.find_all("div",class_="quote")
            # 遍历所有块
            for quote in quotes_blocks:
                # 提取
                quote_text = quote.find("span", class_="text").text.strip()
                author = quote.find("small", class_="author").text.strip()

                tags = [tag.text for tag in quote.find_all("a",class_="tag")]  
                quotes_data.append({ 
                    "quote": quote_text,
                    "author": author,
                    "tags": tags 
                    })
            sleep(1)

        except requests.RequestException as i:
            logging.error(f"爬取第{page}页时出错：{i}")
            continue
    return quotes_data
def main():
    logging.info("开始爬取...")
    quotes_data = scrape_quotes(pages=3)  

    logging.info("转化为DataFrame...")
    df = pd.DataFrame(quotes_data) 

    logging.info("开始清洗...")
    # 去除重复引用(基于基于quote列)
    df_before = len(df)
    df = df.drop_duplicates(subset=['quote'])
    df_after = len(df)
    logging.info(f"清洗了{df_before-df_after}条重复数据")

    # 清除空值
    df = df.dropna()

    # 清理引用文本（移除多余的引号）
    df['quote'] = df['quote'].str.replace('"','',regex=True)
    
    # 4. 将标签列表转换为字符串
    df['tags'] = df['tags'].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)
    
    #统计
    logging.info("进行基本统计分析...")
    print("\n=== 数据概览 ===")
    print(f"总引用数: {len(df)}")
    print(f"不同作者数: {df['author'].nunique()}")
    print("\n最常出现的作者:")
    print(df['author'].value_counts().head())

    output_file = "cleaned_quotes.csv"
    df.to_csv(output_file,index=False,encoding="utf-8")
    logging.info(f"数据已保存到 {output_file}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.info(f"程序出错：{e}")