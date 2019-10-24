import time
from tests.POM_Demo.Pages.LoginPage import LoginPage
from tests.POM_Demo.Pages.LandingPage import LandingPage
from tests.POM_Demo.Pages.DressesPage import DressesPage
from tests.POM_Demo.Pages.ProductPage import ProductPage


def test_add_to_cart(driver):
    driver.get("http://automationpractice.com")
    login = LoginPage(driver)
    login.click_on_sign_in()
    # time.sleep(2)
    login.enter_email(username="admin12345@gmail.com")
    login.enter_password(password="admin123")
    # time.sleep(2)
    login.click_submit_login()

    home = LandingPage(driver)
    home.select_option_from_menu("dresses")

    dresses = DressesPage(driver)
    dresses.select_option_from_subcategory("summer dresses")
    dresses.select_random_product()

    product = ProductPage(driver)
    product.select_quantity("2")
    product.select_size("L")
    product.select_random_colour()
    product.add_cart()
    product.proceed_checkout()
    product.proceed_cart_checkout()
    product.proceed_cart_checkout()
    product.check_terms_of_service()
    product.proceed_cart_checkout()
    product.select_pay_by_bank()
    product.proceed_cart_checkout()
    product.validate_order_complete_message("Your order on My Store is complete.")

