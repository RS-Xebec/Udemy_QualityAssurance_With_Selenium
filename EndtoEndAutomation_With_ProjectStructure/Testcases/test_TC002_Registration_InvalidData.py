from selenium.webdriver import Chrome
from Base import InitiateDriver
from Library import ConfigReader
from selenium.webdriver.common.by import By 



def test_InvalidRegistration():
    driver = InitiateDriver.startbrowser() 
    driver.find_element(By.XPATH,ConfigReader.fetchElementLocators("Registration","username")).send_keys("InvalidData")
    driver.find_element(By.XPATH,ConfigReader.fetchElementLocators("Registration","password")).send_keys("Testing")
    