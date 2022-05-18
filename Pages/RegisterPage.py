from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class RegisterPage:
    txt_name_xpath = "//input[@placeholder='Enter your name']"
    txt_email_xpath = "//input[@placeholder='Enter valid email address']"
    txt_username_xpath = '(//input[@type="text"])[3]'
    txt_password_xpath = '(//input[@type="password"])[1]'
    btn_register_xpath = "//button[text()='SIGN UP']"
    btn_checkbox_xpath = "//input[@type='checkbox']"

    def __init__(self, driver):
        self.driver = driver

    def setusername(self, username):
        self.driver.find_element_by_xpath(self.txt_username_xpath).send_keys(username)

    def setname(self, name):
        self.driver.find_element_by_xpath(self.txt_name_xpath).send_keys(name)

    def setemail(self, mail):
        self.driver.find_element_by_xpath(self.txt_email_xpath).send_keys(mail)

    def setpassword(self, password):
        self.driver.find_element_by_xpath(self.txt_password_xpath).send_keys(password)

    def clickcheckbox(self):
        self.driver.find_element_by_xpath(self.btn_checkbox_xpath).click()

    def clickonregister(self):
        self.driver.find_element_by_xpath(self.btn_register_xpath).click()
