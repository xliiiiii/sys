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


# ====================================
# 保存图片
def Change_Size(picture):
    pic_input = []
    for i in range(0, len(picture)):
        src = cv2.resize(picture[i], (28, 28), interpolation=cv2.INTER_CUBIC)
        src = abs(255 - src)  # 将图片黑白反转
        pic_input.append(src)

    return pic_input
