from selenium.webdriver.common.by import By 
 #for using By we need to import this
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = Chrome()     #Object Created driver is object name and Chrome() is class
driver.set_page_load_timeout(4)  #it will wait for maximum 4 seconds for page to load, if it is not loaded in 4 seconds it will throw timeout exception
driver.get("https://uatdemo.enlightbook.com/")

driver.implicitly_wait(7)  #It will wait for maximum 7 seconds for searching of an element before throwing NoSuchElementException

#Maximize Browser
driver.maximize_window()

#working on radio button
driver.find_element(By.XPATH, "//input[@type='radio' and @value='office']").click()

input("Press Enter to close the browser...")
driver.close()