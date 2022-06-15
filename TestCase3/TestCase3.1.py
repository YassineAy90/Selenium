import time

from selenium import webdriver

driver=webdriver.Chrome()

driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")

time.sleep(2)

driver.get("https://www.google.ca")
time.sleep(2)

driver.back()
time.sleep(2)
driver.close()