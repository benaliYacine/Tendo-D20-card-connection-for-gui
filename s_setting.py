# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 's_setting.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 480)
        self.AutoCalibrateButton = QtWidgets.QPushButton(Form)
        self.AutoCalibrateButton.setGeometry(QtCore.QRect(390, 402, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AutoCalibrateButton.setFont(font)
        self.AutoCalibrateButton.setObjectName("AutoCalibrateButton")
        self.WriteFlashButton = QtWidgets.QPushButton(Form)
        self.WriteFlashButton.setGeometry(QtCore.QRect(210, 402, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.WriteFlashButton.setFont(font)
        self.WriteFlashButton.setObjectName("WriteFlashButton")
        self.exitButton = QtWidgets.QPushButton(Form)
        self.exitButton.setGeometry(QtCore.QRect(730, 12, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exitButton.setFont(font)
        self.exitButton.setObjectName("exitButton")
        self.HomeButton = QtWidgets.QPushButton(Form)
        self.HomeButton.setGeometry(QtCore.QRect(30, 352, 91, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.HomeButton.setFont(font)
        self.HomeButton.setObjectName("HomeButton")
        self.STATUS_label_2 = QtWidgets.QLabel(Form)
        self.STATUS_label_2.setGeometry(QtCore.QRect(650, 50, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.STATUS_label_2.setFont(font)
        self.STATUS_label_2.setObjectName("STATUS_label_2")
        self.FLUIDCALIBRATION_label_2 = QtWidgets.QLabel(Form)
        self.FLUIDCALIBRATION_label_2.setGeometry(QtCore.QRect(200, 50, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.FLUIDCALIBRATION_label_2.setFont(font)
        self.FLUIDCALIBRATION_label_2.setObjectName("FLUIDCALIBRATION_label_2")
        self.SettingsPageLabel_2 = QtWidgets.QLabel(Form)
        self.SettingsPageLabel_2.setGeometry(QtCore.QRect(20, 0, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SettingsPageLabel_2.setFont(font)
        self.SettingsPageLabel_2.setObjectName("SettingsPageLabel_2")
        self.DAQSETTINGS_label_2 = QtWidgets.QLabel(Form)
        self.DAQSETTINGS_label_2.setGeometry(QtCore.QRect(20, 50, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setUnderline(False)
        self.DAQSETTINGS_label_2.setFont(font)
        self.DAQSETTINGS_label_2.setObjectName("DAQSETTINGS_label_2")
        self.POURSETTINGS_label_2 = QtWidgets.QLabel(Form)
        self.POURSETTINGS_label_2.setGeometry(QtCore.QRect(420, 40, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setUnderline(False)
        self.POURSETTINGS_label_2.setFont(font)
        self.POURSETTINGS_label_2.setObjectName("POURSETTINGS_label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.AutoCalibrateButton.setText(_translate("Form", "AutoCalibrate\n"
"DAQ"))
        self.WriteFlashButton.setText(_translate("Form", "Write Flash"))
        self.exitButton.setText(_translate("Form", "exit"))
        self.HomeButton.setText(_translate("Form", "home"))
        self.STATUS_label_2.setText(_translate("Form", "STATUS:"))
        self.FLUIDCALIBRATION_label_2.setText(_translate("Form", "FLUID CALIBRATION:"))
        self.SettingsPageLabel_2.setText(_translate("Form", "Settings & Calibration:"))
        self.DAQSETTINGS_label_2.setText(_translate("Form", "DAQ SETTINGS:"))
        self.POURSETTINGS_label_2.setText(_translate("Form", "POUR SETTINGS:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

