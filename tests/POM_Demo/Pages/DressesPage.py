from random import randrange


class DressesPage:

    def __init__(self, driver):
        self.driver = driver
        self.subcategories = "#subcategories .subcategory-image a"
        self.product_list = ".product_list a.product_img_link"

    def select_option_from_subcategory(self, option):
        subcategory_list = self.driver.find_elements_by_css_selector(self.subcategories)
        for item in subcategory_list:
            if item.get_attribute("title").lower().strip() == option.lower():
                item.click()
                return
        else:
            raise ValueError("Submenu option was not found!")

    def select_random_product(self):
        products = self.driver.find_elements_by_css_selector(self.product_list)
        random_product = randrange(len(products))
        products[random_product].click()



