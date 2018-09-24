# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'i.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random



class Ui_Form(object):



    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.top1 = QtWidgets.QLineEdit(Form)
        self.top1.setGeometry(QtCore.QRect(30, 30, 113, 20))
        self.top1.setObjectName("top1")
        self.top2 = QtWidgets.QLineEdit(Form)
        self.top2.setGeometry(QtCore.QRect(30, 60, 113, 20))
        self.top2.setObjectName("top2")
        self.topla = QtWidgets.QPushButton(Form)
        self.topla.setGeometry(QtCore.QRect(50, 90, 75, 23))
        self.topla.setObjectName("topla")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 122, 47, 31))
        self.label.setText("0")
        self.label.setObjectName("label")
        self.topla.clicked.connect(self.click)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)




    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.topla.setText(_translate("Form", "PushButton"))

    def click(self):
        #self.label.setText(str(int(self.top1.text()) + int(self.top2.text())))
        driver = webdriver.Firefox()
        driver.maximize_window()
        time.sleep(1)

        driver.get("https://lp.darkorbit.com/")
        driver.minimize_window()
        time.sleep(3)

        bbb = driver.find_element_by_id("bgcdw_login_form_username")

        bbb.send_keys(self.top1.text())

        time.sleep(1)
        aaa = driver.find_element_by_id("bgcdw_login_form_password")

        aaa.send_keys(self.top2.text())
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='login']/div[1]/div/form/fieldset[2]/button[1]").click()
        time.sleep(2)

        # hasar

        driver.get("https://tr2.darkorbit.com/indexInternal.es?action=internalAuction")
        a = random.randint(3, 7)
        time.sleep(a)

        driver.find_element_by_xpath(
            "/html/body/div[12]/div/div/div[2]/div[4]/div/div[2]/div/div[5]/div[2]/div[1]/table/tbody[2]/div/div[1]/tr[40]/td[3]").click()
        driver.find_element_by_name("credits").clear()
        time.sleep(1)
        driver.find_element_by_name("credits").send_keys("20000000")
        time.sleep(1)
        driver.find_element_by_name("auction_buy_button").send_keys(Keys.ENTER)
        time.sleep(1)

        driver.get("https://tr2.darkorbit.com/indexInternal.es?action=internalAuction")

        # tp
        a = random.randint(3, 7)
        time.sleep(a)

        driver.find_element_by_xpath(
            "/html/body/div[12]/div/div/div[2]/div[4]/div/div[2]/div/div[5]/div[2]/div[1]/table/tbody[2]/div/div[1]/tr[38]/td[3]").click()
        driver.find_element_by_name("credits").clear()
        time.sleep(1)
        driver.find_element_by_name("credits").send_keys("5000000")
        time.sleep(1)
        driver.find_element_by_name("auction_buy_button").send_keys(Keys.ENTER)
        time.sleep(1)

        # şeref
        driver.get("https://tr2.darkorbit.com/indexInternal.es?action=internalAuction")

        a = random.randint(3, 7)
        time.sleep(a)

        driver.find_element_by_xpath(
            "/html/body/div[12]/div/div/div[2]/div[4]/div/div[2]/div/div[5]/div[2]/div[1]/table/tbody[2]/div/div[1]/tr[42]/td[3]").click()
        driver.find_element_by_name("credits").clear()
        time.sleep(1)
        driver.find_element_by_name("credits").send_keys("10000000")
        time.sleep(1)
        driver.find_element_by_name("auction_buy_button").send_keys(Keys.ENTER)
        time.sleep(1)

        # dp #/html/body/div[12]/div/div/div[2]/div[4]/div/div[2]/div/div[5]/div[2]/div[1]/table/tbody[2]/div/div[1]/tr[45]/td[3]
        driver.get("https://tr2.darkorbit.com/indexInternal.es?action=internalAuction")

        a = random.randint(3, 7)
        time.sleep(a)

        driver.find_element_by_xpath(
            "/html/body/div[12]/div/div/div[2]/div[4]/div/div[2]/div/div[5]/div[2]/div[1]/table/tbody[2]/div/div[1]/tr[45]/td[3]").click()
        driver.find_element_by_name("credits").clear()
        time.sleep(1)
        driver.find_element_by_name("credits").send_keys("1000000")
        time.sleep(1)
        driver.find_element_by_name("auction_buy_button").send_keys(Keys.ENTER)
        time.sleep(1)

        # kalkan(/html/body/div[12]/div/div/div[2]/div[4]/div/div[2]/div/div[5]/div[2]/div[1]/table/tbody[2]/div/div[1]/tr[39]/td[3])
        driver.get("https://tr2.darkorbit.com/indexInternal.es?action=internalAuction")

        a = random.randint(3, 7)
        time.sleep(a)

        driver.find_element_by_xpath(
            "/html/body/div[12]/div/div/div[2]/div[4]/div/div[2]/div/div[5]/div[2]/div[1]/table/tbody[2]/div/div[1]/tr[39]/td[3]").click()
        driver.find_element_by_name("credits").clear()
        time.sleep(1)
        driver.find_element_by_name("credits").send_keys("5000000")
        time.sleep(1)
        driver.find_element_by_name("auction_buy_button").send_keys(Keys.ENTER)
        time.sleep(1)

        # x3 #/html/body/div[12]/div/div/div[2]/div[4]/div/div[2]/div/div[5]/div[2]/div[1]/table/tbody[2]/div/div[1]/tr[2]/td[3]

        driver.get("https://tr2.darkorbit.com/indexInternal.es?action=internalAuction")

        a = random.randint(3, 7)
        time.sleep(a)

        driver.find_element_by_xpath(
            "/html/body/div[12]/div/div/div[2]/div[4]/div/div[2]/div/div[5]/div[2]/div[1]/table/tbody[2]/div/div[1]/tr[2]/td[3]").click()
        driver.find_element_by_name("credits").clear()
        time.sleep(1)
        driver.find_element_by_name("credits").send_keys("450000")
        time.sleep(1)
        driver.find_element_by_name("auction_buy_button").send_keys(Keys.ENTER)
        time.sleep(1)

        # kamufle
        driver.get("https://tr2.darkorbit.com/indexInternal.es?action=internalAuction")
        a = random.randint(3, 7)
        time.sleep(a)

        driver.find_element_by_xpath(
            "/html/body/div[12]/div/div/div[2]/div[4]/div/div[2]/div/div[5]/div[2]/div[1]/table/tbody[2]/div/div[1]/tr[11]/td[2]").click()
        driver.find_element_by_name("credits").clear()
        time.sleep(1)
        driver.find_element_by_name("credits").send_keys("200000000")
        time.sleep(1)
        driver.find_element_by_name("auction_buy_button").send_keys(Keys.ENTER)
        time.sleep(2)

        driver.quit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

