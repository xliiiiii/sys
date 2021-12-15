#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:run.py
@time:2021/04/08
"""

import os
from cv2 import cv2
import numpy as np
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
os.environ['CUDA_VISIBLE_DEVICES'] = '/gpu:0'


# 加载模型并对图片进行识别
model = tf.keras.models.load_model('trained_model/Model.h5')  # 加载模型

pic_lab = ['(', ')', '0', '1', '2', '3', '4', '5', '6',
           '7', '8', '9', '/', '*', '+', '-']  # 模型输出对应的标签


def Use_Model(pic_input):
    output_lab = []  # 识别的标签
    for i in range(0, len(pic_input)):
        src = tf.reshape(pic_input[i], [1, 28, 28, 1])
        src = tf.cast(src, dtype=tf.float32) / 255.
        res = np.argmax(model.predict(src))
        output_lab.append(pic_lab[res])

    # print(output_lab)
    return output_lab
