from selenium.webdriver import Chrome
import pytest

@pytest.mark.Smoke
def test_registration_valid_data():
    driver = Chrome()     #Object Created driver is object name and Chrome() is class
    driver.get("https://www.facebook.com/r.php?entry_point=login")
    driver.maximize_window()


@pytest.mark.Sanity
def test_registration_invalid_data1():
    driver = Chrome()     #Object Created driver is object name and Chrome() is class
    driver.get("https://www.facebook.com/r.php?entry_point=login")
    driver.maximize_window()

@pytest.mark.Smoke
def test_registration_invalid_data2():
    driver = Chrome()     #Object Created driver is object name and Chrome() is class
    driver.get("https://www.facebook.com/r.php?entry_point=login")
    driver.maximize_window()

#Here i have created 3 test cases and assigned them to different groups like Smoke and Sanity
#Now suppose i want to execute only Smoke test cases
#Then we can use -m option in pytest command
#pytest -v  Smoke -m Learning_Pytest/test_grouptestcases_and_executeanyspecificgroup.py

#suppose i want to execute cases other than smoke group then we can use "not" keyword with -m option
#pytest -v  "not Smoke" -m Learning_Pytest/test_grouptestcases_and_executeanyspecificgroup.py


