from selenium import webdriver
from selenium.webdriver.common.by import By

# Configura el driver para usar Chrome
driver = webdriver.Chrome()

# Navega a una página web
driver.get("https://www.example.com")

# Imprime el título de la página
print("Title of the page is:", driver.title)

# Cierra el navegador
driver.quit()
