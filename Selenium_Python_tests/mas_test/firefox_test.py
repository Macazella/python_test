from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurar opciones de Firefox
options = Options()
# Descomenta la línea de abajo para ejecutar en modo headless
# options.add_argument("--headless")

# Inicializar el controlador de Firefox
try:
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
    print("Navegador Firefox abierto con éxito.")

    # Navegar a la URL
    driver.get("https://github.com/Macazella")
    print("Navegado a https://github.com/Macazella")

    # Esperar a que la página se cargue completamente
    WebDriverWait(driver, 30).until(lambda d: d.execute_script('return document.readyState') == 'complete')

    try:
        # Localizar el elemento usando el XPath actualizado
        link = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/Macazella?tab=repositories"]'))
        )
        
        # Desplazar el elemento a la vista si es necesario
        driver.execute_script("arguments[0].scrollIntoView(true);", link)
        
        # Hacer clic en el enlace
        link.click()
        print("Clic ejecutado con éxito.")
    except Exception as e:
        print(f"No se pudo ejecutar el clic: {e}")

finally:
    # Mantener el navegador abierto durante 10 segundos antes de cerrarlo
    time.sleep(10)
    # Cerrar el navegador
    driver.quit()
