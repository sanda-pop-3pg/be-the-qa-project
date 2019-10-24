from time import sleep

class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.sign_in_button_link_text = "Sign in"
        self.contact_us_button_link_text = "Contact us"
        self.driver.get("http://automationpractice.com")

    def click_sign_in(self):
        self.driver.find_element_by_link_text(self.sign_in_button_link_text).click()
        sleep(3)


    def click_contact_us(self):
        self.driver.find_element_by_link_text(self.contact_us_button_link_text).click()
        sleep(3)