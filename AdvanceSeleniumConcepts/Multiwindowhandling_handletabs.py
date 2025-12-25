from selenium.webdriver import Chrome

driver=Chrome()
driver.maximize_window()

driver.get("https://thetestingworld.com/testings/")
driver.find_element("xpath","//a[text()='Login']").click()
driver.find_element("NAME","_txtUserName").send_keys("admin")
driver.find_element("NAME","_txtPassword").send_keys("admin")
driver.find_element("XPATH","//input[@type='submit' and @value='Login']").click()
driver.find_element("XPATH","//a[contains(text(),'My Account')]").click()
driver.find_element("XPATH","//a[contains(text(),'Delete')]").click()

allTabs = driver.window_handles
print(allTabs)

for tab in allTabs: 
    driver.switch_to.window(tab)
    if(driver.current_url=="https://thetestingworld.com/testings/manage_customer.php"):
        driver.find_element("XPATH","//button[text()='Start Download']").click()
        