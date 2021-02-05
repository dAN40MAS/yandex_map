# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(507, 561)
        MainWindow.setMinimumSize(QtCore.QSize(507, 324))
        MainWindow.setMaximumSize(QtCore.QSize(507, 561))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 391, 51))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.coords_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.coords_input.setObjectName("coords_input")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.coords_input)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.scale_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.scale_input.setObjectName("scale_input")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.scale_input)
        self.map_image = QtWidgets.QLabel(self.centralwidget)
        self.map_image.setGeometry(QtCore.QRect(10, 80, 450, 450))
        self.map_image.setText("")
        self.map_image.setObjectName("map_image")
        self.ok_btn = QtWidgets.QPushButton(self.centralwidget)
        self.ok_btn.setGeometry(QtCore.QRect(420, 20, 75, 23))
        self.ok_btn.setObjectName("ok_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Карта"))
        self.label.setText(_translate("MainWindow", "Координаты:"))
        self.label_2.setText(_translate("MainWindow", "Масштаб"))
        self.ok_btn.setText(_translate("MainWindow", "OK"))
