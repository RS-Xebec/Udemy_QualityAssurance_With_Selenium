from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from Library import ConfigReader

def startbrowser():
    global driver

    if(ConfigReader.readConfigData('Details','Browser')=="Chrome"):
        driver = Chrome()
    
    elif(ConfigReader.readConfigData('Details','Browser')=="Firefox"):
        driver = Firefox()
    
    else:
        driver = Chrome()

    driver.get(ConfigReader.readConfigData('Details','Application_Url'))
    driver.maximize_window()
    return driver

def closebrowser():
    driver.close()


    
