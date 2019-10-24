class LandingPage:

    def __init__(self, driver):
        self.driver = driver
        self.menu_option_list = "ul.menu-content>li>a"

    def select_option_from_menu(self, option):
        menu_list = self.driver.find_elements_by_css_selector(self.menu_option_list)
        for item in menu_list:
            if item.text.lower() == option.lower():
                item.click()
                return
        else:
            raise ValueError("Menu option was not found!")



