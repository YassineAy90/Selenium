import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://demo.nopcommerce.com")
# 1ere option
driver.find_element(By.LINK_TEXT, "Register").click()
# Ou bien 2eme option ==>
# driver.find_element(By.PARTIAL_LINK_TEXT,"Regi").click()

driver.find_element(By.ID, "FirstName").send_keys('TEST112')
driver.find_element(By.NAME, "LastName").send_keys('1TEST2')
driver.find_element(By.ID, "Email").send_keys("TEST@TEST.fr")
driver.find_element(By.ID, "Password").send_keys("azerty")
driver.find_element(By.ID, "ConfirmPassword").send_keys("azerty")
driver.find_element(By.ID, "register-button").click()

#https://www.saucedemo.com
#Entrer dans site
# selectionner article
# ajouter article
# cancel
# retourner sur panier
# supprimer article




#Syntaxe general de Xpath
#tagname[@attribut="value"]

#driver.close()
