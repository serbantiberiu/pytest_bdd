from pytest_bdd import scenario, given, when, then
from selenium.webdriver.support import expected_conditions as ec
from BDD_POM.Locators.Locators import SecurepageLocators
from BDD_POM.Pages.Login_page import Loginpage

scenario('../features/login_page.feature', 'Login succesfully')

@given('Open Loginpage')
def load_page(browser):
    Loginpage(browser).load_page()
    print("\n---Step 1---Given---Pass---")

@when("Introduce username")
def type_username(user):
    Loginpage(user).type_username('tomsmith')
    print("\n---Step 2---When---Pass---")

@when("Introduce password")
def type_password(password):
    Loginpage(password).type_password('SuperSecretPassword!')
    print("\n---Step 3---When---Pass---")

@when("Click Login")
def click_login(browser):
    Loginpage(browser).click_login()
    print("\n---Step 4---When---Pass---")

@then ('Redirect Securepage')
def check_redirect_to_page(browser):
    Webdriver.Wait(browser,5).until(ec.url_changes(SecurepageLocators.URL))
    assert browser.current_url == SecurepageLocators.URL, "Main page URL is not ok."
    print("\n---Step 5---Then---Pass---")