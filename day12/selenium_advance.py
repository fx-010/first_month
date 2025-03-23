from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("http://quotes.toscrape.com/login")


username = driver.find_element(By.ID,"username")
password = driver.find_element(By.ID,"password")
username.send_keys("123456")
password.send_keys("1234567890")
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
print("网址标题是：",driver.title)

# 打开about
WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.CLASS_NAME,"quote"))
)
quote_link = driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div[1]/span[2]/a[1]")
quote_link.click()



time.sleep(3)

author_info = driver.find_element(By.CLASS_NAME,"author-title").text
print("作者信息：",author_info)

driver.quit()