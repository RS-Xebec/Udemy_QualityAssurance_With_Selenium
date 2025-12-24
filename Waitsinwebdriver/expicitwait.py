from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By 
 #for using By we need to import this
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = Chrome()
driver.get("https://uatdemo.enlightbook.com/")
driver.maximize_window()

 
wait = WebDriverWait(driver, 7)  #It waits until the elements are visible for maximum 15 seconds
wait.until(EC.text_to_be_present_in_element((By.ID,"countryid"),"Nepal")) #Wait until the text "Nepal" is present in the element with ID "element_id"  
obj = Select(driver.find_element(By.ID,"countryid"))
obj.select_by_visible_text("Nepal")

#This i just an example of text to be present in element, similar way we can use other expected conditions as per our requirement
#For example, in the dropdown options we may need to wait until certain option is present before selecting it so we can use this expected condition