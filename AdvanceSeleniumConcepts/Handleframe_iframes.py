from selenium.webdriver import Chrome

driver = Chrome()
driver.maximize_window()
driver.get("https://toolsqa.com/iframe-practice-page/")
driver.switch_to.frame(driver.find_element("XPATH","//iframe[@name='iframe2']"))       #Switching to iframe using name attribute
driver.find_element("XPATH","//a[contains(text(),'Read More')]").click()
driver.switch_to.default_content()                    #Switching back to main page from iframe
driver.find_element("XPATH","//span[text()='Videos']").click()