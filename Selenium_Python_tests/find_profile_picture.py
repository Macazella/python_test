from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Especifica la ruta al chromedriver
chrome_driver_path = 'C:/Users/magal/pip Python Selenium/chromedriver.exe'

# Configura el WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Abre la página web
    driver.get("https://github.com/Macazella")

    # Espera a que la página cargue
    time.sleep(5)

    # Encuentra la foto de perfil usando XPath
    profile_image = driver.find_element(By.XPATH, '//img[contains(@class, "avatar") and contains(@class, "avatar-user")]')

    # Imprime la URL de la foto de perfil
    print("URL de la foto de perfil:", profile_image.get_attribute("src"))

    # Captura una imagen de la página
    driver.save_screenshot('screenshot.png')
    print("Captura de pantalla guardada como 'screenshot.png'.")

finally:
    # Cierra el navegador
    driver.quit()
