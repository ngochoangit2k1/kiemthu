import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePape
from Utilitis.customLogger import LogGen
from Utilitis.readproperty import ReadConfig
import time

baseURl = ReadConfig.getURL()
mylogger = LogGen.loggen()

print(baseURl)


@given(u'Launch the browser')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    mylogger.info("****Driver Initilized ****")
    context.driver.get(baseURl)
    mylogger.info("****Broser ****")


@then(u'verify the page title')
def step_impl(context):
    actual_title = context.driver.title
    expcted_title = "Change 2 Automation – Change 2 Automation"
    if actual_title == expcted_title:
        assert True
        mylogger.info("****Title matched ****")
    else:
        mylogger.info("****Title not matched ****")
        assert False
        time.sleep(5)


@then(u'close the browser')
def step_impl(context):
    context.driver.close()
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
