from pytest_bdd import scenario, given, when, then
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from BDD_POM.Locators.Locators import LoginpageLocators
from BDD_POM.Pages.Secure_page import Securepage

@scenario('../features/Securepage.features','Check if Login Succesfully')
def test_secure_page():
    pass

@given('Open Securepage')
def load_page(browser):
    Securepage(browser).load_page()
    print("\n---Step 1---Given---Pass---")

@when("Find succes message")
def check_message_is_displayed(browser):
    assert Securepage(browser).get_message().lower()== ' You logged into a secure area!'
    print("\n---Step 2---When---Pass---")

@when('Click logout btn')
def click_logout(browser):
    Securepage(browser).click_logout()
    print("\n---Step 3---When---Pass---")

@then ('Redirect Securepage')
def check_redirect_to_page(browser):
    webdriver.Wait(browser,5).until(ec.url_changes(LoginpageLocators.URL))
    assert browser.current_url == LoginpageLocators.URL, "Main page URL is not ok."
