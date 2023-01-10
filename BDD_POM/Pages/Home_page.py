from time import sleep
from BDD_POM.Locators.Locators import HomepageLocators

class Homepage:
    def __init__(self,browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(HomepageLocators.URL)
        sleep(3)

    def click_elements(self, button):
        if button == "Checkboxes":
            self.browser.find_element(*HomepageLocators.checkboxes).click()
            print("\nClick!")
        elif button == "Dropdown":
            self.browser.find_element(*HomepageLocators.dropdown).click()
            print("\nClick!")
        elif button == "Form Authentication":
            self.browser.find_element(*HomepageLocators.formy).click()
            print("\nClick!")
        elif button == "Frames":
            self.browser.find_element(*HomepageLocators.frames).click()
            print("\nClick!")
        elif button == "Inputs":
            self.browser.find_element(*HomepageLocators.inputs).click()
            print("\nClick!")




