from selenium.webdriver import Chrome   
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 

driver = Chrome()     #Object Created
driver.get("https://www.facebook.com")
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("test@example.com")

act = ActionChains(driver)  #Create ActionChains object to perform keyboard actions in the same browser session
# act.send_keys(Keys.TAB).perform()  -- Moves to the next field (password field)

#TO do CTRL + A (Select All) in the same textbox of username
act.key_down(Keys.CONTROL).send_keys('a').perform()
#In these ways we can perform multiple keyboard operations or watch video no 257 on udemy of the course



input("Press Enter to close the browser...")