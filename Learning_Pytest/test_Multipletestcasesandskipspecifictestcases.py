from selenium.webdriver import Chrome
import pytest


def test_registration_valid_data():
    driver = Chrome()     #Object Created driver is object name and Chrome() is class
    driver.get("https://www.facebook.com/r.php?entry_point=login")
    driver.maximize_window()

#lets skip this test case
@pytest.mark.skip("Don't want to execute on current build")
def test_registration_invalid_data1():
    driver = Chrome()     #Object Created driver is object name and Chrome() is class
    driver.get("https://www.facebook.com/r.php?entry_point=login")
    driver.maximize_window()

def test_registration_invalid_data2():
    driver = Chrome()     #Object Created driver is object name and Chrome() is class
    driver.get("https://www.facebook.com/r.php?entry_point=login")
    driver.maximize_window()


