class Locators():
    # Home Page Objects
    sign_in_button_link_text = "Sign in"
    contact_us_button_link_text = "Contact us"
    # Login Page Objects
    email_textbox_id = "email"
    password_textbox_id = "passwd"
    submit_login_button_link_text = "SubmitLogin"
    # Contact Us Page Objects
    subject_heading_customer_service_xpath = "//select[@id='id_contact']/option[text()='Customer service']"
    subject_heading_webmaster_xpath = "//select[@id='id_contact']/option[text()='Webmaster']"
    select_subject_id = "id_contact"
    send_button_id = 'submitMessage'
    message_textbox_id = 'message'