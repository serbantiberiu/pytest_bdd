from pytest_bdd import scenario, given, when, then
from BDD_POM.locators.Locators import LoginpageLocators
from BDD_POM.pages.Home_page import Homepage

scenario('../features/form_authentication.feature', 'Find Form Authentication')


@given('Open Homepage')
@when("Find Form Authentication and click on it")
@then('Redirect to Loginpage')
def test_form_authentication_page(browser):
    homepage = Homepage(browser)
    homepage.load_home_page()
    homepage.click_elements("Form Authentication")
    assert browser.current_url == LoginpageLocators.URL, "Login page not displayed."
