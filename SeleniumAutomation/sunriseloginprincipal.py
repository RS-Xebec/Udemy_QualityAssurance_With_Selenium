from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By 
 #for using By we need to import this
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = Chrome()     #Object Created
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

login_button = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//span[text()='Log In']"))
)
login_button.click()



Discussion_forum = WebDriverWait(driver, 8).until(
    EC.presence_of_element_located((By.XPATH, "//span[text()='Discussion Forum']"))
)
Discussion_forum.click()

input("Press Enter to close the browser...")



driver.close()