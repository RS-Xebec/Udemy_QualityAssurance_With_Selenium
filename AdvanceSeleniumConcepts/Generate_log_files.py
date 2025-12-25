# #Logging functions
# 1.Logging.debug
# 2.Logging.warning
# 3.logging.error
# 4.logging.info
# 5.logging.critical


# Logging Levels
# 1.Debug
# 2.Info
# 3.Warning
# 4.KeyError
# 5.Critical

#Step 1: Import logging 
import logging
import logging as log

#Step 2: 
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)    #logger tells us what are all the logs you want to generate

#Step 3 : File Handler : here we have handler which is handling files where you want to generate and store logs
warn = logging.FileHandler('Warning_Logs.txt')
warn.setLevel(logging.WARNING)

info = logging.FileHandler('Info_Logs.txt')
info.setLevel(logging.INFO)

#Step 4: Next we nee to define formatting of logs
#Create a logging format
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')

# Step 5:
warn.setFormatter(formatter)
info.setFormatter(formatter)



from selenium.webdriver import Chrome
driver = Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")

log.info("[My url is opened successfully]")
log.warn("[There is delay in opening of browser]")
