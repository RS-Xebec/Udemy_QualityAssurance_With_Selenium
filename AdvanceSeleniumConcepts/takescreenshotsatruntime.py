#While doing automation testing, it is very useful to take screenshots at runtime to debug issues.
 
from selenium.webdriver import Chrome
import takescreenshot
driver = Chrome()
driver.get("https://uatdemo.enlightbook.com/")

driver.maximize_window()
# driver.get_screenshot_as_file("D:\\UDEMY\\AdvanceSeleniumConcepts\\screenshot_runtime.png")



#Another way is we can create a function to take screenshots at runtime and do import takescreenhot.py
takescreenshot.take_page_screenshot(driver,"screenshot_runtime2")




