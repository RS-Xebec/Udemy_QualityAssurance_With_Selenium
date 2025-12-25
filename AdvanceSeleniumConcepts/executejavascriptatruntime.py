from selenium.webdriver import Chrome

driver = Chrome()
driver.get("https://uatdemo.enlightbook.com/")
driver.maximize_window()

driver.execute_script("window.scrollTo(0,400);")  #Scroll down by 400 pixels
