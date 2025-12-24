#Description of Assertion In Pytest
#Assertions are used to verify that a certain condition is true. If the condition is false, the test case will fail.
#In pytest, we can use the assert statement to perform assertions.

#The following code wont run because the file title is not starting with test_ . I have written this so i can look at the syntax later

import pytest
from selenium.webdriver import Chrome

# For example
def test_registration_invalid_data2():
    driver = Chrome()     #Object Created driver is object name and Chrome() is class
    driver.get("https://www.facebook.com/r.php?entry_point=login")
    driver.maximize_window()
    assert driver.title == "Sign up for Facebook"  # This assertion will pass if the title is correct


# Or watch video 267

