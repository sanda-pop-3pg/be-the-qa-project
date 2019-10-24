from selenium.webdriver.support.select import Select
from random import randrange


class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.quantity = "quantity_wanted"
        self.size_drop_down = "group_1"
        self.colour_list = "#color_to_pick_list li a"
        self.add_to_cart = "#add_to_cart button"
        self.checkout = "Proceed to checkout"
        self.cart_checkout = ".cart_navigation  i.icon-chevron-right"
        self.terms_of_service = "uniform-cgv"
        self.bank_pay = "Pay by bank wire"
        self.order_complete_message = "p.cheque-indent"

    def select_quantity(self, quantity):
        quantity_input = self.driver.find_element_by_id(self.quantity)
        quantity_input.clear()
        quantity_input.send_keys(quantity)

    def select_size(self, size):
        sub = Select(self.driver.find_element_by_id(self.size_drop_down))
        sub.select_by_visible_text(size)

    def select_random_colour(self):
        colours = self.driver.find_elements_by_css_selector(self.colour_list)
        random_color = randrange(len(colours))
        colours[random_color].click()

    def add_cart(self):
        self.driver.find_element_by_css_selector(self.add_to_cart).click()

    def proceed_checkout(self):
        self.driver.find_element_by_link_text(self.checkout).click()

    def proceed_cart_checkout(self):
        self.driver.find_element_by_css_selector(self.cart_checkout).click()

    def check_terms_of_service(self):
        self.driver.find_element_by_id(self.terms_of_service).click()

    def select_pay_by_bank(self):
        self.driver.find_element_by_partial_link_text(self.bank_pay).click()

    def validate_order_complete_message(self, message):
        grabbed_message = self.driver.find_element_by_css_selector(self.order_complete_message).text
        assert grabbed_message == message, "Order complete message doesn't match"
