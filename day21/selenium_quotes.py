from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()

driver.get(r'http://quotes.toscrape.com/')

quotes_list = []
authors_list = []

while True:
    # quotes = driver.find_elements(By.CLASS_NAME,'text')
    # authors = driver.find_elements(By.CLASS_NAME,'text')

    quotes = [q.text for q in driver.find_elements(By.CLASS_NAME,'text')]
    authors = [a.text for a in driver.find_elements(By.CLASS_NAME,'text')]

    quotes_list.extend(quotes)
    authors_list.extend(authors)

    try:
        next_button = driver.find_element(By.LINK_TEXT,'Next →')# 精准搜索，注意格式
        # next_button = driver.find_element(By.PARTIAL_LINK_TEXT, 'Next')模糊搜索，可能搜索多个值
        # next_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div[1]/span[2]/a[1]")Xpath搜索，网站可能不稳定；CSS类似
        next_button.click()
        time.sleep(3)
    except:
        break

df = pd.DataFrame({'quotes':quotes_list,'authors':authors_list})
df.to_csv("quotes.csv", index=False)
print(df)
print("已保存数据到 quotes21.csv")
driver.quit()