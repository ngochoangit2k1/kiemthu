import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


from Pages.RegisterPage import RegisterPage
from Pages.HomePage import HomePape
from Utilitis.customLogger import LogGen
from Utilitis.readproperty import ReadConfig
import time

baseURl = ReadConfig.getURL()
mylogger = LogGen.register()


@given(u'Launch the App1')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    mylogger.info("****Driver Initilized ****")
    context.driver.get(baseURl)
    mylogger.info("****Broser ****")


@when(u'enter registration credentials1')
def step_impl(context):
    mylogger.info("****Passing Credentsials ****")
    global hpage
    global lpage
    hpage = HomePape(context.driver)
    hpage.clickOnLogin()

    hpage.clickOnRegister()
    lpage = RegisterPage(context.driver)
    nam = ReadConfig.getName()
    eml = ReadConfig.getEmail()
    urs = ReadConfig.getnewUserName()
    pwd = ReadConfig.getPassword()
    rpwd = ReadConfig.getRePassword()
    lpage.setname(nam)
    lpage.setemail(eml)
    lpage.setusername(urs)
    lpage.setpassword(pwd)
    lpage.setrepeatpassword(rpwd)
    lpage.clickcheckbox()
    mylogger.info("****Passing Credentsials ****")


@then(u'click register')
def step_impl(context):
    lpage.clickonregister()
    mylogger.info("****Click register Button ****")


@then(u'verify the page title and screenshot1')
def step_impl(context):
    actual_title = context.driver.title
    expected_title = ""
    if actual_title == expected_title:
        assert True
        context.driver.save_screenshot(
            "F:\\baitap\\kiemthu\\ScreenShots\\" + "RegisterPage.png")
        allure.attach(context.driver.get_screenshot_as_png(), name="c2ta Register test",
                      attachment_type=AttachmentType.PNG)
        mylogger.info("****Title matched****")
    else:
        mylogger.info("****Title not matched****")
        context.driver.save_screenshot(
            "F:\\baitap\\kiemthu\\ScreenShots\\" + "RegisterPage.png")
        allure.attach(context.driver.get_screenshot_as_png(), name="c2ta Login test",
                      attachment_type=AttachmentType.PNG)
        assert False


@then(u'close the App1')
def step_impl(context):
    context.driver.close()
    mylogger.info("****End ****")
