from time import sleep

from BDD_POM.locators.Locators import SecurepageLocators


class Securepage:
    def __init__(self, browser):
        self.browser = browser

    def load_secure_page(self):
        self.browser.get(SecurepageLocators.URL)

    def get_message(self):
        return self.browser.find_element(*SecurepageLocators.success_msg).text

    def click_logout(self):
        self.browser.find_element(*SecurepageLocators.logout_btn).click()
