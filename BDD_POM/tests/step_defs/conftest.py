import pytest
from selenium import webdriver


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')


@pytest.fixture
def browser():
    # initializam un browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    # return driver
    yield driver
    # after tests
    driver.quit()
