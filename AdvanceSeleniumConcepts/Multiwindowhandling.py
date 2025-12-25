from selenium.webdriver import Chrome

driver=Chrome()
driver.maximize_window()
mainWin=""
driver.get("https://www.naukri.com/")
Allwindow = driver.window_handles

for win in Allwindow:
    driver.switch_to.window(win)
    if(driver.current_url=="https://www.naukri.com/"):
        mainWin=win
    else:
        driver.close()

driver.switch_to.window(mainWin)
print(driver.current_url)