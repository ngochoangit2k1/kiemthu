from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class LoginPage:
    txt_username_type = "//input[@name='email']"
    txt_password_type = "//input[@name='password']"
    btn_login_xpath = "//button[text()='LOGIN']"

    btn_logout_xpath = "//a[text()='Sign out']"

    def __init__(self, driver):
        self.driver = driver

    def setusername(self, username):
        self.driver.find_element_by_xpath(self.txt_username_type).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element_by_xpath(self.txt_password_type).send_keys(password)


    def clickonlogin(self):
        self.driver.find_element_by_xpath(self.btn_login_xpath).click()

    def clickontotlogout(self):
        self.driver.find_element_by_xpath(self.btn_totliplogout_xpath).click()

    def clickonlogout(self):
        self.driver.find_element_by_xpath(self.btn_logout_xpath).click()
