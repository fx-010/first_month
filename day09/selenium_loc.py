# 用selenium打开百度，搜索Python
# 抓取第一页第一个搜索结果的标题
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get(r"http://www.baidu.com/")
search_box = driver.find_element(By.ID,'kw')
search_box.send_keys('Python')
search_box.send_keys(Keys.RETURN)

first_result = WebDriverWait(driver,10).until(
    # 使用element获取第一个元素
    EC.presence_of_element_located((By.XPATH,'//h3/a'))
)
print('第一个搜索结果是：',first_result.text)

driver.quit()