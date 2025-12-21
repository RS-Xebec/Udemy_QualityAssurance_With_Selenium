from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By 

driver = Chrome()     #Object Created driver is object name and Chrome() is class
driver.get("https://www.facebook.com/")
driver.maximize_window()

#fetching innerText of an element
print("Inner text of the element is" + driver.find_element(By.XPATH,"//button[@name='login']").text)  #.text is used to fetch inner text of an element


#fetching attribute value of an element
print("Attribute which is id value of the element is:", driver.find_element(By.XPATH,"//input[@type='text']").get_attribute("id"))