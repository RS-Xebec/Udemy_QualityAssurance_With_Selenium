from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By 
 #for using By we need to import this
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = Chrome()     #Object Created driver is object name and Chrome() is class
driver.get("https://www.facebook.com/")

#Maximize Browser
driver.maximize_window()

#Fetching title
print("Page Title is:", driver.title) 

#Fetching Page URL
print("Page URL is:", driver.current_url)

#Fetching Page HTML Source Code
print("---------------------------------------------------")
print("Page HTML Source Code is:", driver.page_source)



