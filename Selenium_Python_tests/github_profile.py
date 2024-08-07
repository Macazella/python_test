from selenium import webdriver

# Configura el driver para usar Chrome
driver = webdriver.Chrome()

# Navega a tu perfil de GitHub
driver.get("https://github.com/Macazella")

# Imprime el título de la página
print("Title of the page is:", driver.title)

# Espera 10 segundos para que puedas ver la página antes de cerrarla
import time
time.sleep(30)

# Cierra el navegador
driver.quit()
