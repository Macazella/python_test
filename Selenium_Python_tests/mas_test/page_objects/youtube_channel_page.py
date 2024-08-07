from selenium.webdriver.common.by import By

class YouTubeChannelPage:
    def __init__(self, driver):
        self.driver = driver
        self.channel_title_locator = (By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[3]/ytd-tabbed-page-header/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/div/div/yt-page-header-renderer/yt-page-header-view-model/div/div[1]/div/yt-dynamic-text-view-model/h1/span')

    def get_channel_title(self):
        title_element = self.driver.find_element(*self.channel_title_locator)
        return title_element.text
