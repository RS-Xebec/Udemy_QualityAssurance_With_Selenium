from selenium.webdriver import Chrome

def test_registration_valid_data():
    driver = Chrome()     #Object Created driver is object name and Chrome() is class
    driver.get("https://www.facebook.com/r.php?entry_point=login")

