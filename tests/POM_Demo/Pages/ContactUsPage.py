from selenium.webdriver.support.select import Select


class ContactUsPage():

    def __init__(self, driver):
        self.driver = driver

        self.contact_us_button_id = "contact-link"
        self.subject_heading_dropdown_id = "id_contact"
        self.email_textbox_id = "email"
        self.id_order_textbox_id = "id_order"
        self.message_textbox_id = "message"
        self.send_button_id = "submitMessage"

    def click_contact_us(self):
        self.driver.find_element_by_id(self.contact_us_button_id).click()

    def select_subject_heading(self,subject):
        var = Select(self.driver.find_element_by_id(self.subject_heading_dropdown_id))
        var.select_by_visible_text(subject)

    def enter_email(self, email):
        self.driver.find_element_by_id(self.email_textbox_id).clear()
        self.driver.find_element_by_id(self.email_textbox_id).send_keys(email)

    def enter_id_order(self, no_order):
        self.driver.find_element_by_id(self.id_order_textbox_id).clear()
        self.driver.find_element_by_id(self.id_order_textbox_id).send_keys(no_order)

    def enter_message(self, message):
        self.driver.find_element_by_id(self.message_textbox_id).clear()
        self.driver.find_element_by_id(self.message_textbox_id).send_keys(message)

    def click_send(self):
        self.driver.find_element_by_id(self.send_button_id).click()





