import pytest
from pytest_bdd import scenario, given, when, then
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from BDD_POM.Locators.Locators import LoginpageLocators
from BDD_POM.Pages.Home_page import Homepage


scenario('../features/form_authentification.feature', 'Find Form Authentification')

@given('Open Homepage')
def load_page(browser):
    Homepage(browser).load_page()
    print("\n---Step 1---Given---Pass---")

@when("Find Form Authentication and click on it")
def click_on_element(button):
    Homepage(button).click_elements("Form Authentication")
    print("\n---Step 2---When---Pass---")


@then('Redirect to Loginpage')
def check_redirect_to_page(browser):
    webdriver.Wait(browser, 5).until(ec.url_changes(LoginpageLocators.URL))
    assert browser.current_url == LoginpageLocators.URL, "Main page URL is not ok."
