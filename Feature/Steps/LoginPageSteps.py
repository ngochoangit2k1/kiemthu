# -*- coding: utf-8 -*-
import re, sys, unicodedata

import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePape
from TestData import DataExcel
from Utilitis.customLogger import LogGen
from Utilitis.readproperty import ReadConfig
import time

baseURl = ReadConfig.getURL()
mylogger = LogGen.loggen()
pathExcel = ReadConfig.getUrlExcelFile()
sheetLogin = ReadConfig.getUrlSheetLogin()



rows = DataExcel.getRowCount(pathExcel, sheetLogin)

@given(u'Launch the App')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    mylogger.info("****Driver Initilized ****")
    context.driver.get(baseURl)
    mylogger.info("****Broser ****")


@when(u'enter key to input login credentials and click button')
def step_impl(context):
    mylogger.info("****Passing Credentsials ****")
    global hpage
    global lpage
    hpage = HomePape(context.driver)
    lpage = LoginPage(context.driver)
    hpage.clickOnLogin()
    rows = DataExcel.getRowCount(pathExcel, sheetLogin)
    for r in range(16, rows + 1):
        email = DataExcel.readData(pathExcel, sheetLogin, r, 1)
        password = DataExcel.readData(pathExcel, sheetLogin, r, 2)
        lpage.setusername(email)
        time.sleep(2)
        lpage.setpassword(password)
        time.sleep(2)
        lpage.clickonlogin()
        txt1 = "****Entered Credentials {} passed *****"
        txt2 = "****Entered Credentials {} failed *****"
        time.sleep(3)
        if context.driver.current_url == "https://letcode.in/":
            mylogger.info(txt1.format(r - 1))
            DataExcel.writeData(pathExcel, sheetLogin, r, 3, "test passed")
        else:
            mylogger.info(txt2.format(r - 1))
            DataExcel.writeData(pathExcel, sheetLogin, r, 3, "test failed")
            context.driver.save_screenshot(
                "F:\\baitap\\kiemthu\\ScreenShots\\Login\\" + f"LoginFalse{r}.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="letcode Login test",
                          attachment_type=AttachmentType.PNG)

        context.driver.refresh()
    mylogger.info("****Passing Credentsials ****")


@then(u'verify the page title and screenshot')
def step_impl(context):
    actual_title = context.driver.title
    expected_title = r"LetCode with Koushik"
    actual_title == expected_title

    context.driver.save_screenshot(
            "F:\\baitap\\kiemthu\\ScreenShots\\Login\\" + "LoginTruePage.png")
    allure.attach(context.driver.get_screenshot_as_png(), name="c2ta Login test",
                      attachment_type=AttachmentType.PNG)
    mylogger.info("****Title matched****")



@then(u'close the App')
def step_impl(context):
    context.driver.close()
    mylogger.info("****Close****")

# @given(u'Launch the App')
# def step_impl(context):
#     context.driver = webdriver.Chrome(ChromeDriverManager().install())
#     mylogger.info("****Driver Initilized ****")
#     context.driver.get(baseURl)
#     mylogger.info("****Broser ****")
#
#
# @when(u'enter login credentials')
# def step_impl(context):
#     mylogger.info("****Passing Credentsials ****")
#     global hpage
#     global lpage
#     hpage = HomePape(context.driver)
#     hpage.clickOnLogin()
#     lpage = LoginPage(context.driver)
#     urs = ReadConfig.getUserName()
#     pwd = ReadConfig.getPassword()
#     lpage.setusername(urs)
#     lpage.setpassword(pwd)
#     mylogger.info("****Passing Credentsials ****")
#
#
# @then(u'click login')
# def step_impl(context):
#     lpage.clickonlogin()
#     mylogger.info("****Click Login Button ****")
#
#
# @then(u'verify the page title and screenshot')
# def step_impl(context):
#     p.actual_title = context.driver.title
#     p.expected_title = r"Bài viết mới nhất - Viblo"
#     if p.actual_title == p.expected_title:
#         assert True
#         context.driver.save_screenshot(
#             "F:\\baitap\\kiemthu\\ScreenShots\\" + "LoginTruePage.png")
#         allure.attach(context.driver.get_screenshot_as_png(), name="c2ta Login test",
#                       attachment_type=AttachmentType.PNG)
#         mylogger.info("****Title matched****")
#     else:
#         mylogger.info("****Title not matched****")
#         context.driver.save_screenshot(
#             "F:\\baitap\\kiemthu\\ScreenShots\\" + "LoginFalsePage.png")
#         allure.attach(context.driver.get_screenshot_as_png(), name="Viblo Login test",
#                       attachment_type=AttachmentType.PNG)
#         assert False
#
#
# @then(u'close the App')
# def step_impl(context):
#     context.driver.close()
#     mylogger.info("****Close****")