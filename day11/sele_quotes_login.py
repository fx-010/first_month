from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
try:
    driver = webdriver.Chrome()
    driver.get('http://quotes.toscrape.com/login')

    username = driver.find_element(By.ID,'username')
    password = driver.find_element(By.ID,'password')
    username.send_keys('testuser')
    password.send_keys('testpassword')

    login_botten = driver.find_element(By.CSS_SELECTOR,"input[type='submit']")
    login_botten.click()

    # 预定义条件，可以检查网页url是否变化
    WebDriverWait(driver,10).until(EC.url_contains('quotes'))
    print('登录后标题：',driver.title)
finally:
    driver.quit()