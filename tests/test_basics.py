from pages.simple_button_page import SimpleButtonPage
from time import sleep

def test_click_button(driver):
    simple_button = SimpleButtonPage(driver)
    simple_button.open_simple_button_page()
    simple_button.click_button()
    sleep(2)


    # driver.get("https://www.qa-practice.com/elements/button/simple")
    # button = driver.find_element(By.ID, "submit-id-submit")
    # button.click()

