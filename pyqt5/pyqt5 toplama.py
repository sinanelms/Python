# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'i.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

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
        self.label.setText(str(int(self.top1.text()) + int(self.top2.text())))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

