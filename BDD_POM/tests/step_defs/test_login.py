from pytest_bdd import scenario, given, when, then
from BDD_POM.locators import Locators
from BDD_POM.locators.Locators import SecurepageLocators
from BDD_POM.pages.Login_page import Loginpage
from BDD_POM.pages.Secure_page import Securepage

scenario('../features/successful_login.feature', 'Login successfully')


@given('Open Loginpage')
@when('The user inserts credentials and clicks login button')
@then('Login is successful')
def test_login_page(browser):
    login = Loginpage(browser)
    login.load_login_page()
    login.type_username(Locators.Credentials.USERNAME)
    login.type_password(Locators.Credentials.PASSWORD)
    login.click_login()
    success_message = Securepage(browser).get_message()
    assert browser.current_url == SecurepageLocators.URL,\
        "User was not redirected to the correct page after login."
    assert success_message == Locators.SuccessMesages.LOGIN,\
        'successfully login message not displayed'
