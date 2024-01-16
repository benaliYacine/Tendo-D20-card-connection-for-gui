#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-
#version 3.7.7 of python w lekhra ta3 pyqt5 w numpy w minimalmodbus w 0.10.0 ta3 pyqtgraph
"""

.. moduleauthor:: benali abderrahmane

This is a Python script that creates a GUI application for data acquisition and visualization. 
It uses the PyQtGraph library for plotting and the MinimalModbus library for communicating with 
a device over a serial port using the Modbus protocol. The script reads configuration data from 
a CSV file and generates a parameter tree in the GUI based on this data. The user can start and 
stop data acquisition, log the acquired data to a file, and adjust the Modbus register values using
the GUI controls. The acquired data is plotted in real-time on a graph.

"""

import argparse
import minimalmodbus
import numpy as np
import sys
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QStackedWidget, QMessageBox


import pyqtgraph as pg
import random

class Ui_gui(object):

    instr = None

    def __init__(self):
        self.time_data = np.zeros(300)
        j = 0
        for index, _ in enumerate(self.time_data):
            self.time_data[index] = j
            j += 0.1

        self.voltage_s1_data = np.ones(300) * 1
        self.voltage_s2_data = np.ones(300) * 2
        self.voltage_s3_data = np.ones(300) * 3
        self.voltage_s4_data = np.ones(300) * 4
        
        
        self.instr = None

    def set_button_style(self, button, style):
        button.setStyleSheet(style)

    normal_button_style = (
        "QPushButton {"
        "background-color: #363636;"
        "border: 3px solid #2d2d2d;"
        "color: white;"
        "border-radius: 15px;"
        "}"
        "QPushButton:hover {"
        "background-color: #2d2d2d;" 
        "}"
        )

    Pour_button_style = (
    "QPushButton {"
    "background-color: #363636;"
    "color: white;"
    "border: 1px solid #363636;"
    "border-top-right-radius: 10px; border-bottom-right-radius: 10px;"
    "}"
    "QPushButton:hover {"
    "background-color: #2d2d2d;" 
    "}"
    )

    Pour_label_style = (
        "border: 2px solid #2d2d2d;\n"
        "color: white;\n"
        "border-top-left-radius: 10px; border-bottom-left-radius: 10px;"
    )

    normal_label_style = (
        "color: white;"
    )

    def set_table_style(self):
        
        style=("""
            QWidget {
                background-color: #2B2B2B;
                color: #FFFFFF;
            }
            QPushButton {
                background-color: #3D3D3D;
                border: 1px solid #5A5A5A;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #5A5A5A;
            }
            QPushButton:pressed {
                background-color: #787878;
            }
            QTableWidget {
                gridline-color: #5A5A5A;
                selection-background-color: #5A5A5A;
                
            }
            QHeaderView::section {
                background-color: #3D3D3D;
                font-size: 8pt;
                padding: 4px;
                border: 1px solid #5A5A5A;
            }
            QLabel {
                color: #FFFFFF;
            }
            QTableCornerButton::section {
                background-color: #3D3D3D;
                border: none;
            }
            """)
        self.DAQSETTINGS_tableWidget.setStyleSheet(style)
        self.FLUIDCALIBRATION_tableWidget.setStyleSheet(style)
        self.POURSETTINGS_tableWidget.setStyleSheet(style)
        self.STATUS_tableWidget.setStyleSheet(style)

    def setupUi(self, gui):
        gui.setObjectName("gui")
        gui.resize(800, 480)
        gui.setWindowTitle("Dynamic GUI")
        self.HomePage = QtWidgets.QWidget(gui)
        self.HomePage.setObjectName("HomePage")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        gui.setFont(font)
        gui.setStyleSheet("background-color: #242424;\n")

        self.StartButton = QtWidgets.QPushButton(self.HomePage)
        self.StartButton.setGeometry(QtCore.QRect(140, 360, 231, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.StartButton.setFont(font)
        self.StartButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.StartButton.setObjectName("StartButton")
        
        self.SettingsButton = QtWidgets.QPushButton(self.HomePage)
        self.SettingsButton.setGeometry(QtCore.QRect(30, 360, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.SettingsButton.setFont(font)
        self.SettingsButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SettingsButton.setObjectName("SettingsButton")
        self.Pour_value_S4_Button = QtWidgets.QPushButton(self.HomePage)
        self.Pour_value_S4_Button.setGeometry(QtCore.QRect(190, 280, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Pour_value_S4_Button.setFont(font)
        self.Pour_value_S4_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Pour_value_S4_Button.setObjectName("Pour_value_S4_Button")
        self.Pour_value_S3_Button = QtWidgets.QPushButton(self.HomePage)
        self.Pour_value_S3_Button.setGeometry(QtCore.QRect(190, 210, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Pour_value_S3_Button.setFont(font)
        self.Pour_value_S3_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Pour_value_S3_Button.setObjectName("Pour_value_S3_Button")
        self.Pour_value_S2_Button = QtWidgets.QPushButton(self.HomePage)
        self.Pour_value_S2_Button.setGeometry(QtCore.QRect(190, 140, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Pour_value_S2_Button.setFont(font)
        self.Pour_value_S2_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.Pour_value_S1_Button.setObjectName("Pour_value_S1_Button")
        self.Pour_label = QtWidgets.QLabel(self.HomePage)
        self.Pour_label.setGeometry(QtCore.QRect(60, 10, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Pour_label.setFont(font)
        self.Pour_label.setObjectName("Pour_label")
        self.Pour_label1 = QtWidgets.QLabel(self.HomePage)
        self.Pour_label1.setGeometry(QtCore.QRect(80, 70, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Pour_label1.setFont(font)
        self.Pour_label1.setFrameShape(QtWidgets.QFrame.Box)
        self.Pour_label1.setObjectName("Pour_label1")
        self.Pour_label2 = QtWidgets.QLabel(self.HomePage)
        self.Pour_label2.setGeometry(QtCore.QRect(80, 140, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Pour_label2.setFont(font)
        self.Pour_label2.setFrameShape(QtWidgets.QFrame.Box)
        self.Pour_label2.setObjectName("Pour_label2")
        self.Pour_label3 = QtWidgets.QLabel(self.HomePage)
        self.Pour_label3.setGeometry(QtCore.QRect(80, 210, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Pour_label3.setFont(font)
        self.Pour_label3.setFrameShape(QtWidgets.QFrame.Box)
        self.Pour_label3.setObjectName("Pour_label3")
        self.Pour_label4 = QtWidgets.QLabel(self.HomePage)
        self.Pour_label4.setGeometry(QtCore.QRect(80, 280, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Pour_label4.setFont(font)
        self.Pour_label4.setFrameShape(QtWidgets.QFrame.Box)
        self.Pour_label4.setObjectName("Pour_label4")


        #home_page_styling
        self.set_button_style(self.StartButton, self.normal_button_style)
        self.set_button_style(self.SettingsButton, self.normal_button_style)
        

        for button in [
            self.Pour_value_S4_Button,
            self.Pour_value_S3_Button,
            self.Pour_value_S2_Button,
            self.Pour_value_S1_Button,
        ]:
            self.set_button_style(button, self.Pour_button_style)

        self.Pour_label.setStyleSheet("color: white;\n" "border-radius: 10px")

        for label in [
            self.Pour_label1,
            self.Pour_label2,
            self.Pour_label3,
            self.Pour_label4,
        ]:
            self.set_button_style(label, self.Pour_label_style)


        #setup the setting page
        self.SettingsPage = QtWidgets.QWidget(gui)
        self.SettingsPage.setObjectName("SettingsPage")

        ##the new
        self.AutoCalibrateButton = QtWidgets.QPushButton(self.SettingsPage)
        self.AutoCalibrateButton.setGeometry(QtCore.QRect(390, 402, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AutoCalibrateButton.setFont(font)
        self.AutoCalibrateButton.setObjectName("AutoCalibrateButton")
        self.WriteFlashButton = QtWidgets.QPushButton(self.SettingsPage)
        self.WriteFlashButton.setGeometry(QtCore.QRect(210, 402, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.WriteFlashButton.setFont(font)
        self.WriteFlashButton.setObjectName("WriteFlashButton")
        self.HomeButton = QtWidgets.QPushButton(self.SettingsPage)
        self.HomeButton.setGeometry(QtCore.QRect(30, 360, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.HomeButton.setFont(font)
        self.HomeButton.setObjectName("HomeButton")
        self.STATUS_label = QtWidgets.QLabel(self.SettingsPage)
        self.STATUS_label.setGeometry(QtCore.QRect(650, 50, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.STATUS_label.setFont(font)
        self.STATUS_label.setObjectName("STATUS_label_2")
        self.FLUIDCALIBRATION_label = QtWidgets.QLabel(self.SettingsPage)
        self.FLUIDCALIBRATION_label.setGeometry(QtCore.QRect(200, 50, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.FLUIDCALIBRATION_label.setFont(font)
        self.FLUIDCALIBRATION_label.setObjectName("FLUIDCALIBRATION_label")
        self.SettingsPageLabel = QtWidgets.QLabel(self.SettingsPage)
        self.SettingsPageLabel.setGeometry(QtCore.QRect(20, 0, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SettingsPageLabel.setFont(font)
        self.SettingsPageLabel.setObjectName("SettingsPageLabel")
        self.DAQSETTINGS_label = QtWidgets.QLabel(self.SettingsPage)
        self.DAQSETTINGS_label.setGeometry(QtCore.QRect(20, 50, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setUnderline(False)
        self.DAQSETTINGS_label.setFont(font)
        self.DAQSETTINGS_label.setObjectName("DAQSETTINGS_label")
        self.POURSETTINGS_label = QtWidgets.QLabel(self.SettingsPage)
        self.POURSETTINGS_label.setGeometry(QtCore.QRect(420, 40, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setUnderline(False)
        self.POURSETTINGS_label.setFont(font)
        self.POURSETTINGS_label.setObjectName("POURSETTINGS_label")
        self.exitButton = QtWidgets.QPushButton(self.SettingsPage)
        self.exitButton.setGeometry(QtCore.QRect(740, 12, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exitButton.setFont(font)
        self.exitButton.setObjectName("exitButton")

        #tables setup
        self.DAQSETTINGS_tableWidget = QtWidgets.QTableWidget(self.SettingsPage)
        self.DAQSETTINGS_tableWidget.setGeometry(0, 78, 202, 180)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        #font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.DAQSETTINGS_tableWidget.setFont(font)
        self.DAQSETTINGS_tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        #self.DAQSETTINGS_tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        #self.DAQSETTINGS_tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.DAQSETTINGS_tableWidget.setLineWidth(1)
        self.DAQSETTINGS_tableWidget.setAutoScrollMargin(8)
        self.DAQSETTINGS_tableWidget.setObjectName("DAQSETTINGS_tableWidget")
        self.DAQSETTINGS_tableWidget.setColumnCount(1)
        self.DAQSETTINGS_tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.DAQSETTINGS_tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.DAQSETTINGS_tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.DAQSETTINGS_tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.DAQSETTINGS_tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.DAQSETTINGS_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.DAQSETTINGS_tableWidget.setItem(0, 0, item)
        self.DAQSETTINGS_tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.DAQSETTINGS_tableWidget.horizontalHeader().setDefaultSectionSize(80)
        self.DAQSETTINGS_tableWidget.horizontalHeader().setMinimumSectionSize(40)
        self.DAQSETTINGS_tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.DAQSETTINGS_tableWidget.horizontalHeader().setStretchLastSection(False)
        self.DAQSETTINGS_tableWidget.verticalHeader().setDefaultSectionSize(34)
        self.DAQSETTINGS_tableWidget.verticalHeader().setMinimumSectionSize(7)
        
        self.FLUIDCALIBRATION_tableWidget = QtWidgets.QTableWidget(self.SettingsPage)
        self.FLUIDCALIBRATION_tableWidget.setGeometry(QtCore.QRect(200, 78, 202, 315))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.FLUIDCALIBRATION_tableWidget.setFont(font)
        self.FLUIDCALIBRATION_tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        #self.FLUIDCALIBRATION_tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.FLUIDCALIBRATION_tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.FLUIDCALIBRATION_tableWidget.setLineWidth(1)
        self.FLUIDCALIBRATION_tableWidget.setAutoScrollMargin(8)
        self.FLUIDCALIBRATION_tableWidget.setObjectName("FLUIDCALIBRATION_tableWidget")
        self.FLUIDCALIBRATION_tableWidget.setColumnCount(1)
        self.FLUIDCALIBRATION_tableWidget.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.FLUIDCALIBRATION_tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.FLUIDCALIBRATION_tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.FLUIDCALIBRATION_tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.FLUIDCALIBRATION_tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.FLUIDCALIBRATION_tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.FLUIDCALIBRATION_tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.FLUIDCALIBRATION_tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.FLUIDCALIBRATION_tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.FLUIDCALIBRATION_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.FLUIDCALIBRATION_tableWidget.setItem(0, 0, item)
        self.FLUIDCALIBRATION_tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.FLUIDCALIBRATION_tableWidget.horizontalHeader().setDefaultSectionSize(80)
        self.FLUIDCALIBRATION_tableWidget.horizontalHeader().setMinimumSectionSize(40)
        self.FLUIDCALIBRATION_tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.FLUIDCALIBRATION_tableWidget.horizontalHeader().setStretchLastSection(False)
        self.FLUIDCALIBRATION_tableWidget.verticalHeader().setDefaultSectionSize(34)
        self.FLUIDCALIBRATION_tableWidget.verticalHeader().setMinimumSectionSize(7)
        self.POURSETTINGS_tableWidget = QtWidgets.QTableWidget(self.SettingsPage)
        self.POURSETTINGS_tableWidget.setGeometry(QtCore.QRect(400, 78, 202, 212))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.POURSETTINGS_tableWidget.setFont(font)
        self.POURSETTINGS_tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        #self.POURSETTINGS_tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.POURSETTINGS_tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.POURSETTINGS_tableWidget.setLineWidth(1)
        self.POURSETTINGS_tableWidget.setAutoScrollMargin(8)
        self.POURSETTINGS_tableWidget.setObjectName("POURSETTINGS_tableWidget")
        self.POURSETTINGS_tableWidget.setColumnCount(1)
        self.POURSETTINGS_tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.POURSETTINGS_tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.POURSETTINGS_tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.POURSETTINGS_tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.POURSETTINGS_tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.POURSETTINGS_tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.POURSETTINGS_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.POURSETTINGS_tableWidget.setItem(0, 0, item)
        self.POURSETTINGS_tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.POURSETTINGS_tableWidget.horizontalHeader().setDefaultSectionSize(80)
        self.POURSETTINGS_tableWidget.horizontalHeader().setMinimumSectionSize(40)
        self.POURSETTINGS_tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.POURSETTINGS_tableWidget.horizontalHeader().setStretchLastSection(False)
        self.POURSETTINGS_tableWidget.verticalHeader().setDefaultSectionSize(34)
        self.POURSETTINGS_tableWidget.verticalHeader().setMinimumSectionSize(7)
        self.STATUS_tableWidget = QtWidgets.QTableWidget(self.SettingsPage)
        self.STATUS_tableWidget.setGeometry(QtCore.QRect(600, 78, 190, 407))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.STATUS_tableWidget.setFont(font)
        self.STATUS_tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        #self.STATUS_tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.STATUS_tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.STATUS_tableWidget.setLineWidth(1)
        self.STATUS_tableWidget.setAutoScrollMargin(8)
        self.STATUS_tableWidget.setObjectName("STATUS_tableWidget")
        self.STATUS_tableWidget.setColumnCount(1)
        self.STATUS_tableWidget.setRowCount(13)
        item = QtWidgets.QTableWidgetItem()
        
        self.STATUS_tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        
        self.STATUS_tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        
        self.STATUS_tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        
        self.STATUS_tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        
        self.STATUS_tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        
        self.STATUS_tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        
        self.STATUS_tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        
        self.STATUS_tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        
        self.STATUS_tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        
        self.STATUS_tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        
        self.STATUS_tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        
        self.STATUS_tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        
        self.STATUS_tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        
        self.STATUS_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
        self.STATUS_tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
        self.STATUS_tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
        self.STATUS_tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
        self.STATUS_tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
        self.STATUS_tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
        self.STATUS_tableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
        self.STATUS_tableWidget.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
        self.STATUS_tableWidget.setItem(0, 7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
        self.STATUS_tableWidget.setItem(0, 8, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
        self.STATUS_tableWidget.setItem(0, 9, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
        self.STATUS_tableWidget.setItem(0, 10, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
        self.STATUS_tableWidget.setItem(0, 11, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
        self.STATUS_tableWidget.setItem(0, 12, item)

        self.STATUS_tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.STATUS_tableWidget.horizontalHeader().setDefaultSectionSize(87)
        self.STATUS_tableWidget.horizontalHeader().setMinimumSectionSize(36)
        self.STATUS_tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.STATUS_tableWidget.horizontalHeader().setStretchLastSection(False)
        self.STATUS_tableWidget.verticalHeader().setDefaultSectionSize(28)
        self.STATUS_tableWidget.verticalHeader().setMinimumSectionSize(7)
        self.set_table_style()

        #settings_page_styling
        self.set_button_style(self.HomeButton, self.normal_button_style)
        self.set_button_style(self.SettingsPageLabel, self.normal_label_style)
        self.set_button_style(self.WriteFlashButton, self.normal_button_style)
        self.set_button_style(self.AutoCalibrateButton, self.normal_button_style)
        self.set_button_style(self.exitButton, self.normal_button_style)
        self.set_button_style(self.DAQSETTINGS_label, self.normal_label_style)
        self.set_button_style(self.FLUIDCALIBRATION_label, self.normal_label_style)
        self.set_button_style(self.POURSETTINGS_label, self.normal_label_style)
        self.set_button_style(self.STATUS_label, self.normal_label_style)

        #setup graph

        self.retranslateUi(gui)
        QtCore.QMetaObject.connectSlotsByName(gui)
        
        self.graphWidget = pg.PlotWidget(self.HomePage)
        self.graphWidget.setGeometry(QtCore.QRect(400, 0, 420, 480))
        self.graphWidget.setObjectName("graphWidget")
        self.graphWidget.plotItem.showGrid(x=True,y=True,alpha=1)

        self.setupGraph(ui.time_data, ui.voltage_s1_data, ui.voltage_s2_data, ui.voltage_s3_data, ui.voltage_s4_data)

        # Create a stacked widget
        self.stacked_widget = QStackedWidget(gui)
        gui.setCentralWidget(self.stacked_widget)
        
        # Add HomePage and SettingsPage to the stacked widget
        self.stacked_widget.addWidget(self.HomePage)
        self.stacked_widget.addWidget(self.SettingsPage)
        
        # Set HomePage as the default widget
        self.stacked_widget.setCurrentWidget(self.HomePage)

    def retranslateUi(self, gui):
        _translate = QtCore.QCoreApplication.translate
        gui.setWindowTitle(_translate("gui", "gui"))
        self.StartButton.setText(_translate("gui", "Start"))
        self.StartButton.clicked.connect(lambda: self.setRH(43, 1, "u16bit"))
        self.SettingsButton.clicked.connect(self.switch_to_settings)
        setting_icon = QIcon('icons/settings.png')
        self.SettingsButton.setIcon(setting_icon)
        self.SettingsButton.setIconSize(self.SettingsButton.size())
        self.Pour_value_S4_Button.setText(_translate("gui", ""))
        self.Pour_value_S4_Button.clicked.connect(lambda: self.set_pour(self.Pour_value_S4_Button,50))
        self.Pour_value_S3_Button.setText(_translate("gui", ""))
        self.Pour_value_S3_Button.clicked.connect(lambda: self.set_pour(self.Pour_value_S3_Button,48))
        self.Pour_value_S2_Button.setText(_translate("gui", ""))
        self.Pour_value_S2_Button.clicked.connect(lambda: self.set_pour(self.Pour_value_S2_Button,46))
        self.Pour_value_S1_Button.setText(_translate("gui", ""))
        self.Pour_value_S1_Button.clicked.connect(lambda: self.set_pour(self.Pour_value_S1_Button,44))
        self.Pour_label.setText(_translate("gui", "   Set Pour Amount (grams)"))
        self.Pour_label1.setText(_translate("gui", "Line 1:"))
        self.Pour_label2.setText(_translate("gui", "Line 2:"))
        self.Pour_label3.setText(_translate("gui", "Line 3:"))
        self.Pour_label4.setText(_translate("gui", "Line 4:"))

        #setting page

        #self.HomeButton.setText(_translate("gui", "Home"))
        self.HomeButton.clicked.connect(self.switch_to_main)
        home_icon = QIcon('icons/home.png')
        self.HomeButton.setIcon(home_icon)
        self.HomeButton.setIconSize(self.HomeButton.size())
        self.SettingsPageLabel.setText(_translate("gui", "Settings & Calibration:"))
        self.WriteFlashButton.setText(_translate("gui", "Write Flash"))
        self.WriteFlashButton.clicked.connect(self.confirm_WriteFlash)
        self.AutoCalibrateButton.setText(_translate("gui", "AutoCalibrate\n"
"DAQ"))
        self.AutoCalibrateButton.clicked.connect(self.confirm_AutoCalibrate)
        #self.exitButton.setText(_translate("gui", "Exit"))
        self.exitButton.clicked.connect(self.confirm_exit)
        exit_icon = QIcon('icons/close.png')
        self.exitButton.setIcon(exit_icon)
        self.exitButton.setIconSize(self.exitButton.size())
        item = self.DAQSETTINGS_tableWidget.verticalHeaderItem(0)
        item.setText(_translate("gui", "CALIBRATION_S1"))
        item = self.DAQSETTINGS_tableWidget.verticalHeaderItem(1)
        item.setText(_translate("gui", "CALIBRATION_S2"))
        item = self.DAQSETTINGS_tableWidget.verticalHeaderItem(2)
        item.setText(_translate("gui", "CALIBRATION_S3"))
        item = self.DAQSETTINGS_tableWidget.verticalHeaderItem(3)
        item.setText(_translate("gui", "CALIBRATION_S4"))
        item = self.DAQSETTINGS_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("gui", "Value"))
        __sortingEnabled = self.DAQSETTINGS_tableWidget.isSortingEnabled()
        self.DAQSETTINGS_tableWidget.setSortingEnabled(False)
        self.DAQSETTINGS_tableWidget.setSortingEnabled(__sortingEnabled)
        self.DAQSETTINGS_label.setText(_translate("gui", "DAQ SETTINGS:"))
        item = self.FLUIDCALIBRATION_tableWidget.verticalHeaderItem(0)
        item.setText(_translate("gui", "SENS_COFF_A_S1"))
        item = self.FLUIDCALIBRATION_tableWidget.verticalHeaderItem(1)
        item.setText(_translate("gui", "SENS_COFF_B_S1"))
        item = self.FLUIDCALIBRATION_tableWidget.verticalHeaderItem(2)
        item.setText(_translate("gui", "SENS_COFF_A_S3"))
        item = self.FLUIDCALIBRATION_tableWidget.verticalHeaderItem(3)
        item.setText(_translate("gui", "SENS_COFF_A_S4"))
        item = self.FLUIDCALIBRATION_tableWidget.verticalHeaderItem(4)
        item.setText(_translate("gui", "SENS_COFF_B_S1"))
        item = self.FLUIDCALIBRATION_tableWidget.verticalHeaderItem(5)
        item.setText(_translate("gui", "SENS_COFF_B_S2"))
        item = self.FLUIDCALIBRATION_tableWidget.verticalHeaderItem(6)
        item.setText(_translate("gui", "SENS_COFF_B_S3"))
        item = self.FLUIDCALIBRATION_tableWidget.verticalHeaderItem(7)
        item.setText(_translate("gui", "SENS_COFF_B_S4"))
        item = self.FLUIDCALIBRATION_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("gui", "Value"))
        __sortingEnabled = self.FLUIDCALIBRATION_tableWidget.isSortingEnabled()
        self.FLUIDCALIBRATION_tableWidget.setSortingEnabled(False)
        self.FLUIDCALIBRATION_tableWidget.setSortingEnabled(__sortingEnabled)
        item = self.POURSETTINGS_tableWidget.verticalHeaderItem(0)
        item.setText(_translate("gui", "Pour_Control"))
        item = self.POURSETTINGS_tableWidget.verticalHeaderItem(1)
        item.setText(_translate("gui", "POUR_VALUE_S1"))
        item = self.POURSETTINGS_tableWidget.verticalHeaderItem(2)
        item.setText(_translate("gui", "POUR_VALUE_S2"))
        item = self.POURSETTINGS_tableWidget.verticalHeaderItem(3)
        item.setText(_translate("gui", "POUR_VALUE_S3"))
        item = self.POURSETTINGS_tableWidget.verticalHeaderItem(4)
        item.setText(_translate("gui", "POUR_VALUE_S4"))
        item = self.POURSETTINGS_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("gui", "Value"))
        __sortingEnabled = self.POURSETTINGS_tableWidget.isSortingEnabled()
        self.POURSETTINGS_tableWidget.setSortingEnabled(False)
        self.POURSETTINGS_tableWidget.setSortingEnabled(__sortingEnabled)
        item = self.STATUS_tableWidget.verticalHeaderItem(0)
        item.setText(_translate("gui", "Voltage_S1"))
        item = self.STATUS_tableWidget.verticalHeaderItem(1)
        item.setText(_translate("gui", "Voltage_S2"))
        item = self.STATUS_tableWidget.verticalHeaderItem(2)
        item.setText(_translate("gui", "Voltage_S3"))
        item = self.STATUS_tableWidget.verticalHeaderItem(3)
        item.setText(_translate("gui", "Voltage_S4"))
        item = self.STATUS_tableWidget.verticalHeaderItem(4)
        item.setText(_translate("gui", "New Row"))
        item = self.STATUS_tableWidget.verticalHeaderItem(5)
        item.setText(_translate("gui", "Flow_S1"))
        item = self.STATUS_tableWidget.verticalHeaderItem(6)
        item.setText(_translate("gui", "Flow_S3"))
        item = self.STATUS_tableWidget.verticalHeaderItem(7)
        item.setText(_translate("gui", "Flow_S4"))
        item = self.STATUS_tableWidget.verticalHeaderItem(8)
        item.setText(_translate("gui", "New Row"))
        item = self.STATUS_tableWidget.verticalHeaderItem(9)
        item.setText(_translate("gui", "RTD_S1"))
        item = self.STATUS_tableWidget.verticalHeaderItem(10)
        item.setText(_translate("gui", "RTD_S2"))
        item = self.STATUS_tableWidget.verticalHeaderItem(11)
        item.setText(_translate("gui", "RTD_S3"))
        item = self.STATUS_tableWidget.verticalHeaderItem(12)
        item.setText(_translate("gui", "UNIT_STATUS "))
        item = self.STATUS_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("gui", "Value"))
        __sortingEnabled = self.STATUS_tableWidget.isSortingEnabled()
        self.STATUS_tableWidget.setSortingEnabled(False)
        self.STATUS_tableWidget.setSortingEnabled(__sortingEnabled)
        self.FLUIDCALIBRATION_label.setText(_translate("gui", "FLUID CALIBRATION SETTINGS:"))
        self.POURSETTINGS_label.setText(_translate("gui", "POUR SETTINGS:"))
        self.STATUS_label.setText(_translate("gui", "STATUS:"))

        self.setupDeafaultTableValues()

        self.DAQSETTINGS_tableWidget.cellChanged.connect(lambda row, column : self.on_cell_changed(row,column,1))
        self.FLUIDCALIBRATION_tableWidget.cellChanged.connect(lambda row, column : self.on_cell_changed(row,column,2))
        self.POURSETTINGS_tableWidget.cellChanged.connect(lambda row, column : self.on_cell_changed(row,column,3))

    def comUpdate(self):#hadi lfct lwahida li sta3melna fiha minimalmodbus
        try:    
            minimalmodbus._print_out(f"Port: {args.port}, Address: {args.adr}")
            self.instr = minimalmodbus.Instrument(args.port, args.adr)#esah ga3 fi l'Instrument instr biha te9der tmed l registre mo3ayan valeur /te9ra lvaleur li fi registre etc..
            # Setup serial port
            self.instr.serial.parity=minimalmodbus.serial.PARITY_NONE
            self.instr.serial.baudrate=115200
            self.instr.serial.bytesize=8
            self.instr.serial.stopbits=1
            self.instr.serial.timeout=1
            self.instr.handle_local_echo = False
            self.instr.debug = False
            self.instr.serial.timeout = 1.0
            self.instr.mode= minimalmodbus.MODE_RTU
            self.instr.clear_buffers_before_each_transaction=True
            print(self.instr)
        except (RuntimeError, TypeError, NameError, IOError, ValueError):
            print("could not open port '/dev/ttyUSB0'")
            return 0    

    def update_notopti(self):
            if self.instr == None:
                # Shift voltage data arrays to the left by one element
                self.voltage_s1_data = np.roll(self.voltage_s1_data, -1)
                self.voltage_s2_data = np.roll(self.voltage_s2_data, -1)
                self.voltage_s3_data = np.roll(self.voltage_s3_data, -1)
                self.voltage_s4_data = np.roll(self.voltage_s4_data, -1)

                # Replace the last element of each voltage data array with the corresponding value
                self.voltage_s1_data[-1] = random.uniform(0,1)
                self.voltage_s2_data[-1] = random.uniform(1,2)
                self.voltage_s3_data[-1] = random.uniform(2,3)
                self.voltage_s4_data[-1] = random.uniform(3,4)
                
                # Update time data
                self.time_data = np.roll(self.time_data, -1)
                self.time_data[-1] = self.time_data[-2] + 0.1
                self.updateGraph(self.time_data, self.voltage_s1_data, self.voltage_s2_data, self.voltage_s3_data, self.voltage_s4_data)
                
                return 
            
            self.comUpdate()
            
            # Read voltage values
            voltage_s1 = self.instr.read_float(34, functioncode=4)
            voltage_s2 = self.instr.read_float(36, functioncode=4)
            voltage_s3 = self.instr.read_float(38, functioncode=4)
            voltage_s4 = self.instr.read_float(40, functioncode=4)
            
            # Shift voltage data arrays to the left by one element
            voltage_s1_data = np.roll(voltage_s1_data, -1)
            voltage_s2_data = np.roll(voltage_s2_data, -1)
            voltage_s3_data = np.roll(voltage_s3_data, -1)
            voltage_s4_data = np.roll(voltage_s4_data, -1)

            # Replace the last element of each voltage data array with the corresponding value
            voltage_s1_data[-1] = voltage_s1
            voltage_s2_data[-1] = voltage_s2
            voltage_s3_data[-1] = voltage_s3
            voltage_s4_data[-1] = voltage_s4
            
            # Update time data
            time_data = np.roll(time_data, -1)
            time_data[-1] = time_data[-2] + 0.1
            
            self.updateGraph(time_data, voltage_s1_data, voltage_s2_data, voltage_s3_data, voltage_s4_data)    

    def shift_data_arrays(self):
        # Shift voltage and time data arrays to the left by one element
        self.voltage_s1_data = np.roll(self.voltage_s1_data, -1)
        self.voltage_s2_data = np.roll(self.voltage_s2_data, -1)
        self.voltage_s3_data = np.roll(self.voltage_s3_data, -1)
        self.voltage_s4_data = np.roll(self.voltage_s4_data, -1)
        self.time_data = np.roll(self.time_data, -1)

    def generate_random_voltages(self):
        self.voltage_s1_data[-1] = random.uniform(0, 1)
        self.voltage_s2_data[-1] = random.uniform(1, 2)
        self.voltage_s3_data[-1] = random.uniform(2, 3)
        self.voltage_s4_data[-1] = random.uniform(3, 4)

    def update(self):
        self.shift_data_arrays()
        #****************************************************
        if self.instr is None:
            self.generate_random_voltages()
            self.time_data[-1] = self.time_data[-2] + 0.1
        else:
            self.comUpdate()

            # Read voltage values
            voltage_s1 = self.instr.read_float(34, functioncode=4)
            voltage_s2 = self.instr.read_float(36, functioncode=4)
            voltage_s3 = self.instr.read_float(38, functioncode=4)
            voltage_s4 = self.instr.read_float(40, functioncode=4)

            # Replace the last element of each voltage data array with the corresponding value
            self.voltage_s1_data[-1] = voltage_s1
            self.voltage_s2_data[-1] = voltage_s2
            self.voltage_s3_data[-1] = voltage_s3
            self.voltage_s4_data[-1] = voltage_s4

            # Update time data
            self.time_data[-1] = self.time_data[-2] + 0.1

        self.updateGraph(self.time_data, self.voltage_s1_data, self.voltage_s2_data, self.voltage_s3_data, self.voltage_s4_data)

    def setupGraph(self, time_data, voltage_s1_data, voltage_s2_data, voltage_s3_data, voltage_s4_data):
        plot = self.graphWidget
        plot.setTitle("Signal Graph")
        plot.setLabel("left", "Voltage", units="V")
        plot.setLabel("bottom", "Time", units="s")
        legend = plot.addLegend()
        plot.setYRange(0, 12)
        # Create plot curves for each voltage
        self.curve_s1 = plot.plot(pen="r", name="Voltage_S1")
        self.curve_s2 = plot.plot(pen="g", name="Voltage_S2")
        self.curve_s3 = plot.plot(pen="b", name="Voltage_S3")
        self.curve_s4 = plot.plot(pen="y", name="Voltage_S4")

        self.curve_s1.setData(self.time_data, voltage_s1_data)
        self.curve_s2.setData(self.time_data, voltage_s2_data)
        self.curve_s3.setData(self.time_data, voltage_s3_data)
        self.curve_s4.setData(self.time_data, voltage_s4_data)

        plot.setMouseEnabled(x=False, y=False)  # Disable mouse interaction
        plot.setInteractive(False)  # Disable any interactive features

    def updateGraph(self, time_data, voltage_s1_data, voltage_s2_data, voltage_s3_data, voltage_s4_data):
        self.curve_s1.setData(time_data, voltage_s1_data)
        self.curve_s2.setData(time_data, voltage_s2_data)
        self.curve_s3.setData(time_data, voltage_s3_data)
        self.curve_s4.setData(time_data, voltage_s4_data)
        QtGui.QGuiApplication.processEvents()

    def setRH(self,addr,data,dbtype):
        if addr==43:
            self.StartButton.setText("started")
        #********************************************************************    
        return#matensach tnahi hada estar memba3d
        self.comUpdate()
        try:
            if dbtype=='u16bit':
                self.instr.write_register(addr, data)
            if dbtype=='16bit':
                self.instr.write_register(addr, data)
            elif dbtype=='32bit':
                self.instr.write_long(addr, data, signed=True)
            elif dbtype=='u32bit':
                self.instr.write_long(addr, data, signed=False)
            elif dbtype=='Float':
                self.instr.write_float(addr, data)
            QtGui.QGuiApplication.processEvents()

        except RuntimeError:
            print("RuntimeError occurred while setting RH")
        except (TypeError, NameError, IOError, ValueError) as e:
            print(f"An error occurred while setting RH: {e}")
        
        self.setupDeafaultTableValues()

    def readRI(self,addr,div,dbtype):
        if self.instr == None:
            #☻***********************************************
            return random.uniform(0,12)
        try:
            self.comUpdate()
            val=0
            if dbtype=='u16bit':
                val=self.instr.read_register((int(addr)), functioncode=4, signed=False)
            elif dbtype=='16bit':
                val=self.instr.read_register((int(addr)), functioncode=4, signed=True)
            elif dbtype=='32bit':
                val=self.instr.read_long(int(addr), functioncode=4)
            elif dbtype=='Float':
                val=self.instr.read_float(int(addr), functioncode=4)

            if div=='10':
                val=val/10
            if div=='100':
                val=val/100  
            return val
        except (RuntimeError, TypeError, NameError, IOError, ValueError):
            print("RuntimeError RI: No value")
            return 0

    def updateStatueTable(self):
        Statue_items = [
            ('UNIT_STATUS', 7, 0, '16bit'),
            ('RTD_S1', 20, 100, '16bit'),
            ('RTD_S2', 21, 100, '16bit'),
            ('RTD_S3', 22, 100, '16bit'),
            ('RTD_S4', 23, 100, '16bit'),
            ('VOLTAGE_S1', 34, 0, 'float'),
            ('VOLTAGE_S2', 36, 0, 'float'),
            ('VOLTAGE_S3', 38, 0, 'float'),
            ('VOLTAGE_S4', 40, 0, 'float'),
            ('FLOW_S1', 48, 0, 'float'),
            ('FLOW_S2', 50, 0, 'float'),
            ('FLOW_S3', 52, 0, 'float'),
            ('FLOW_S4', 54, 0, '16bit')
        ]

        for i, (name, addr, div, dbtype) in enumerate(Statue_items):
            value = self.readRI(addr, div, dbtype)
            item = QtWidgets.QTableWidgetItem(str(value))
            self.STATUS_tableWidget.setItem(i, 0, item)

    def readRh(self,addr,dbtype):
        if self.instr == None:
            #☻***********************************************
            return 0
        try:
            self.comUpdate()
            val=0
            if dbtype=='u16bit':
                val=self.instr.read_register((int(addr)), functioncode=3, signed=False)
            elif dbtype=='16bit':
                val=self.instr.read_register(int(addr), functioncode=3, signed=True)
            elif dbtype=='32bit':
                val=self.instr.read_long(int(addr), functioncode=3, signed=True)
            elif dbtype=='u32bit':
                val=self.instr.read_long(int(addr), functioncode=3, signed=False)
            elif dbtype=='Float':
                val=self.instr.read_float(int(addr), functioncode=3)

            return val
        except (RuntimeError, TypeError, NameError, IOError, ValueError):
            print("RuntimeError Rh: No value")
            return 0

    def setupDeafaultTableValues(self):
        for i, addr in enumerate(range(6, 10)):
            value = self.readRh(addr,'u16bit')
            item = QtWidgets.QTableWidgetItem(str(value))
            self.DAQSETTINGS_tableWidget.setItem(i, 0, item)

        for i, addr in enumerate(range(15, 22, 2)):
            value = self.readRh(addr,'Float')
            item = QtWidgets.QTableWidgetItem(str(value))
            self.FLUIDCALIBRATION_tableWidget.setItem(i,0,item)

        for i, addr in enumerate(range(29, 36, 2),4):
            value = self.readRh(addr,'Float')
            item = QtWidgets.QTableWidgetItem(str(value))
            self.FLUIDCALIBRATION_tableWidget.setItem(i,0,item)

        value = self.readRh(43, 'u16bit')
        item = QtWidgets.QTableWidgetItem(str(value))
        self.POURSETTINGS_tableWidget.setItem(0, 0, item)    

        for i, addr in enumerate(range(44, 51, 2),1):
            value = self.readRh(addr, 'Float')
            item = QtWidgets.QTableWidgetItem(str(value))
            self.POURSETTINGS_tableWidget.setItem(i, 0, item)

    def set_pour(self,pour_button,adrr):
        if pour_button.text()=="":
            pour_button.setText("0")
            self.setRH(adrr,0,"Float")
        
        elif float(pour_button.text())==0 :
            pour_button.setText("0.75")
            self.setRH(adrr,0.75,"Float")


        elif float(pour_button.text())==0.75 :
            pour_button.setText("1")
            self.setRH(adrr,1,"Float")

        elif float(pour_button.text())==1 :
            pour_button.setText("1.5")
            self.setRH(adrr,1.5,"Float")

        elif float(pour_button.text())==1.5 :
            pour_button.setText("2")
            self.setRH(adrr,2,"Float")

        elif float(pour_button.text())==2 :
            pour_button.setText("3")
            self.setRH(adrr,3,"Float")

        elif float(pour_button.text())==3 :
            pour_button.setText("0")
            self.setRH(adrr,0,"Float")

    def confirm_WriteFlash(self):
        # Create a QMessageBox
        msgBox = QMessageBox()
        
        msgBox.setText("ARE YOU SURE?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setDefaultButton(QMessageBox.No)

        # Apply the dark theme stylesheet
        msgBox.setStyleSheet('''
        QWidget {
            background-color: #2b2b2b;
            color: white;
            selection-background-color: #4a4a4a;
            selection-color: white;
            font-family: Arial;
            font-size: 18px;
        }
        QPushButton {
            font-size: 16pt;
            background-color: #555555;
            color: white;
            border: none;
            padding: 5px 10px 5px 10px;
            border-radius: 5px;
        }

        QPushButton:hover {
            background-color: #4a4a4a;
        }
        ''')

        # Show the QMessageBox and get the user's response
        
        reply = msgBox.exec_()
        if reply == QMessageBox.Yes:
            self.setRH(62, 1, "16bit")

    def confirm_AutoCalibrate(self):
        
        # Create a QMessageBox
        msgBox = QMessageBox()
        
        msgBox.setText("ARE YOU SURE? THIS CAN TAKE 5 MINUTES")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setDefaultButton(QMessageBox.No)
        # Apply the dark theme stylesheet
        msgBox.setStyleSheet('''
        QWidget {
            background-color: #2b2b2b;
            color: white;
            selection-background-color: #4a4a4a;
            selection-color: white;
            font-family: Arial;
            font-size: 18px;
        }
        QPushButton {
            font-size: 16pt;
            background-color: #555555;
            color: white;
            border: none;
            padding: 5px 10px 5px 10px;
            border-radius: 5px;
        }

        QPushButton:hover {
            background-color: #4a4a4a;
        }
        ''')

        # Show the QMessageBox and get the user's response
        
        reply = msgBox.exec_()
        if reply == QMessageBox.Yes:
            self.setRH(3, 1, "16bit")

    def confirm_exit(self):
        # Create a QMessageBox
        msgBox = QMessageBox()
        
        msgBox.setText("ARE YOU SURE?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setDefaultButton(QMessageBox.No)

        # Apply the dark theme stylesheet
        msgBox.setStyleSheet('''
        QWidget {
            background-color: #2b2b2b;
            color: white;
            selection-background-color: #4a4a4a;
            selection-color: white;
            font-family: Arial;
            font-size: 18px;
        }
        QPushButton {
            font-size: 16pt;
            background-color: #555555;
            color: white;
            border: none;
            padding: 5px 10px 5px 10px;
            border-radius: 5px;
        }

        QPushButton:hover {
            background-color: #4a4a4a;
        }
        ''')

        # Show the QMessageBox and get the user's response
        
        reply = msgBox.exec_()
        if reply == QMessageBox.Yes:
            QtWidgets.QApplication.instance().quit()

    def switch_to_settings(self):
        self.stacked_widget.setCurrentWidget(self.SettingsPage)

    def switch_to_main(self):
        self.stacked_widget.setCurrentWidget(self.HomePage)

    def on_cell_changed_notopti(self, row, column, num_tab):
        if num_tab==1 :
            item = self.DAQSETTINGS_tableWidget.verticalHeaderItem(row)
            value = self.DAQSETTINGS_tableWidget.item(row, column).text()
            print(f"the value is: {value}")
            try:
                value_int = int(value)
                self.setRH(row+6, value_int, "u16bit")
                print(f"{item.text()} = {value_int} and his adr is {row+6}")
            except ValueError:
                print("ValueError: Cannot convert value to integer")

        elif num_tab==2:
            item = self.FLUIDCALIBRATION_tableWidget.verticalHeaderItem(row)
            value = self.FLUIDCALIBRATION_tableWidget.item(row, column).text()
            print(f"the value is: {value}")
            try:
                value_fl = float(value)
                self.setRH(row*2+15, value_fl, "u16bit")
                print(f"{item.text()} = {value_fl} and his adr is {row*2+15}")
            except ValueError:
                print("ValueError: Cannot convert value to integer")
            
        elif num_tab==3:
            item = self.POURSETTINGS_tableWidget.verticalHeaderItem(row)
            value = self.POURSETTINGS_tableWidget.item(row, column).text()
            print(f"the value is: {value}")
            if row ==0:
                try:
                    value_int = int(value)
                    self.setRH(43, value_int, "u16bit")
                    print(f"{item.text()} = {value_int} and his adr is {43}")
                except ValueError:
                    print("ValueError: Cannot convert value to integer")    

            else:
                try:
                    value_fl = float(value)
                    self.setRH(row*2+42, value_fl, "Float")
                    print(f"{item.text()} = {value_fl} and his adr is {row*2+42}")
                except ValueError:
                    print("ValueError: Cannot convert value to float")
        else :
            print(f"Error when setting value {value}")

    def on_cell_changed(self, row, column, num_tab):
        def handle_value_error(value_type):
            print(f"ValueError: Cannot convert value to {value_type}")
            
        def handle_set_value(item, value, row_offset, value_type):
            try:
                value_parsed = int(value) if value_type == "u16bit" else float(value)
                self.setRH(row_offset, value_parsed, value_type)
                print(f"{item.text()} = {value_parsed} and his adr is {row_offset}")
            except ValueError:
                handle_value_error(value_type)

        if num_tab in (1, 2, 3):
            table_widget = getattr(self, f"{['DAQSETTINGS', 'FLUIDCALIBRATION', 'POURSETTINGS'][num_tab-1]}_tableWidget")
            item = table_widget.verticalHeaderItem(row)
            value = table_widget.item(row, column).text()
            print(f"the value is: {value}")
            
            if num_tab == 1:
                handle_set_value(item, value, row + 6, "u16bit")
            elif num_tab == 2:
                handle_set_value(item, value, row * 2 + 15, "u16bit")
            else:  # num_tab == 3
                value_type = "u16bit" if row == 0 else "Float"
                row_offset = 43 if row == 0 else row * 2 + 42
                handle_set_value(item, value, row_offset, value_type)
        else:
            print(f"Error when setting value {value}")


#main

#ex ki truni l code dir python myscript.py --port /dev/ttyUSB1 --adr 2 --file /path/to/database.csv koun madirhomch yeb9aw bel valeur deafault ta3hom
parser = argparse.ArgumentParser(description="Dynamic GUI")
parser.add_argument('--port', default='/dev/ttyUSB0', help='Serial port')
parser.add_argument('--adr', type=int, default=1, help='Modbus address')
parser.add_argument('--file', default='Database.csv', help='Patch to database cvs file')
args = parser.parse_args()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gui = QtWidgets.QMainWindow()
    ui = Ui_gui()
    ui.setupUi(gui)
    gui.show()

    timer1 = QtCore.QTimer()
    timer1.timeout.connect(ui.update)
    timer1.start(100)

    timer2 = QtCore.QTimer()
    timer2.timeout.connect(ui.updateStatueTable)
    timer2.start(1000)  # Update the table at a smooth rate (1 Hz) each 1s

    sys.exit(app.exec_())