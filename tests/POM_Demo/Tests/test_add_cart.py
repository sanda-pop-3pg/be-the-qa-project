import time
from tests.POM_Demo.Pages.LoginPage import LoginPage
from tests.POM_Demo.Pages.LandingPage import LandingPage


def test_add_to_cart(driver):
    driver.get("http://automationpractice.com")
    login = LoginPage(driver)
    login.click_on_sign_in()
    # time.sleep(2)
    login.enter_email(username="admin12345@gmail.com")
    login.enter_password(password="admin123")
    # time.sleep(2)
    login.click_submit_login()

    homepage = LandingPage(driver)
    homepage.select_option_from_menu("dresses")
    time.sleep(5)
