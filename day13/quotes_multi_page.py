from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

driver = webdriver.Chrome()
driver.get("http://quotes.toscrape.com/login")
username = driver.find_element(By.ID,"username").send_keys("123456")
password = driver.find_element(By.ID,"password").send_keys("1234567890")
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
print("网址标题是：",driver.title)

all_quotes = []
all_authors = []
while True:
    quotes = driver.find_elements(By.CLASS_NAME,"text")
    authors = driver.find_elements(By.CLASS_NAME,"author")
    all_quotes.extend([q.text for q in quotes])
    all_authors.extend([a.text for a in authors])
    try:
        next_button = driver.find_element(By.CSS_SELECTOR,".next a")
        next_button.click()
    except:
        break
data = {"Quotes":all_quotes,"Authors":all_authors}
df = pd.DataFrame(data)
df.to_csv("quotes_multi.csv",index=False)
driver.quit
print(f"已经爬取{len(all_quotes)}条引言,保存到quotes_multi.csv")