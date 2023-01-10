from selenium.webdriver.common.by import By
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

class SecurepageLocators:
    URL="https://the-internet.herokuapp.com/secure"
    success_msg=(By.CLASS_NAME,'flash success')
    logout_btn=(By.CLASS_NAME,'button secondary radius')








