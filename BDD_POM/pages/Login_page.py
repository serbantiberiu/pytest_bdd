from time import sleep

from BDD_POM.locators.Locators import LoginpageLocators


class Loginpage:
    def __init__(self, browser):
        self.browser = browser

    def load_login_page(self):
        self.browser.get(LoginpageLocators.URL)
        sleep(3)

    def type_username(self, user):
        self.browser.find_element(*LoginpageLocators.user).send_keys(user)

    def type_password(self, password):
        self.browser.find_element(*LoginpageLocators.password).send_keys(password)

    def click_login(self):
        self.browser.find_element(*LoginpageLocators.login_btn).click()
    def get_message(self):
        return self.browser.find_element(*LoginpageLocators.success_msg).text