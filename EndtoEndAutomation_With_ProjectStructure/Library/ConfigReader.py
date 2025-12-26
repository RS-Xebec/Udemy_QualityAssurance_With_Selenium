import configparser
# import os

def readConfigData(section,key):
    config=configparser.ConfigParser()
    config.read("./ConfigurationFiles/config.cfg")
    #use ./ not ../
    # or
    # config.read("D:\UDEMY\EndtoEndAutomation_With_ProjectStructure\ConfigurationFiles\config.cfg")

    return config.get(section,key)


# BEST PRACTICE (what professionals use)

# Never hardcode absolute paths ❌
# Never trust plain relative paths ❌

# ✔ Use path relative to the file itself
#Below is what professional use
# def readConfigData(section, key):
#     config = configparser.ConfigParser()

#     base_dir = os.path.dirname(__file__)
#     config_path = os.path.join(base_dir, "..", "ConfigurationFiles", "config.cfg")

#     config.read(config_path)
#     return config.get(section, key)

# print(readConfigData('Details','Application_Url'))

def fetchElementLocators(section,key):
    config=configparser.ConfigParser()
    config.read("./ConfigurationFiles/elements.cfg")
    return config.get(section,key)