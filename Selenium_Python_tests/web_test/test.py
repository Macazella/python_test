from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Ruta del chromedriver
chromedriver_path = 'C:/Users/magal/pip Python Selenium/chromedriver.exe'

# Configurar el driver usando ChromeOptions
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--headless')  # Comentado para ver la interfaz gráfica
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920,1080')

# Iniciar el driver de Chrome
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

# Abrir el archivo HTML
driver.get('file:///C:/Users/magal/pip%20Python%20Selenium/web_test/index.html')

# Esperar 10 segundos
time.sleep(10)

# Obtener y hacer clic en el botón de confirmación
confirm_button = driver.find_element("xpath", '//button[text()="Confirm"]')
confirm_button.click()

# Esperar un momento para que el alert aparezca
time.sleep(2)

# Aceptar el alert
alert = driver.switch_to.alert
alert.accept()

# Imprimir mensaje de éxito
print("La prueba se ejecutó correctamente.")

# Cerrar el navegador
driver.quit()
