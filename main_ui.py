# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(788, 522)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_open_img = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open_img.setGeometry(QtCore.QRect(510, 370, 121, 51))
        self.pushButton_open_img.setObjectName("pushButton_open_img")
        self.pushButton_seg = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_seg.setGeometry(QtCore.QRect(650, 370, 121, 51))
        self.pushButton_seg.setObjectName("pushButton_seg")
        self.pushButton_detect = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_detect.setGeometry(QtCore.QRect(510, 460, 121, 51))
        self.pushButton_detect.setObjectName("pushButton_detect")
        self.pushButton_res = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_res.setGeometry(QtCore.QRect(650, 460, 121, 51))
        self.pushButton_res.setObjectName("pushButton_res")
        self.label_img = QtWidgets.QLabel(self.centralwidget)
        self.label_img.setGeometry(QtCore.QRect(10, 100, 761, 261))
        self.label_img.setText("")
        self.label_img.setObjectName("label_img")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 450, 241, 54))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_res = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_res.setFont(font)
        self.lineEdit_res.setText("")
        self.lineEdit_res.setObjectName("lineEdit_res")
        self.horizontalLayout_2.addWidget(self.lineEdit_res)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 370, 461, 54))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_gs = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_gs.setFont(font)
        self.lineEdit_gs.setText("")
        self.lineEdit_gs.setObjectName("lineEdit_gs")
        self.horizontalLayout.addWidget(self.lineEdit_gs)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 0, 471, 91))
        font = QtGui.QFont()
        font.setFamily("站酷小薇LOGO体")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(270, 460, 121, 38))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_seg = QtWidgets.QLabel(self.centralwidget)
        self.label_seg.setGeometry(QtCore.QRect(390, 440, 91, 81))
        self.label_seg.setText("")
        self.label_seg.setObjectName("label_seg")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "基于的CNN网络的算式识别软件"))
        self.pushButton_open_img.setText(_translate("MainWindow", "打开图片"))
        self.pushButton_seg.setText(_translate("MainWindow", "字符分割"))
        self.pushButton_detect.setText(_translate("MainWindow", "算式识别"))
        self.pushButton_res.setText(_translate("MainWindow", "查看结果"))
        self.label_2.setText(_translate("MainWindow", "结果："))
        self.label.setText(_translate("MainWindow", "公式："))
        self.label_3.setText(_translate("MainWindow", "CNN手写算式识别软件"))
        self.label_4.setText(_translate("MainWindow", "分割图："))
