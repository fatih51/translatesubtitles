# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/YAZILIM/PythonYazilimlari/altyazicevirici/untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(565, 499)
        MainWindow.setMinimumSize(QtCore.QSize(565, 499))
        MainWindow.setMaximumSize(QtCore.QSize(565, 499))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.FileInputButton = QtWidgets.QPushButton(self.centralwidget)
        self.FileInputButton.setGeometry(QtCore.QRect(410, 90, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.FileInputButton.setFont(font)
        self.FileInputButton.setObjectName("FileInputButton")
        self.FileInput = QtWidgets.QLineEdit(self.centralwidget)
        self.FileInput.setGeometry(QtCore.QRect(100, 90, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.FileInput.setFont(font)
        self.FileInput.setObjectName("FileInput")
        self.mainLang = QtWidgets.QLabel(self.centralwidget)
        self.mainLang.setGeometry(QtCore.QRect(100, 160, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.mainLang.setFont(font)
        self.mainLang.setObjectName("mainLang")
        self.targetLang = QtWidgets.QLabel(self.centralwidget)
        self.targetLang.setGeometry(QtCore.QRect(100, 250, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.targetLang.setFont(font)
        self.targetLang.setObjectName("targetLang")
        self.MainLangInput = QtWidgets.QLineEdit(self.centralwidget)
        self.MainLangInput.setGeometry(QtCore.QRect(100, 200, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MainLangInput.setFont(font)
        self.MainLangInput.setObjectName("MainLangInput")
        self.TargetLangInput = QtWidgets.QLineEdit(self.centralwidget)
        self.TargetLangInput.setGeometry(QtCore.QRect(100, 300, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TargetLangInput.setFont(font)
        self.TargetLangInput.setObjectName("TargetLangInput")
        self.Translate = QtWidgets.QPushButton(self.centralwidget)
        self.Translate.setGeometry(QtCore.QRect(100, 390, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Translate.setFont(font)
        self.Translate.setObjectName("Translate")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Altyazı Çevirici"))
        self.FileInputButton.setText(_translate("MainWindow", "Select File"))
        self.mainLang.setText(_translate("MainWindow", "Ana Dil:"))
        self.targetLang.setText(_translate("MainWindow", "Hedef Dil"))
        self.Translate.setText(_translate("MainWindow", "Çevir"))

