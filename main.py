# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\space\Desktop\fill_course_hours\ui\main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import json
import os.path as op
import fill_course_hours

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(692, 377)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.SpanningRole, self.pushButton_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 692, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # connect the two push buttons
        self.pushButton.clicked.connect(self.update_user_info_json)
        self.pushButton_2.clicked.connect(self.generate_excel_sheet)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Couse hour filler"))
        self.label.setText(_translate("MainWindow", "First name "))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "first name"))
        self.label_2.setText(_translate("MainWindow", "Last Name"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "last name"))
        self.label_3.setText(_translate("MainWindow", "Data of Birth"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "date of birth"))
        self.label_4.setText(_translate("MainWindow", "Address"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "address"))
        self.label_5.setText(_translate("MainWindow", "Postal Code"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "postal code"))
        self.label_6.setText(_translate("MainWindow", "SIN#"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "SIN"))
        self.label_7.setText(_translate("MainWindow", "Hourly Rate"))
        self.lineEdit_7.setPlaceholderText(_translate("MainWindow", "hourly rate"))
        self.label_8.setText(_translate("MainWindow", "Increment per Student"))
        self.lineEdit_8.setPlaceholderText(_translate("MainWindow", "increment per student" ))
        self.pushButton.setText(_translate("MainWindow", "Update User Infomation"))
        self.pushButton_2.setText(_translate("MainWindow", "Fill Excel Sheet"))

        if(op.exists("user_info.json")):
            with open("user_info.json", "r") as f:
                info = json.load(f)
            first_name = info['first_name']
            last_name = info['last_name']
            date_of_birth = info['date_of_birth']
            address = info['address']
            postal_code = info['postal_code']
            SIN = info['SIN']
            hourly_rate = info['payment']['hourly_rate']
            increment_per_student = info['payment']['increment_per_student']

            self.lineEdit.setText(_translate("MainWindow", first_name))
            self.lineEdit_2.setText(_translate("MainWindow", last_name))
            self.lineEdit_3.setText(_translate("MainWindow", date_of_birth))
            self.lineEdit_4.setText(_translate("MainWindow", address))
            self.lineEdit_5.setText(_translate("MainWindow", postal_code))
            self.lineEdit_6.setText(_translate("MainWindow", SIN))
            self.lineEdit_7.setText(_translate("MainWindow", str(hourly_rate)))
            self.lineEdit_8.setText(_translate("MainWindow", str(increment_per_student)))

    def update_user_info_json(self):
        first_name = self.lineEdit.text()
        last_name = self.lineEdit_2.text()
        date_of_birth = self.lineEdit_3.text()
        address = self.lineEdit_4.text()
        postal_code = self.lineEdit_5.text()
        SIN = self.lineEdit_6.text()
        hourly_rate = float( self.lineEdit_7.text() )
        increment_per_student = float( self.lineEdit_8.text() )

        data = {
            "last_name": last_name,
            "first_name": first_name,
            "date_of_birth": date_of_birth,
            "address": address,
            "postal_code": postal_code,
            "SIN": SIN,
            "payment":{ "hourly_rate": hourly_rate, "increment_per_student": increment_per_student }
        }
        with open("user_info.json", "w") as f:
            json.dump(data, f)

    def generate_excel_sheet(self):
        fill_course_hours.main()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

