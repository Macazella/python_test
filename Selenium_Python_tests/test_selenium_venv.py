from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Ruta al ChromeDriver
chrome_driver_path = 'C:\\Users\\magal\\pip Python Selenium\\chromedriver.exe'

# Configuración de opciones de Chrome (opcional)
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Puedes comentar esta línea si quieres ver el navegador

# Configuración del WebDriver
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Intenta abrir la página web
try:
    print("Intentando abrir la página...")
    driver.get('https://github.com/Macazella')
    print("Página abierta.")
    
    # Espera para ver la página
    time.sleep(10)  # Espera 10 segundos para que puedas ver la página
finally:
    # Cierra el navegador
    print("Cerrando el navegador...")
    driver.quit()
    print("Navegador cerrado.")

