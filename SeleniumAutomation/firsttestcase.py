from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By 
 #for using By we need to import this
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = Chrome()     #Object Created driver is object name and Chrome() is class
driver.get("https://uatdemo.enlightbook.com/")

#Maximize Browser
driver.maximize_window()

#Enter data into textbox
# driver.find_element(By.XPATH,"//input[@name='username']").send_keys("principal1")  #For entering data into textboxes
#we can also find element by x path
# driver.find_element(By.XPATH,"")

wait = WebDriverWait(driver, 7)  #It waits until the elements are visible for maximum 15 seconds

username = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@name='username']"))
)   #Wait until the username input box becomes visible on the page, then store it in the variable
username.send_keys("principal1")

password = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@name='password']"))
)
password.send_keys("principal1")

#Here is an example of working with radio button
# Wait until the radio button with value='office' is clickable
radio_office = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@type='radio' and @value='office']"))
)
# Click the radio button
radio_office.click()


#Here is an example of working on checkbox
checkbox = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox' and @value='newsletter']"))
)
checkbox.click()


#For clicking events like these the steps are same, there maybe slight changes but it is done in the same way


#for closing browser
driver.close()
