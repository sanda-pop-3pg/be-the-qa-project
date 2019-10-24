import time
from tests.POM_Demo.Pages.LoginPage import LoginPage
from tests.POM_Demo.Pages.ContactUsPage import ContactUsPage

def test_login_valid(driver):
    driver.get("http://automationpractice.com")
    driver.implicitly_wait(10)
    driver.maximize_window()
    print(driver.title)
    # driver.find_element_by_link_text("Sign in").click()
    # time.sleep(2)
    # driver.find_element_by_id("email").clear()
    # driver.find_element_by_id("email").send_keys("admin12345@gmail.com")
    # driver.find_element_by_id("passwd").clear()
    # driver.find_element_by_id("passwd").send_keys("admin123")
    # driver.find_element_by_id("SubmitLogin").click()
    # driver.find_element_by_link_text("Sign out").click()

    login = LoginPage(driver)
    login.click_on_sign_in()
    time.sleep(2)
    login.enter_email(username="admin12345@gmail.com")
    login.enter_password(password="admin123")
    time.sleep(2)
    login.click_submit_login()
    time.sleep(2)

    login.validate_sign_in()

    login.click_sign_out()

    # contact = ContactUsPage(driver)
    # contact.click_contact_us()
    # time.sleep(2)
    # contact.select_subject_heading("Webmaster")
    # contact.enter_email("admin12345@gmail.com")
    # contact.enter_id_order("12345")
    # contact.enter_message("Dress to impress")
    # contact.click_send()




