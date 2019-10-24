from tests.POM_Demo.Locators.locators import Locators

class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.sign_in_button_link_text = Locators.sign_in_button_link_text
        self.email_textbox_id = "email"
        self.password_textbox_id = "passwd"
        self.submit_login_button_id = "SubmitLogin"
        self.sign_out_button_link_text = "Sign out"

    def click_on_sign_in(self):
        self.driver.find_element_by_link_text(self.sign_in_button_link_text).click()

    def enter_email(self, username):
        self.driver.find_element_by_id(self.email_textbox_id).clear()
        self.driver.find_element_by_id(self.email_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_submit_login(self):
        self.driver.find_element_by_id(self.submit_login_button_id).click()

    def click_sign_out(self):
        self.driver.find_element_by_link_text(self.sign_out_button_link_text).click()

    def validate_sign_in(self):
        sign_out_button = self.driver.find_element_by_link_text(self.sign_out_button_link_text)
        assert sign_out_button.text == "Sign out", "Sign out button message doesn't match"
