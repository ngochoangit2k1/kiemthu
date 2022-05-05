from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class RegisterPage:
    txt_name_xpath = '(//input[@type="text"])[1]'
    txt_email_xpath = '(//input[@type="text"])[2]'
    txt_username_xpath = '(//input[@type="text"])[3]'
    txt_password_xpath = '(//input[@type="password"])[1]'
    txt_repeatpassword_xpath = '(//input[@type="password"])[2]'
    btn_register_xpath = "(//button[@type='button'])[1]"
    btn_checkbox_xpath = "//span[@class='el-checkbox__inner']"

    def __init__(self, driver):
        self.driver = driver

    def setusername(self, username):
        self.driver.find_element_by_xpath(self.txt_username_xpath).send_keys(username)

    def setname(self, name):
        self.driver.find_element_by_xpath(self.txt_name_xpath).send_keys(name)

    def setemail(self, mail):
        self.driver.find_element_by_xpath(self. txt_email_xpath ).send_keys(mail)

    def setpassword(self, password):
        self.driver.find_element_by_xpath(self.txt_password_xpath).send_keys(password)

    def setrepeatpassword(self, repassword):
        self.driver.find_element_by_xpath(self.txt_repeatpassword_xpath).send_keys(repassword)

    def clickcheckbox(self):
        self.driver.find_element_by_xpath(self.btn_checkbox_xpath).click()

    def clickonregister(self):
        self.driver.find_element_by_xpath(self.btn_register_xpath).click()
