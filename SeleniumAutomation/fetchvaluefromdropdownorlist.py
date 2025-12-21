from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By 



driver = Chrome()     #Object Created driver is object name and Chrome() is class
driver.get("https://www.facebook.com/r.php?entry_point=login")

#Maximize Browser
driver.maximize_window()

#Working with dropdown or listbox
obj = Select(driver.find_element(By.XPATH,"//select[@aria-label='Month']"))
obj.select_by_visible_text("May")  #select by visible text

#Fetch only the selected option from the dropdown
print("Selected option is:", obj.first_selected_option.text)

#Fetch all the options from the dropdown
print("All options from the dropdown are:")
for option in obj.options:
    print(option.text)

input("Press Enter to close the browser...")