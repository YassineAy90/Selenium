import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.opencart.com/index.php?route=account/register")

dropdown=driver.find_element(By.ID,"input-country")
country= Select(dropdown)
#country.select_by_visible_text("Monaco")
#time.sleep(3)

#country.select_by_index(6)
#time.sleep(3)

##country.select_by_value("167")
#time.sleep(3)

all_options= country.options


total_options=len(all_options)
print ("le nombre total d'options:", total_options)

#for opt in all_options:
    #print(opt.text)

for opt in all_options:
    if opt.text == "Canada":
        opt.click()
        break





