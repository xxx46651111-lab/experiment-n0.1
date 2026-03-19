import cv2
import numpy as np
import matplotlib.pyplot as plt

# 任务1：读取图片
print("="*50)
print("任务1：读取图片")
# 读取 images 文件夹下的 test.jpg
img = cv2.imread("images/test.jpg")

# 检查图片是否读取成功
if img is None:
    print("错误：无法读取图片，请检查图片路径和文件名")
    exit()
print("图片读取成功！")
print("="*50)