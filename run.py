#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:run.py
@time:2021/04/09
"""
import os
import sys
import time

import cv2
import qdarkstyle
from PyQt5.QtGui import QIcon

import Detect_Main
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox
from PyQt5.QtWidgets import QMainWindow
from main_ui import Ui_MainWindow  # 加载我们的布局


class MymainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MymainWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)  # 初始化ui
        self.btn_connect()
        self.setWindowIcon(QIcon('src/icon.png'))
        self.pushButton_seg.setDisabled(True)
        self.pushButton_res.setDisabled(True)
        self.pushButton_detect.setDisabled(True)

        self.label_seg.setScaledContents(True)
        self.label_img.setScaledContents(True)

    def btn_connect(self):
        self.pushButton_open_img.clicked.connect(self.open_image)
        self.pushButton_detect.clicked.connect(self.detect_number)
        self.pushButton_res.clicked.connect(self.show_result)
        self.pushButton_seg.clicked.connect(self.show_seg)

    def __init_ui(self):
        self.label_seg.clear()
        self.lineEdit_gs.clear()
        self.lineEdit_res.clear()

    def open_image(self):
        path = 'segs'
        self.pushButton_seg.setDisabled(False)
        self.__init_ui()
        for i in os.listdir(path):
            path_file = os.path.join(path, i)
            if os.path.isfile(path_file):
                os.remove(path_file)
        self.pic_path, _ = QFileDialog.getOpenFileName(self, '选择图片', r'C', 'Image files(*.jpg *.gif *.png)')
        print(self.pic_path)
        self.label_img.setPixmap(QtGui.QPixmap(self.pic_path))

    def detect_number(self):

        try:
            int(self.equ[0])
        except:
            if self.equ[0] != '(':
                self.equ = self.equ[1:]

        self.lineEdit_gs.setText(self.equ)

    def show_seg(self):
        self.pushButton_res.setDisabled(False)
        self.pushButton_detect.setDisabled(False)
        self.calculator_res, self.equ, self.seg_images = Detect_Main.image_detect(self.pic_path)
        # print(self.calculator_res, self.equ)
        for i in range(len(self.seg_images)):
            time.sleep(0.5)
            # cv2.imshow('segs/img' + str(i), self.seg_images[i])
            cv2.imwrite('segs/' +str(i) + '.jpg', self.seg_images[i])
            # show2 = self.seg_images[i]
            jpg = QtGui.QPixmap('segs/' +str(i) + '.jpg')
            self.label_seg.setPixmap(jpg)
            self.repaint()
        QMessageBox.warning(self, '提示', '分割已完成！', QMessageBox.Ok)


    def show_result(self):
        self.lineEdit_res.setText(str(self.calculator_res))


if __name__ == '__main__':  # 程序的入口
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    win = MymainWindow()
    win.show()
    sys.exit(app.exec_())
