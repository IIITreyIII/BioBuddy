# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BioBuddy.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1918, 1024)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.circularProgressBarBase = QtWidgets.QFrame(self.centralwidget)
        self.circularProgressBarBase.setGeometry(QtCore.QRect(240, 80, 321, 321))
        self.circularProgressBarBase.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressBarBase.setObjectName("circularProgressBarBase")
        self.circularProgressTEMP = QtWidgets.QFrame(self.circularProgressBarBase)
        self.circularProgressTEMP.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.circularProgressTEMP.setStyleSheet("QFrame{\n"
"    border-radius: 150px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 rgba(85, 170, 255, 255));\n"
"}")
        self.circularProgressTEMP.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgressTEMP.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressTEMP.setObjectName("circularProgressTEMP")
        self.circularBg = QtWidgets.QFrame(self.circularProgressBarBase)
        self.circularBg.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.circularBg.setStyleSheet("QFrame{\n"
"    border-radius: 150px;\n"
"    background-color: rgba(77, 77, 127, 120);\n"
"}")
        self.circularBg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularBg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularBg.setObjectName("circularBg")
        self.container = QtWidgets.QFrame(self.circularProgressBarBase)
        self.container.setGeometry(QtCore.QRect(25, 25, 270, 270))
        self.container.setStyleSheet("QFrame{\n"
"    border-radius: 135px;\n"
"    background-color: #0A2D44;\n"
"}")
        self.container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container.setObjectName("container")
        self.layoutWidget = QtWidgets.QWidget(self.container)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 50, 191, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelTitle = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(12)
        self.labelTitle.setFont(font)
        self.labelTitle.setStyleSheet("background-color: none;\n"
"color: #FFFFFF")
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.gridLayout.addWidget(self.labelTitle, 0, 0, 1, 1)
        self.labelPercentage = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(20)
        self.labelPercentage.setFont(font)
        self.labelPercentage.setAutoFillBackground(False)
        self.labelPercentage.setStyleSheet("background-color: none;\n"
"color: #FFFFFF")
        self.labelPercentage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPercentage.setObjectName("labelPercentage")
        self.gridLayout.addWidget(self.labelPercentage, 2, 0, 1, 1)
        self.tempPB_MM = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(20)
        self.tempPB_MM.setFont(font)
        self.tempPB_MM.setStyleSheet("color: rgb(255, 255, 255);")
        self.tempPB_MM.setObjectName("tempPB_MM")
        self.gridLayout.addWidget(self.tempPB_MM, 1, 0, 1, 1)
        self.circularBg.raise_()
        self.circularProgressTEMP.raise_()
        self.container.raise_()
        self.circularProgressBarBase_2 = QtWidgets.QFrame(self.centralwidget)
        self.circularProgressBarBase_2.setGeometry(QtCore.QRect(660, 80, 321, 321))
        self.circularProgressBarBase_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgressBarBase_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressBarBase_2.setObjectName("circularProgressBarBase_2")
        self.circularProgressHUMID = QtWidgets.QFrame(self.circularProgressBarBase_2)
        self.circularProgressHUMID.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.circularProgressHUMID.setStyleSheet("QFrame{\n"
"    border-radius: 150px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 rgba(0, 255, 34, 255));\n"
"}")
        self.circularProgressHUMID.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgressHUMID.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressHUMID.setObjectName("circularProgressHUMID")
        self.circularBg_2 = QtWidgets.QFrame(self.circularProgressBarBase_2)
        self.circularBg_2.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.circularBg_2.setStyleSheet("QFrame{\n"
"    border-radius: 150px;\n"
"    background-color: rgba(77, 77, 127, 120);\n"
"}")
        self.circularBg_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularBg_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularBg_2.setObjectName("circularBg_2")
        self.container_2 = QtWidgets.QFrame(self.circularProgressBarBase_2)
        self.container_2.setGeometry(QtCore.QRect(25, 25, 270, 270))
        self.container_2.setStyleSheet("QFrame{\n"
"    border-radius: 135px;\n"
"    background-color: #0A2D44;\n"
"}")
        self.container_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.container_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container_2.setObjectName("container_2")
        self.layoutWidget_2 = QtWidgets.QWidget(self.container_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(40, 50, 191, 191))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelTitle_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(20)
        self.labelTitle_2.setFont(font)
        self.labelTitle_2.setStyleSheet("background-color: none;\n"
"color: #FFFFFF")
        self.labelTitle_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle_2.setObjectName("labelTitle_2")
        self.gridLayout_2.addWidget(self.labelTitle_2, 0, 0, 1, 1)
        self.labelPercentage_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(20)
        self.labelPercentage_2.setFont(font)
        self.labelPercentage_2.setAutoFillBackground(False)
        self.labelPercentage_2.setStyleSheet("background-color: none;\n"
"color: #FFFFFF")
        self.labelPercentage_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPercentage_2.setObjectName("labelPercentage_2")
        self.gridLayout_2.addWidget(self.labelPercentage_2, 2, 0, 1, 1)
        self.HumidPB_MM = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(20)
        self.HumidPB_MM.setFont(font)
        self.HumidPB_MM.setStyleSheet("color: rgb(255, 255, 255);")
        self.HumidPB_MM.setObjectName("HumidPB_MM")
        self.gridLayout_2.addWidget(self.HumidPB_MM, 1, 0, 1, 1)
        self.circularProgressBarBase_3 = QtWidgets.QFrame(self.centralwidget)
        self.circularProgressBarBase_3.setGeometry(QtCore.QRect(1070, 80, 321, 321))
        self.circularProgressBarBase_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgressBarBase_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressBarBase_3.setObjectName("circularProgressBarBase_3")
        self.circularProgressPRES = QtWidgets.QFrame(self.circularProgressBarBase_3)
        self.circularProgressPRES.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.circularProgressPRES.setStyleSheet("QFrame{\n"
"    border-radius: 150px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 rgba(255, 184, 60, 255));\n"
"}")
        self.circularProgressPRES.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgressPRES.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressPRES.setObjectName("circularProgressPRES")
        self.circularBg_3 = QtWidgets.QFrame(self.circularProgressBarBase_3)
        self.circularBg_3.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.circularBg_3.setStyleSheet("QFrame{\n"
"    border-radius: 150px;\n"
"    background-color: rgba(77, 77, 127, 120);\n"
"}")
        self.circularBg_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularBg_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularBg_3.setObjectName("circularBg_3")
        self.container_3 = QtWidgets.QFrame(self.circularProgressBarBase_3)
        self.container_3.setGeometry(QtCore.QRect(25, 25, 270, 270))
        self.container_3.setStyleSheet("QFrame{\n"
"    border-radius: 135px;\n"
"    background-color: #0A2D44;\n"
"}")
        self.container_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.container_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container_3.setObjectName("container_3")
        self.layoutWidget_3 = QtWidgets.QWidget(self.container_3)
        self.layoutWidget_3.setGeometry(QtCore.QRect(40, 50, 191, 191))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.labelTitle_3 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(20)
        self.labelTitle_3.setFont(font)
        self.labelTitle_3.setStyleSheet("background-color: none;\n"
"color: #FFFFFF")
        self.labelTitle_3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle_3.setObjectName("labelTitle_3")
        self.gridLayout_3.addWidget(self.labelTitle_3, 0, 0, 1, 1)
        self.labelPercentage_3 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(20)
        self.labelPercentage_3.setFont(font)
        self.labelPercentage_3.setAutoFillBackground(False)
        self.labelPercentage_3.setStyleSheet("background-color: none;\n"
"color: #FFFFFF")
        self.labelPercentage_3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPercentage_3.setObjectName("labelPercentage_3")
        self.gridLayout_3.addWidget(self.labelPercentage_3, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(150, 590, 761, 331))
        self.frame.setStyleSheet("background-color: rgb(10, 45, 68);\n"
"border: 2px solid rgb(65, 212, 149);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(30, 10, 701, 41))
        self.frame_2.setStyleSheet("border: 2px solid rgb(65, 212, 149);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.MoistureMonitor = QtWidgets.QLabel(self.frame_2)
        self.MoistureMonitor.setGeometry(QtCore.QRect(260, 10, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Quicksand Medium")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.MoistureMonitor.setFont(font)
        self.MoistureMonitor.setStyleSheet("border: none;\n"
"color: rgb(255, 255, 255);")
        self.MoistureMonitor.setScaledContents(False)
        self.MoistureMonitor.setWordWrap(False)
        self.MoistureMonitor.setObjectName("MoistureMonitor")
        self.frameMS1 = QtWidgets.QFrame(self.frame)
        self.frameMS1.setGeometry(QtCore.QRect(30, 60, 161, 221))
        self.frameMS1.setStyleSheet("background-color: rgb(249, 253, 242);\n"
" border: 2px solid rgb(65, 212, 149);")
        self.frameMS1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameMS1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameMS1.setObjectName("frameMS1")
        self.frame_4 = QtWidgets.QFrame(self.frameMS1)
        self.frame_4.setGeometry(QtCore.QRect(9, 9, 141, 41))
        self.frame_4.setAutoFillBackground(False)
        self.frame_4.setStyleSheet("background-color: rgb(249, 253, 242);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setGeometry(QtCore.QRect(40, 10, 68, 22))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(249, 253, 242);\n"
"border: none;")
        self.label.setObjectName("label")
        self.frame_5 = QtWidgets.QFrame(self.frameMS1)
        self.frame_5.setGeometry(QtCore.QRect(19, 69, 121, 111))
        self.frame_5.setStyleSheet("QFrame {\n"
"        background-color: rgb(1, 12, 15);\n"
"        border: 2px solid rgb(65, 212, 149);\n"
"    }")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.sensor1Mstatus = QtWidgets.QLabel(self.frame_5)
        self.sensor1Mstatus.setGeometry(QtCore.QRect(30, 10, 61, 91))
        self.sensor1Mstatus.setStyleSheet("QLabel {\n"
"    border: none;  /* Reset QLabel border */\n"
"    /* Other QLabel-specific styles */\n"
"}")
        self.sensor1Mstatus.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.sensor1Mstatus.setLineWidth(0)
        self.sensor1Mstatus.setText("")
        self.sensor1Mstatus.setPixmap(QtGui.QPixmap("moist.png"))
        self.sensor1Mstatus.setScaledContents(True)
        self.sensor1Mstatus.setObjectName("sensor1Mstatus")
        self.labelSensor1 = QtWidgets.QLabel(self.frameMS1)
        self.labelSensor1.setGeometry(QtCore.QRect(30, 180, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.labelSensor1.setFont(font)
        self.labelSensor1.setStyleSheet("border: none")
        self.labelSensor1.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSensor1.setObjectName("labelSensor1")
        self.frameMS2 = QtWidgets.QFrame(self.frame)
        self.frameMS2.setGeometry(QtCore.QRect(210, 60, 161, 221))
        self.frameMS2.setStyleSheet("background-color: rgb(249, 253, 242);\n"
" border: 2px solid rgb(65, 212, 149);")
        self.frameMS2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameMS2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameMS2.setObjectName("frameMS2")
        self.frame_7 = QtWidgets.QFrame(self.frameMS2)
        self.frame_7.setGeometry(QtCore.QRect(9, 9, 141, 41))
        self.frame_7.setStyleSheet("background-color: rgb(249, 253, 242);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_2 = QtWidgets.QLabel(self.frame_7)
        self.label_2.setGeometry(QtCore.QRect(40, 10, 68, 22))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(249, 253, 242);\n"
"border: none;")
        self.label_2.setObjectName("label_2")
        self.frame_8 = QtWidgets.QFrame(self.frameMS2)
        self.frame_8.setGeometry(QtCore.QRect(20, 69, 120, 111))
        self.frame_8.setStyleSheet("QFrame {\n"
"        background-color: rgb(1, 12, 15);\n"
"        border: 2px solid rgb(65, 212, 149);\n"
"    }")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.sensor2Mstatus = QtWidgets.QLabel(self.frame_8)
        self.sensor2Mstatus.setGeometry(QtCore.QRect(30, 10, 61, 91))
        self.sensor2Mstatus.setAutoFillBackground(False)
        self.sensor2Mstatus.setStyleSheet("QLabel {\n"
"    border: none;  /* Reset QLabel border */\n"
"    /* Other QLabel-specific styles */\n"
"}")
        self.sensor2Mstatus.setText("")
        self.sensor2Mstatus.setPixmap(QtGui.QPixmap("moist.png"))
        self.sensor2Mstatus.setScaledContents(True)
        self.sensor2Mstatus.setObjectName("sensor2Mstatus")
        self.labelSensor2 = QtWidgets.QLabel(self.frameMS2)
        self.labelSensor2.setGeometry(QtCore.QRect(30, 180, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.labelSensor2.setFont(font)
        self.labelSensor2.setStyleSheet("border:none")
        self.labelSensor2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSensor2.setObjectName("labelSensor2")
        self.frameMS3 = QtWidgets.QFrame(self.frame)
        self.frameMS3.setGeometry(QtCore.QRect(390, 60, 161, 221))
        self.frameMS3.setStyleSheet("background-color: rgb(249, 253, 242);\n"
" border: 2px solid rgb(65, 212, 149);")
        self.frameMS3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameMS3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameMS3.setObjectName("frameMS3")
        self.frame_10 = QtWidgets.QFrame(self.frameMS3)
        self.frame_10.setGeometry(QtCore.QRect(9, 9, 141, 41))
        self.frame_10.setStyleSheet("background-color: rgb(249, 253, 242);")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.label_3 = QtWidgets.QLabel(self.frame_10)
        self.label_3.setGeometry(QtCore.QRect(40, 10, 68, 22))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(249, 253, 242);\n"
"border: none;")
        self.label_3.setObjectName("label_3")
        self.frame_11 = QtWidgets.QFrame(self.frameMS3)
        self.frame_11.setGeometry(QtCore.QRect(20, 69, 120, 111))
        self.frame_11.setStyleSheet("QFrame {\n"
"        background-color: rgb(1, 12, 15);\n"
"        border: 2px solid rgb(65, 212, 149);\n"
"    }")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.sensor3Mstatus = QtWidgets.QLabel(self.frame_11)
        self.sensor3Mstatus.setGeometry(QtCore.QRect(30, 10, 61, 91))
        self.sensor3Mstatus.setStyleSheet("QLabel {\n"
"    border: none;  /* Reset QLabel border */\n"
"    /* Other QLabel-specific styles */\n"
"}")
        self.sensor3Mstatus.setText("")
        self.sensor3Mstatus.setPixmap(QtGui.QPixmap("moist.png"))
        self.sensor3Mstatus.setScaledContents(True)
        self.sensor3Mstatus.setObjectName("sensor3Mstatus")
        self.labelSensor3 = QtWidgets.QLabel(self.frameMS3)
        self.labelSensor3.setGeometry(QtCore.QRect(30, 180, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.labelSensor3.setFont(font)
        self.labelSensor3.setStyleSheet("border:none")
        self.labelSensor3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSensor3.setObjectName("labelSensor3")
        self.frameMS4 = QtWidgets.QFrame(self.frame)
        self.frameMS4.setGeometry(QtCore.QRect(570, 60, 161, 221))
        self.frameMS4.setStyleSheet("background-color: rgb(249, 253, 242);\n"
" border: 2px solid rgb(65, 212, 149);")
        self.frameMS4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameMS4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameMS4.setObjectName("frameMS4")
        self.frame_13 = QtWidgets.QFrame(self.frameMS4)
        self.frame_13.setGeometry(QtCore.QRect(9, 9, 141, 41))
        self.frame_13.setStyleSheet("background-color: rgb(249, 253, 242);")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.label_4 = QtWidgets.QLabel(self.frame_13)
        self.label_4.setGeometry(QtCore.QRect(40, 10, 68, 22))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(249, 253, 242);\n"
"border: none;")
        self.label_4.setObjectName("label_4")
        self.frame_18 = QtWidgets.QFrame(self.frameMS4)
        self.frame_18.setGeometry(QtCore.QRect(20, 69, 120, 111))
        self.frame_18.setStyleSheet("QFrame {\n"
"        background-color: rgb(1, 12, 15);\n"
"        border: 2px solid rgb(65, 212, 149);\n"
"    }")
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.sensor4Mstatus = QtWidgets.QLabel(self.frame_18)
        self.sensor4Mstatus.setGeometry(QtCore.QRect(30, 10, 61, 91))
        self.sensor4Mstatus.setStyleSheet("QLabel {\n"
"    border: none;  /* Reset QLabel border */\n"
"    /* Other QLabel-specific styles */\n"
"}")
        self.sensor4Mstatus.setText("")
        self.sensor4Mstatus.setPixmap(QtGui.QPixmap("moist.png"))
        self.sensor4Mstatus.setScaledContents(True)
        self.sensor4Mstatus.setObjectName("sensor4Mstatus")
        self.labelSensor4 = QtWidgets.QLabel(self.frameMS4)
        self.labelSensor4.setGeometry(QtCore.QRect(30, 180, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.labelSensor4.setFont(font)
        self.labelSensor4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelSensor4.setStyleSheet("border:none")
        self.labelSensor4.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSensor4.setObjectName("labelSensor4")
        self.comboBoxSensor1 = QtWidgets.QComboBox(self.frame)
        self.comboBoxSensor1.setGeometry(QtCore.QRect(50, 290, 121, 32))
        self.comboBoxSensor1.setStyleSheet("color: rgb(10, 45, 68);  /* BLUE*/\n"
"background-color: rgb(249, 253, 242);")
        self.comboBoxSensor1.setObjectName("comboBoxSensor1")
        self.comboBoxSensor2 = QtWidgets.QComboBox(self.frame)
        self.comboBoxSensor2.setGeometry(QtCore.QRect(230, 290, 121, 32))
        self.comboBoxSensor2.setStyleSheet("color: rgb(10, 45, 68);  /* BLUE*/\n"
"background-color: rgb(249, 253, 242);")
        self.comboBoxSensor2.setObjectName("comboBoxSensor2")
        self.comboBoxSensor3 = QtWidgets.QComboBox(self.frame)
        self.comboBoxSensor3.setGeometry(QtCore.QRect(410, 290, 121, 32))
        self.comboBoxSensor3.setStyleSheet("color: rgb(10, 45, 68);  /* BLUE*/\n"
"background-color: rgb(249, 253, 242);")
        self.comboBoxSensor3.setObjectName("comboBoxSensor3")
        self.comboBoxSensor4 = QtWidgets.QComboBox(self.frame)
        self.comboBoxSensor4.setGeometry(QtCore.QRect(590, 290, 121, 32))
        self.comboBoxSensor4.setStyleSheet("color: rgb(10, 45, 68);  /* BLUE*/\n"
"background-color: rgb(249, 253, 242);")
        self.comboBoxSensor4.setObjectName("comboBoxSensor4")
        self.frame_14 = QtWidgets.QFrame(self.centralwidget)
        self.frame_14.setGeometry(QtCore.QRect(0, 0, 151, 971))
        self.frame_14.setStyleSheet("background-color: rgb(249, 253, 242);")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.label_5 = QtWidgets.QLabel(self.frame_14)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 131, 141))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("biobuddy.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.layoutWidget1 = QtWidgets.QWidget(self.frame_14)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 200, 121, 352))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(35)
        self.verticalLayout.setObjectName("verticalLayout")
        self.buttonPansy = QtWidgets.QPushButton(self.layoutWidget1)
        self.buttonPansy.setMouseTracking(False)
        self.buttonPansy.setStyleSheet("QPushButton {\n"
"    border: 2px solid #0A2D44; /* Set border thickness and color */\n"
"    border-radius: 5px; /* Set border radius for rounded corners */\n"
"    padding: 8px 16px; /* Set padding for the button text */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #41D495; /* Change background color on hover */\n"
"    color: rgb(65, 212, 149); /* Change text color on hover */\n"
"}")
        self.buttonPansy.setCheckable(False)
        self.buttonPansy.setObjectName("buttonPansy")
        self.verticalLayout.addWidget(self.buttonPansy)
        self.buttonFern = QtWidgets.QPushButton(self.layoutWidget1)
        self.buttonFern.setStyleSheet("QPushButton {\n"
"    border: 2px solid #0A2D44; /* Set border thickness and color */\n"
"    border-radius: 5px; /* Set border radius for rounded corners */\n"
"    padding: 8px 16px; /* Set padding for the button text */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #41D495; /* Change background color on hover */\n"
"    color: rgb(65, 212, 149); /* Change text color on hover */\n"
"}")
        self.buttonFern.setObjectName("buttonFern")
        self.verticalLayout.addWidget(self.buttonFern)
        self.buttonPeaceLily = QtWidgets.QPushButton(self.layoutWidget1)
        self.buttonPeaceLily.setStyleSheet("QPushButton {\n"
"    border: 2px solid #0A2D44; /* Set border thickness and color */\n"
"    border-radius: 5px; /* Set border radius for rounded corners */\n"
"    padding: 8px 16px; /* Set padding for the button text */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #41D495; /* Change background color on hover */\n"
"    color: rgb(65, 212, 149); /* Change text color on hover */\n"
"}")
        self.buttonPeaceLily.setObjectName("buttonPeaceLily")
        self.verticalLayout.addWidget(self.buttonPeaceLily)
        self.buttonPothos = QtWidgets.QPushButton(self.layoutWidget1)
        self.buttonPothos.setStyleSheet("QPushButton {\n"
"    border: 2px solid #0A2D44; /* Set border thickness and color */\n"
"    border-radius: 5px; /* Set border radius for rounded corners */\n"
"    padding: 8px 16px; /* Set padding for the button text */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #41D495; /* Change background color on hover */\n"
"    color: rgb(65, 212, 149); /* Change text color on hover */\n"
"}")
        self.buttonPothos.setObjectName("buttonPothos")
        self.verticalLayout.addWidget(self.buttonPothos)
        self.frame_15 = QtWidgets.QFrame(self.centralwidget)
        self.frame_15.setGeometry(QtCore.QRect(149, -1, 1771, 61))
        self.frame_15.setStyleSheet("background-color: #0A2D44")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.frame_16 = QtWidgets.QFrame(self.centralwidget)
        self.frame_16.setGeometry(QtCore.QRect(150, 920, 1771, 121))
        self.frame_16.setStyleSheet("background-color: #0A2D44")
        self.frame_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.frame_3 = QtWidgets.QFrame(self.frame_16)
        self.frame_3.setGeometry(QtCore.QRect(970, 10, 711, 40))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(249, 253, 242);")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(249, 253, 242);")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(249, 253, 242);")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.frame_17 = QtWidgets.QFrame(self.centralwidget)
        self.frame_17.setGeometry(QtCore.QRect(1540, 50, 391, 871))
        self.frame_17.setStyleSheet("background-color: #0A2D44")
        self.frame_17.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_17.setObjectName("frame_17")
        self.labelDescription = QtWidgets.QLabel(self.frame_17)
        self.labelDescription.setGeometry(QtCore.QRect(30, 410, 321, 401))
        font = QtGui.QFont()
        font.setFamily("Quicksand Medium")
        self.labelDescription.setFont(font)
        self.labelDescription.setStyleSheet("border: 3px solid rgb(65, 212, 149);\n"
"color: rgb(255, 255, 255);\n"
"line-height: 150%;")
        self.labelDescription.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labelDescription.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.labelDescription.setLineWidth(1)
        self.labelDescription.setScaledContents(False)
        self.labelDescription.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelDescription.setWordWrap(True)
        self.labelDescription.setIndent(2)
        self.labelDescription.setObjectName("labelDescription")
        self.labelImage = QtWidgets.QLabel(self.frame_17)
        self.labelImage.setGeometry(QtCore.QRect(30, 40, 321, 241))
        self.labelImage.setFocusPolicy(QtCore.Qt.TabFocus)
        self.labelImage.setStyleSheet("border: 2px solid rgb(65, 212, 149);")
        self.labelImage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labelImage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.labelImage.setLineWidth(3)
        self.labelImage.setText("")
        self.labelImage.setPixmap(QtGui.QPixmap("../../.designer/backup/PeaceLily.jpg"))
        self.labelImage.setScaledContents(True)
        self.labelImage.setObjectName("labelImage")
        self.plantname_label = QtWidgets.QLabel(self.frame_17)
        self.plantname_label.setGeometry(QtCore.QRect(60, 320, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(24)
        self.plantname_label.setFont(font)
        self.plantname_label.setStyleSheet("color: rgb(65, 212, 149);")
        self.plantname_label.setAlignment(QtCore.Qt.AlignCenter)
        self.plantname_label.setObjectName("plantname_label")
        self.calframe = QtWidgets.QFrame(self.centralwidget)
        self.calframe.setGeometry(QtCore.QRect(910, 590, 631, 331))
        self.calframe.setStyleSheet("border: 2px solid rgb(65, 212, 149);\n"
"background-color: rgb(10, 45, 68);")
        self.calframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.calframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.calframe.setObjectName("calframe")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.calframe)
        self.calendarWidget.setGeometry(QtCore.QRect(1, 0, 391, 331))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(12)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setAutoFillBackground(False)
        self.calendarWidget.setStyleSheet("QCalendarWidget QWidget {\n"
"    background-color: rgb(249, 253, 242); /* White background for the calendar */\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"    color: white; /* Blue text for buttons */\n"
"    background-color: rgb(10, 45, 68);\n"
"    font-weight: bold; /* Make button text bold */\n"
"    border-radius: 5px; /* Rounded corners for buttons */\n"
"    width: 100px; /* Adjust button width as needed */\n"
"    height: 30px; /* Adjust button height as needed */\n"
"    padding: 5px; /* Padding around the button content */\n"
"}\n"
"\n"
"QCalendarWidget QToolButton:hover {\n"
"    background-color: #f3f3f3; /* Light grey background on hover */\n"
"}\n"
"\n"
"QCalendarWidget QMenu {\n"
"    width: 150px; /* Width of dropdown menus */\n"
"    left: 20px; /* Position from the left */\n"
"    color: rgb(10, 45, 68); /* Blue text for menu items */\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox {\n"
"    color: white; /* White text for spin boxes */\n"
"    background-color: #0a2d44; /* Blue background for spin boxes */\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled {\n"
"    font-size: 16px; /* Font size for date numbers */\n"
"    color: #41d495; /* Green text for dates */\n"
"    background-color: white; /* White background for the date grid */\n"
"    selection-background-color: #41d495; /* Green background for selected date */\n"
"    selection-color: white; /* White text for selected date */\n"
"}\n"
"\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"    border: none; /* Remove border from navigation bar */\n"
"    background-color: rgb(10, 45, 68); /* Blue background for navigation bar */\n"
"    padding: 5px; /* Padding inside navigation bar */\n"
"    border-radius: 10px; /* Rounded corners for navigation bar */\n"
"}\n"
"\n"
"QCalendarWidget QHeaderView {\n"
"    background-color: #0a2d44; /* Blue background for header view */\n"
"    color: white; /* White text for header view */\n"
"}\n"
"        \"\"\"\n"
"")
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.notesTextEdit = QtWidgets.QTextEdit(self.calframe)
        self.notesTextEdit.setGeometry(QtCore.QRect(403, 40, 211, 251))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.notesTextEdit.setFont(font)
        self.notesTextEdit.setStyleSheet("background-color: rgb(249, 253, 242);\n"
"color: rgb(1, 12, 15);")
        self.notesTextEdit.setOverwriteMode(False)
        self.notesTextEdit.setObjectName("notesTextEdit")
        self.saveNotesButton = QtWidgets.QPushButton(self.calframe)
        self.saveNotesButton.setGeometry(QtCore.QRect(520, 300, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.saveNotesButton.setFont(font)
        self.saveNotesButton.setStyleSheet("color: rgb(249, 253, 242);\n"
"    border-radius: 5px; ")
        self.saveNotesButton.setObjectName("saveNotesButton")
        self.selectedDateLabel = QtWidgets.QLabel(self.calframe)
        self.selectedDateLabel.setGeometry(QtCore.QRect(407, 10, 201, 22))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(12)
        self.selectedDateLabel.setFont(font)
        self.selectedDateLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.selectedDateLabel.setObjectName("selectedDateLabel")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(150, 50, 1391, 541))
        self.label_8.setStyleSheet("background-color: rgb(169, 236, 202);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_8.raise_()
        self.frame.raise_()
        self.circularProgressBarBase.raise_()
        self.circularProgressBarBase_2.raise_()
        self.circularProgressBarBase_3.raise_()
        self.frame_14.raise_()
        self.frame_15.raise_()
        self.frame_16.raise_()
        self.frame_17.raise_()
        self.calframe.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1918, 28))
        self.menubar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        self.Plants = QtWidgets.QMenu(self.menubar)
        self.Plants.setObjectName("Plants")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionPansy = QtWidgets.QAction(MainWindow)
        self.actionPansy.setObjectName("actionPansy")
        self.actionFern = QtWidgets.QAction(MainWindow)
        self.actionFern.setObjectName("actionFern")
        self.actionPeaceLily = QtWidgets.QAction(MainWindow)
        self.actionPeaceLily.setObjectName("actionPeaceLily")
        self.actionPothos = QtWidgets.QAction(MainWindow)
        self.actionPothos.setObjectName("actionPothos")
        self.Plants.addAction(self.actionPansy)
        self.Plants.addAction(self.actionFern)
        self.Plants.addAction(self.actionPeaceLily)
        self.Plants.addAction(self.actionPothos)
        self.menubar.addAction(self.Plants.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelTitle.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Temperature</span></p></body></html>"))
        self.labelPercentage.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">00.00</span></p></body></html>"))
        self.tempPB_MM.setText(_translate("MainWindow", "   MIN - MAX"))
        self.labelTitle_2.setText(_translate("MainWindow", "<html><head/><body><p>Humidity</p></body></html>"))
        self.labelPercentage_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">00.00</span></p></body></html>"))
        self.HumidPB_MM.setText(_translate("MainWindow", "   MIN - MAX"))
        self.labelTitle_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Pressure</span></p></body></html>"))
        self.labelPercentage_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">00.00</span></p></body></html>"))
        self.MoistureMonitor.setText(_translate("MainWindow", "Moisture Monitor"))
        self.label.setText(_translate("MainWindow", "Sensor 1"))
        self.labelSensor1.setText(_translate("MainWindow", "plant name"))
        self.label_2.setText(_translate("MainWindow", "Sensor 2"))
        self.labelSensor2.setText(_translate("MainWindow", "plant name"))
        self.label_3.setText(_translate("MainWindow", "Sensor 3"))
        self.labelSensor3.setText(_translate("MainWindow", "plant name"))
        self.label_4.setText(_translate("MainWindow", "Sensor 4"))
        self.labelSensor4.setText(_translate("MainWindow", "plant name"))
        self.buttonPansy.setText(_translate("MainWindow", "Pansy"))
        self.buttonFern.setText(_translate("MainWindow", "Fern"))
        self.buttonPeaceLily.setText(_translate("MainWindow", "PeaceLily"))
        self.buttonPothos.setText(_translate("MainWindow", "Pothos"))
        self.label_9.setText(_translate("MainWindow", "Created with: PyQT5 and Python           "))
        self.label_7.setText(_translate("MainWindow", "     Version: 1.02"))
        self.label_6.setText(_translate("MainWindow", "Built By: Trey Ball"))
        self.labelDescription.setText(_translate("MainWindow", "Plant Description"))
        self.plantname_label.setText(_translate("MainWindow", "PLANT NAME"))
        self.notesTextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Quicksand\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'PibotoLt\';\">notes for input yayayyayayayayayyaya testststtstststtststst ssttststts t s st stststss</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'PibotoLt\';\"><br /></p></body></html>"))
        self.saveNotesButton.setText(_translate("MainWindow", "Save Notes"))
        self.selectedDateLabel.setText(_translate("MainWindow", "Selected Date:"))
        self.Plants.setTitle(_translate("MainWindow", "Plants"))
        self.actionPansy.setText(_translate("MainWindow", "Pansy"))
        self.actionFern.setText(_translate("MainWindow", "Fern"))
        self.actionPeaceLily.setText(_translate("MainWindow", "PeaceLily"))
        self.actionPothos.setText(_translate("MainWindow", "Pothos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

