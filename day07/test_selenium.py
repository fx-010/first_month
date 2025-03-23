from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")   
driver_box = driver.find_element(By.ID,'kw')
driver_box.send_keys('python')

# 直接用click点击防止回车键未生效
search_button = driver.find_element(By.ID,"su")
search_button.click()
time.sleep(3)

print(driver.title)
driver.quit()