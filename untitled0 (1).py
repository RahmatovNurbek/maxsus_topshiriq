# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NDYYD5x-iOBCnLa-4VvWAABwndTH8S5H
"""

from google.colab.patches import cv2_imshow
import cv2

picture1=cv2.imread("rasm1.jfif")
picture2=cv2.imread("rasm2.jfif")
picture3=cv2.imread("rasm3.jfif")

cv2_imshow(picture1)
cv2_imshow(picture2)
cv2_imshow(picture3)


color1=cv2.cvtColor(picture1,cv2.COLOR_BGR2GRAY)
cv2_imshow(color1)
color2=cv2.cvtColor(picture2,cv2.COLOR_BGR2GRAY)
cv2_imshow(color2)
color3=cv2.cvtColor(picture3,cv2.COLOR_BGR2GRAY)
cv2_imshow(color3)