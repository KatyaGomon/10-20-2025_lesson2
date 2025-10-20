from selenium.webdriver.common.by import By

class SimpleButtonPage:
    def __init__(self, driver):
        self.driver = driver

    def open_simple_button_page(self):
        self.driver.get("https://www.qa-practice.com/elements/button/simple")

    def click_button(self):
        button = self.driver.find_element(By.ID, "submit-id-submit")
        button.click()