# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_gui(object):
    def setupUi(self, gui):
        gui.setObjectName("gui")
        gui.resize(800, 480)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        gui.setFont(font)
        gui.setStyleSheet("background-color: #242424;\n"
"")
        self.HomePage = QtWidgets.QWidget(gui)
        self.HomePage.setObjectName("HomePage")
        self.StartButton = QtWidgets.QPushButton(self.HomePage)
        self.StartButton.setGeometry(QtCore.QRect(140, 360, 231, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.StartButton.setFont(font)
        self.StartButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.StartButton.setStyleSheet("background-color: #363636;\n"
" border: 2px solid #2d2d2d;\n"
"            color: white;\n"
"            border-radius: 10px")
        self.StartButton.setObjectName("StartButton")
        self.SettingsButton = QtWidgets.QPushButton(self.HomePage)
        self.SettingsButton.setGeometry(QtCore.QRect(30, 350, 91, 101))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.SettingsButton.setFont(font)
        self.SettingsButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SettingsButton.setStyleSheet("background-color: #363636;\n"
" border: 2px solid #2d2d2d;\n"
"            color: white;\n"
"            border-radius: 10px")
        self.SettingsButton.setObjectName("SettingsButton")
        self.Pour_value_S4_Button = QtWidgets.QPushButton(self.HomePage)
        self.Pour_value_S4_Button.setGeometry(QtCore.QRect(190, 280, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Pour_value_S4_Button.setFont(font)
        self.Pour_value_S4_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Pour_value_S4_Button.setStyleSheet("background-color: #363636;\n"
"            color: white;\n"
"            border: 1px solid #363636;\n"
"            border-top-right-radius: 10px; border-bottom-right-radius: 10px;")
        self.Pour_value_S4_Button.setObjectName("Pour_value_S4_Button")
        self.Pour_value_S3_Button = QtWidgets.QPushButton(self.HomePage)
        self.Pour_value_S3_Button.setGeometry(QtCore.QRect(190, 210, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Pour_value_S3_Button.setFont(font)
        self.Pour_value_S3_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Pour_value_S3_Button.setStyleSheet("background-color: #363636;\n"
"            color: white;\n"
"            border: 1px solid #363636;\n"
"            border-top-right-radius: 10px; border-bottom-right-radius: 10px;")
        self.Pour_value_S3_Button.setObjectName("Pour_value_S3_Button")
        self.Pour_value_S2_Button = QtWidgets.QPushButton(self.HomePage)
        self.Pour_value_S2_Button.setGeometry(QtCore.QRect(190, 140, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Pour_value_S2_Button.setFont(font)
        self.Pour_value_S2_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Pour_value_S2_Button.setStyleSheet("background-color: #363636;\n"
"            color: white;\n"
"            border: 1px solid #363636;\n"
"            border-top-right-radius: 10px; border-bottom-right-radius: 10px;")
        self.Pour_value_S2_Button.setObjectName("Pour_value_S2_Button")
        self.Pour_value_S1_Button = QtWidgets.QPushButton(self.HomePage)
        self.Pour_value_S1_Button.setGeometry(QtCore.QRect(190, 70, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.Pour_value_S1_Button.setFont(font)
        self.Pour_value_S1_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Pour_value_S1_Button.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.Pour_value_S1_Button.setAccessibleDescription("")
        self.Pour_value_S1_Button.setStyleSheet("background-color: #363636;\n"
"color: white;\n"
"border: 1px solid #363636;\n"
"border-top-right-radius: 10px; border-bottom-right-radius: 10px;")
        self.Pour_value_S1_Button.setObjectName("Pour_value_S1_Button")
        self.Pour_label = QtWidgets.QLabel(self.HomePage)
        self.Pour_label.setGeometry(QtCore.QRect(60, 10, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.Pour_label.setFont(font)
        self.Pour_label.setStyleSheet("\n"
"            color: white;\n"
"            border-radius: 10px")
        self.Pour_label.setObjectName("Pour_label")
        self.Pour_label1 = QtWidgets.QLabel(self.HomePage)
        self.Pour_label1.setGeometry(QtCore.QRect(80, 70, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Pour_label1.setFont(font)
        self.Pour_label1.setStyleSheet(" border: 2px solid #2d2d2d;\n"
"            color: white;\n"
"            border-top-left-radius: 10px; border-bottom-left-radius: 10px;")
        self.Pour_label1.setFrameShape(QtWidgets.QFrame.Box)
        self.Pour_label1.setObjectName("Pour_label1")
        self.Pour_label2 = QtWidgets.QLabel(self.HomePage)
        self.Pour_label2.setGeometry(QtCore.QRect(80, 140, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Pour_label2.setFont(font)
        self.Pour_label2.setStyleSheet(" border: 2px solid #2d2d2d;\n"
"            color: white;\n"
"            border-top-left-radius: 10px; border-bottom-left-radius: 10px;")
        self.Pour_label2.setFrameShape(QtWidgets.QFrame.Box)
        self.Pour_label2.setObjectName("Pour_label2")
        self.Pour_label3 = QtWidgets.QLabel(self.HomePage)
        self.Pour_label3.setGeometry(QtCore.QRect(80, 210, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Pour_label3.setFont(font)
        self.Pour_label3.setStyleSheet(" border: 2px solid #2d2d2d;\n"
"            color: white;\n"
"            border-top-left-radius: 10px; border-bottom-left-radius: 10px;")
        self.Pour_label3.setFrameShape(QtWidgets.QFrame.Box)
        self.Pour_label3.setObjectName("Pour_label3")
        self.Pour_label4 = QtWidgets.QLabel(self.HomePage)
        self.Pour_label4.setGeometry(QtCore.QRect(80, 280, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Pour_label4.setFont(font)
        self.Pour_label4.setStyleSheet(" border: 2px solid #2d2d2d;\n"
"            color: white;\n"
"            border-top-left-radius: 10px; border-bottom-left-radius: 10px;")
        self.Pour_label4.setFrameShape(QtWidgets.QFrame.Box)
        self.Pour_label4.setObjectName("Pour_label4")
        gui.setCentralWidget(self.HomePage)

        self.retranslateUi(gui)
        QtCore.QMetaObject.connectSlotsByName(gui)

    def retranslateUi(self, gui):
        _translate = QtCore.QCoreApplication.translate
        gui.setWindowTitle(_translate("gui", "MainWindow"))
        self.StartButton.setText(_translate("gui", "start"))
        self.SettingsButton.setText(_translate("gui", "settings\n"
"and\n"
"calibration"))
        self.Pour_value_S4_Button.setText(_translate("gui", "0"))
        self.Pour_value_S3_Button.setText(_translate("gui", "0"))
        self.Pour_value_S2_Button.setText(_translate("gui", "0"))
        self.Pour_value_S1_Button.setText(_translate("gui", "0"))
        self.Pour_label.setWhatsThis(_translate("gui", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.Pour_label.setText(_translate("gui", "      Set Pour Amount (grams)"))
        self.Pour_label1.setText(_translate("gui", "Line 1:"))
        self.Pour_label2.setText(_translate("gui", "Line 2:"))
        self.Pour_label3.setText(_translate("gui", "Line 3:"))
        self.Pour_label4.setText(_translate("gui", "Line 4:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gui = QtWidgets.QMainWindow()
    ui = Ui_gui()
    ui.setupUi(gui)
    gui.show()
    sys.exit(app.exec_())

