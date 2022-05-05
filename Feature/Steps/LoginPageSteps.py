# -*- coding: utf-8 -*-
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


@given(u'Launch the App')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    mylogger.info("****Driver Initilized ****")
    context.driver.get(baseURl)
    mylogger.info("****Broser ****")


@when(u'enter login credentials')
def step_impl(context):
    mylogger.info("****Passing Credentsials ****")
    global hpage
    global lpage
    hpage = HomePape(context.driver)
    hpage.clickOnLogin()
    lpage = LoginPage(context.driver)
    urs = ReadConfig.getUserName()
    pwd = ReadConfig.getPassword()
    lpage.setusername(urs)
    lpage.setpassword(pwd)
    mylogger.info("****Passing Credentsials ****")


@then(u'click login')
def step_impl(context):
    lpage.clickonlogin()
    mylogger.info("****Click Login Button ****")


@then(u'verify the page title and screenshot')
def step_impl(context):
    actual_title = context.driver.title
    expected_title = r"Viblo - Login"
    if actual_title == expected_title:
        assert True
        context.driver.save_screenshot(
            "F:\\baitap\\kiemthu\\ScreenShots\\" + "LoginTruePage.png")
        allure.attach(context.driver.get_screenshot_as_png(), name="c2ta Login test",
                      attachment_type=AttachmentType.PNG)
        mylogger.info("****Title matched****")
    else:
        mylogger.info("****Title not matched****")
        context.driver.save_screenshot(
            "F:\\baitap\\kiemthu\\ScreenShots\\" + "LoginFalsePage.png")
        allure.attach(context.driver.get_screenshot_as_png(), name="Viblo Login test",
                      attachment_type=AttachmentType.PNG)
        assert False


@then(u'close the App')
def step_impl(context):
    context.driver.close()
    mylogger.info("****Close****")
