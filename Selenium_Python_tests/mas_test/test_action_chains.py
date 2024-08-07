import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  # Importa el módulo time para añadir una pausa

@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
    yield driver
    driver.quit()

def test_action_chains(driver):
    # Navegar a la URL
    driver.get("https://github.com/Macazella")

    # Esperar a que el elemento esté disponible
    element_to_hover_over = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="user-profile-frame"]/div/div[1]/div/article/ul/li[5]/a[2]'))
    )

    # Crear un objeto ActionChains
    actions = ActionChains(driver)
    
    # Realizar la acción de hover y clic en el elemento
    actions.move_to_element(element_to_hover_over).click().perform()

    # Validar que se ha realizado el clic correctamente
    assert "Macazella" in driver.title  # Cambia la verificación según sea necesario
    
    # Pausa para revisión manual (10 segundos en este caso)
    time.sleep(10)
