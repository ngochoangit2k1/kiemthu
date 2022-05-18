from selenium import webdriver
from  webdriver_manager.chrome import  ChromeDriverManager

class HomePape:
    link_login_xpath="//a[@href='/signin']"
    link_register_xpath="//a[@href='/signup']"

    def __init__(self,driver):
        self.driver = driver

    def clickOnLogin(self):
        self.driver.find_element_by_xpath(self.link_login_xpath).click()


    def clickOnRegister(self):
        self.driver.find_element_by_xpath(self.link_register_xpath).click()