from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.by import By

import time 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://texnomart.uz")

time.sleep(10)
button_shop = driver.find_element(By.CSS_SELECTOR, "#product-link356110 > div.product-item-component > div.product-bottom > div.product-bottom__right.flex.flex-col.items-start.justify-between > div.d-flex.align-center.justify-between.w-full > button")
button_shop.click()

button_shop1 = driver.find_element(By.CSS_SELECTOR, "#product-link356105 > div.product-item-component > div.product-bottom > div.product-bottom__right.flex.flex-col.items-start.justify-between > div.d-flex.align-center.justify-between.w-full > button")
button_shop1.click()
button_shop2 = driver.find_element(By.CSS_SELECTOR, "#product-link356106 > div.product-item-component > div.product-bottom > div.product-bottom__right.flex.flex-col.items-start.justify-between > div.d-flex.align-center.justify-between.w-full > button ")
button_shop2.click()
time.sleep(4)

shop = driver.find_element(By.ID,"header-basket")
shop.click()

time.sleep(7)
# # Taking the image
# driver.save_screenshot("image.png")
# # Loading the image
# image = Image.open("image.png")
# # Showing the image
# image.show()

# driver.execute_script("windows.scrollTO(0,document.body.scrollHeight)")


time.sleep(3)
driver.close()