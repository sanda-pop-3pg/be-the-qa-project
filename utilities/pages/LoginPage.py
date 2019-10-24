import time
from utilities.locators.locators import Locators

class LoginPage():
    def __init__(self, driver):
        # self.sign_in_button_link_text = "Sign in"
        # self.email_textbox_id = "email"
        # self.password_textbox_id = "passwd"
        # self.submit_login_button_link_text= "SubmitLogin"
        self.driver = driver



        self.sign_in_button_link_text = Locators.sign_in_button_link_text
        self.email_textbox_id = Locators.email_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.submit_login_button_link_text = Locators.submit_login_button_link_text

    # def click_sign_in(self):
    #     self.driver.get("http://automationpractice.com")
    #     self.driver.find_element_by_link_text(self.sign_in_button_link_text).click()
    #     time.sleep(3)

    def enter_email(self, username):
        self.driver.find_element_by_id(self.email_textbox_id).clear()
        time.sleep(2)
        self.driver.find_element_by_id(self.email_textbox_id).send_keys(username)
        time.sleep(2)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        time.sleep(2)
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)
        time.sleep(2)

    def click_submit_login(self):
        self.driver.find_element_by_id(self.submit_login_button_link_text).click()
        time.sleep(2)