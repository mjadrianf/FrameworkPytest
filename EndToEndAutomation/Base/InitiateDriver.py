from lib2to3.pgen2 import driver
from selenium import webdriver
from Library import ConfigReader

def startBrowser():
    global driver
    driver=webdriver.Chrome()
    driver.get(ConfigReader.readConfigData('Details', 'Application_URL'))
    # Maximize browser
    driver.maximize_window()
    return driver

def closeBrowser():
    driver.quit()