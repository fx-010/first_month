# 核心模块，启动浏览器
from selenium import webdriver
# 提供定位元素方式
from selenium.webdriver.common.by import By
# 提供显式等待功能；提供各种等待条件
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 用来配置ChromeDriver的服务；第三方库，自动下载与管理ChromeDriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
# 打开目标网站
driver.get(r"http://quotes.toscrape.com")

try:
    # 等待“Next”按钮可点击，并点击它
    next_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Next"))# 模糊搜索
    )
    next_btn.click()

    # 等待页面加载完成，定位第2页的第一条引用
    first_quote = WebDriverWait(driver, 10).until(
        # EC.presence_of_element_located()只接受一个元素，所以传一个元组即(By.CLASS_NAME, "text")
        EC.presence_of_element_located((By.CLASS_NAME, "text"))
    ).text

    # 打印第2页的第一条引用
    print("第2页第一条引用：", first_quote)
    

except Exception as e:
    print("出现错误：", e)

finally:
    # 关闭浏览器
    driver.quit()