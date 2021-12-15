#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:run.py
@time:2021/04/09
"""
from cv2 import cv2
import Character_Segmentation as cs
import Resize_Images as ri
import Load_Trained_Model as ltm

#===================================
#绘制图像
# draw_picture = Draw.Create_Window()
def image_detect(img_path):
    input_picture = cv2.imread(img_path)
    #===================================
    #将图像进行分割为单个
    cut_picture = cs.Vertical_Projection(input_picture)

    #===================================
    #将图片改为28*28像素大小
    seg_pics = ri.Change_Size(cut_picture)
    #===================================
    #加载模型并使用模型进行预测
    output_chars = ltm.Use_Model(seg_pics)
    #===================================
    equation = "".join(list(output_chars))
    try:
        result = eval(equation)
    except:
        result = 000
    equ = equation.replace('/', '÷')
    equ = equ.replace('*', 'x')

    return result, equ, seg_pics

if __name__ == '__main__':
    _,_,imgs = image_detect('pic/124ok.jpg')
    img = cv2.imread('pic/124ok.jpg')
    for i in range(len(imgs)):
        cv2.imshow('img'+str(i), imgs[i])
        cv2.imwrite(str(i)+'.jpg',imgs[i])
    # cv2.waitKey(0)

