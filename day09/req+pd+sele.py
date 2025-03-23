# 抓取'http://quotes.toscrape.com/'第一页所有引用和作者
# 将抓取到的数据存入Pandas DataFrame
# 将DataFrame存为CSV文件

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
try:
    driver.get(r"http://quotes.toscrape.com/")
    WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME,"text"))
    )
    quotes = driver.find_elements(By.CLASS_NAME,"text")
    authors = driver.find_elements(By.CLASS_NAME,"author")
    quotes_data = [{'Quotes':q.text,'Authors':a.text} for q,a in zip(quotes,authors)]
    df = pd.DataFrame(quotes_data)
    print("抓取数据：\n",df)
    df.to_csv("quotes_with_authors.csv",index=False)
    print("\n保存为quotes_with_authors.csv成功!")
except Exception as e:
    print(f'发生异常{e}')

finally:
    driver.quit()