from selenium import webdriver

driver=webdriver.Chrome()

driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")

url_page = driver.current_url

print(url_page)
#Obtenir l'URL de la page
# obtenir le code source de la page