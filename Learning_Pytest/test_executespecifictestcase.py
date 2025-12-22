from selenium.webdriver import Chrome
import pytest


def test_registration_valid_data():
    driver = Chrome()     #Object Created driver is object name and Chrome() is class
    driver.get("https://www.facebook.com/r.php?entry_point=login")
    driver.maximize_window()


def test_registration_invalid_data():
    driver = Chrome()     #Object Created driver is object name and Chrome() is class
    driver.get("https://www.facebook.com/r.php?entry_point=login")
    driver.maximize_window()

#Suppose i only want to execute the 2nd test case which is test_registration_invalid_data
#Then we can use -k option in pytest command
#pytest -v -k test_registration_invalid_data Learning_Pytest/test_executespecifictestcase.py

def test_invalid_data():
    driver = Chrome()     #Object Created driver is object name and Chrome() is class
    driver.get("https://www.facebook.com/r.php?entry_point=login")
    driver.maximize_window()

#suppose i want to execute test case having registration in the name
#pytest -v -k registration Learning_Pytest/test_executespecifictestcase.py


