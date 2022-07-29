from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Base import InitiateDriver

def test_firstcase():
    driver = InitiateDriver.startBrowser()
    #  Enter Data to the textbox
    driver.find_element(By.NAME,"fld_username").send_keys("helloworld")
    driver.find_element(By.XPATH,"//input[@name='fld_email']").send_keys("testingworldindia@gmail.com")
    driver.find_element(By.NAME,"fld_password").send_keys("abcd123")
    driver.find_element(By.NAME,"fld_cpassword").send_keys("abcd123")
    driver.find_element(By.NAME,"fld_username").clear()
    driver.find_element(By.NAME,"fld_username").send_keys("abcd123")
    
    driver = InitiateDriver.closeBrowser()