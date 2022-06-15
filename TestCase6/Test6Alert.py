import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
#Trouver le bouton click de JSALERT
driver.find_element(By.XPATH,"//button[contains(text(),'Alert')]").click()
#recuperer l'alerte
alertWindow = driver.switch_to.alert

print(alertWindow.text)

#cliquer  sur le bouton ok de l'alerte
alertWindow.accept()

time.sleep(3)
driver.quit()