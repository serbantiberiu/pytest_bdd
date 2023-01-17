from pytest_bdd import scenario, given, when, then
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec

from BDD_POM.locators import Locators
from BDD_POM.locators.Locators import LoginpageLocators
from BDD_POM.pages.Login_page import Loginpage
from BDD_POM.pages.Secure_page import Securepage

scenario('../features/successful_logout.feature', 'Logout Successfully')


@given('The user in logged into the application')
@when('the user clicks logout btn')
@then('the user is redirected to Login page')
def test_logout_page(browser):
    login = Loginpage(browser)
    login.load_login_page()
    login.type_username(Locators.Credentials.USERNAME)
    login.type_password(Locators.Credentials.PASSWORD)
    login.click_login()
    Securepage(browser).click_logout()
    success_message = Loginpage(browser).get_message()
    assert browser.current_url == LoginpageLocators.URL, "login page URL is not ok."
    assert success_message == Locators.SuccessMesages.LOGOUT, \
        'successfully logout message not displayed'
