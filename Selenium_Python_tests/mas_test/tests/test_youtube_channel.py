import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from page_objects.youtube_channel_page import YouTubeChannelPage

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

def test_youtube_channel(driver):
    driver.get("https://www.youtube.com/@magalicazellamendez5809")
    channel_page = YouTubeChannelPage(driver)
    channel_title = channel_page.get_channel_title()
    assert "Magali Cazella Mendez" in channel_title
