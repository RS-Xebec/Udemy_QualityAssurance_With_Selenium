# Forced wait
# for using forced wait, we import time module
# and by using time.sleep method we can force a wait. For example: time.sleep(5). It forces 5 second wait before executing the remaining script.


# Page load timeout

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By 
 #for using By we need to import this
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = Chrome()     #Object Created driver is object name and Chrome() is class
driver.set_page_load_timeout(4)  #it will wait for maximum 4 seconds for page to load, if it is not loaded in 4 seconds it will throw timeout exception
driver.get("https://uatdemo.enlightbook.com/")

#Maximize Browser
driver.maximize_window()

input("Press Enter to close the browser...")
driver.close()