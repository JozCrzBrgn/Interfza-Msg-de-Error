# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Error.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UI_Error(object):
    def setupUi(self, UI_Error):
        UI_Error.setObjectName("UI_Error")
        UI_Error.resize(550, 194)
        UI_Error.setStyleSheet("background-color: rgb(85, 170, 255) /* FONDO:  rgb(35, 57, 91) */\n"
"/*color: rgb(85, 170, 255);*/")
        self.centralwidget = QtWidgets.QWidget(UI_Error)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_icon = QtWidgets.QLabel(self.centralwidget)
        self.lbl_icon.setGeometry(QtCore.QRect(20, 50, 141, 131))
        self.lbl_icon.setText("")
        self.lbl_icon.setPixmap(QtGui.QPixmap("Error.png"))
        self.lbl_icon.setScaledContents(True)
        self.lbl_icon.setObjectName("lbl_icon")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 80, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 551, 31))
        self.frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btn_close = QtWidgets.QPushButton(self.frame)
        self.btn_close.setGeometry(QtCore.QRect(499, 7, 40, 17))
        self.btn_close.setMinimumSize(QtCore.QSize(40, 15))
        self.btn_close.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_close.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    background-color: rgb(255, 0, 0)\n"
"}\n"
"\n"
"QPushButton:hover{    \n"
"    background-color: rgba(255,0,0, 183);\n"
"}")
        self.btn_close.setText("")
        self.btn_close.setObjectName("btn_close")
        UI_Error.setCentralWidget(self.centralwidget)

        self.retranslateUi(UI_Error)
        QtCore.QMetaObject.connectSlotsByName(UI_Error)

    def retranslateUi(self, UI_Error):
        _translate = QtCore.QCoreApplication.translate
        UI_Error.setWindowTitle(_translate("UI_Error", "MainWindow"))
        self.label.setText(_translate("UI_Error", "error"))
