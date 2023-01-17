from selenium.webdriver.common.by import By

class Credentials:
    USERNAME = 'tomsmith'
    PASSWORD = 'SuperSecretPassword!'
class HomepageLocators:
    URL="https://the-internet.herokuapp.com/"
    checkboxes = (By.LINK_TEXT, 'Checkboxes')
    dropdown = (By.LINK_TEXT, 'Dropdown')
    formy = (By.LINK_TEXT, 'Form Authentication')
    frames=(By.LINK_TEXT,'Frames')
    inputs=(By.LINK_TEXT,'Inputs')

class LoginpageLocators:
    URL="https://the-internet.herokuapp.com/login"
    user = (By.NAME, 'username')
    password = (By.NAME, 'password')
    login_btn = (By.CLASS_NAME, 'radius')
    success_msg = (By.ID, 'flash')

class SecurepageLocators:
    URL="https://the-internet.herokuapp.com/secure"
    success_msg=(By.ID,'flash')
    logout_btn=(By.XPATH,'//*[@class="button secondary radius"]')

class SuccessMesages:
    LOGIN = 'You logged into a secure area!\n×'
    LOGOUT = 'You logged out of the secure area!\n×'






