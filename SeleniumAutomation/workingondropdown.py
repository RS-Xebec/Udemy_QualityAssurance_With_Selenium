from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.select import Select

driver = Chrome()     #Object Created
driver.get("https://uatdemo.enlightbook.com/")

#Maximize Browser
driver.maximize_window()

obj = Select(driver.find_element(By.NAME, "sex"))
obj.select_by_index(1)   #select by index
obj.select_by_value("2")  #select by value #The alue is inside the tag as value="2"
obj.select_by_visible_text("Female")  #select by visible text       