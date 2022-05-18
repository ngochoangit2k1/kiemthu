# -*- coding: utf-8 -*-

import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages.RegisterPage import RegisterPage
from Pages.HomePage import HomePape
from TestData import DataExcel
from Utilitis.customLogger import LogGen
from Utilitis.readproperty import ReadConfig
import time

baseURl = ReadConfig.getURL()
mylogger = LogGen.register()
pathExcel = ReadConfig.getUrlExcelFile()
sheetRe = ReadConfig.getUrlSheetRegister()



rows = DataExcel.getRowCount(pathExcel, sheetRe)

@given(u'Launch the App111')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    mylogger.info("****Driver Initilized ****")
    context.driver.get(baseURl)
    mylogger.info("****Broser ****")


@when(u'enter registration credentials111')
def step_impl(context):

    mylogger.info("****Passing Credentsials ****")
    global hpage
    global lpage
    hpage = HomePape(context.driver)
    lpage = RegisterPage(context.driver)
    hpage.clickOnRegister()
    rows = DataExcel.getRowCount(pathExcel, sheetRe)
    for r in range(16, rows + 1):
        name = DataExcel.readData(pathExcel, sheetRe, r, 1)
        emaill = DataExcel.readData(pathExcel, sheetRe, r, 2)
        passwordd = DataExcel.readData(pathExcel, sheetRe, r, 3)
        lpage.setname(name)
        lpage.setemail(emaill)
        lpage.setpassword(passwordd)
        lpage.clickcheckbox()
        lpage.clickonregister()
        txt1 = "****Entered Credentials {} passed *****"
        txt2 = "****Entered Credentials {} failed *****"
        time.sleep(2)
        if context.driver.current_url == "https://letcode.in/":
            mylogger.info(txt1.format(r - 1))
            DataExcel.writeData(pathExcel, sheetRe, r, 4, "test passed")

        else:
            mylogger.info(txt2.format(r - 1))
            DataExcel.writeData(pathExcel, sheetRe, r, 4, "test failed")
            context.driver.save_screenshot(
                 "F:\\baitap\\kiemthu\\ScreenShots\\Registest\\"  + f"RegesFalse{r}Page.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="letcode Login test",
                          attachment_type=AttachmentType.PNG)
        context.driver.refresh()
    mylogger.info("****Passing Credentsials ****")


@then(u'verify the page title and screenshot111')
def step_impl(context):
    actual_title = context.driver.title
    expected_title = r"LetCode with Koushik"
    actual_title == expected_title

    context.driver.save_screenshot(
            "F:\\baitap\\kiemthu\\ScreenShots\\Registest\\" + "RegisTruePage.png")
    allure.attach(context.driver.get_screenshot_as_png(), name="c2ta Login test",
                      attachment_type=AttachmentType.PNG)
    mylogger.info("****Title matched****")



@then(u'close the App111')
def step_impl(context):
    context.driver.close()
    mylogger.info("****Close****")


