from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.thegioididong.com/dtdd")
time.sleep(3)

# Chờ trang tải xong
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".item")))

# Lấy danh sách sản phẩm
products = driver.find_elements(By.CSS_SELECTOR, ".item.ajaxed.__cate_42")
phone_list = []
for product in products:
    try:
        name = product.find_element(By.CSS_SELECTOR, "h3").text
        price = product.find_element(By.CSS_SELECTOR, ".price").text
        phone_list.append({"name": name, "price": price})
    except Exception as e:
        print(f"Lỗi: {e}")
        continue

# In kết quả
for phone in phone_list:
    print(f"Ten: {phone['name']}, Gia: {phone['price']}")

driver.quit()
