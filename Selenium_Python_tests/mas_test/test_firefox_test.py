import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    # Configurar opciones de Firefox
    options = Options()
    # Inicializar el controlador de Firefox
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
    yield driver
    driver.quit()

def test_navegacion_github(driver):
    # Navegar a la URL
    driver.get("https://github.com/Macazella")
    assert "Macazella" in driver.title

    # Esperar a que el elemento sea clickeable
    try:
        link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/Macazella?tab=repositories"]'))
        )
        # Desplazar el elemento a la vista
        driver.execute_script("arguments[0].scrollIntoView(true);", link)
        # Hacer clic en el enlace
        link.click()
        
        # Esperar a que la nueva URL sea cargada
        WebDriverWait(driver, 20).until(lambda d: "repositories" in d.current_url)
        assert "repositories" in driver.current_url
    except Exception as e:
        pytest.fail(f"Prueba fallida debido a: {e}")
