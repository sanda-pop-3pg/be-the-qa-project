from time import sleep

from selenium.webdriver.support.select import Select


class ContactUs():
    def __init__(self, driver):
        self.driver = driver
        self.sign_in_button_link_text = "Sign in"
        self.contact_us_button_link_text = "Contact us"
        self.subject_heading_customer_service_xpath = "//select[@id='id_contact']/option[text()='Customer service']"
        self.subject_heading_webmaster_xpath = "//select[@id='id_contact']/option[text()='Webmaster']"
        self.select_subject_id = "id_contact"
        self.email_textbox_id = 'email'
        self.send_button_id = 'submitMessage'
        self.message_textbox_id = 'message'

    def select_subject_heading(self, subject):
        sub = Select(self.driver.find_element_by_id(self.select_subject_id))
        sub.select_by_visible_text(subject)
        sleep(3)

    def enter_email(self, email):
        self.driver.find_element_by_id(self.email_textbox_id).send_keys(email)
        sleep(3)

    def enter_message(self, message):
        self.driver.find_element_by_id(self.message_textbox_id).send_keys(message)
        sleep(3)

    def click_submit_message(self):
        self.driver.find_element_by_id(self.send_button_id).click()
        sleep(3)