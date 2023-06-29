#!/usr/bin/python
#-*- coding:utf8 -*-

import os

import cv2

ROOT = '/home/kali/D/pictures'
FACES = '/home/kali/D/faces'
TRAIN = '/home/kali/D/training'

# 检查每张图片并确认里面是否有人脸，对于有人脸的图片
# 在人脸周围画一个方框，然后存储为另一张新图片
def detect(srcdir=ROOT, tgtdir=FACES, train_dir=TRAIN):
    for fname in os.listdir(srcdir):
        # 图片可能是“JPG”、“PNG”、“JPEG”等，需要一类一类去验证
        if not fname.upper().endswith('.JPEG'):
            continue
        fullname = os.path.join(srcdir, fname)
        newname = os.path.join(tgtdir,fname)
        # 使用OpenCV的计算视觉库cv2来读取图片
        img = cv2.imread(fullname)
        if img is None:
            continue
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 加载人脸检测器的xml文件配置
        # 下载地址：http://eclecti.cc/files/2008/03/haarcascade_frontalface_alt.xml
        training = os.path.join(train_dir, 'haarcascade_frontalface_alt.xml')
        # 创建cv2的面部检测对象
        cascade = cv2.CascadeClassifier(training)
        rects = cascade.detectMultiScale(gray, 1.3, 5)
        try:
            # 如果包含人脸，就返回一个长方形的坐标，对应图片的人脸区域
            if rects.any():
                print(f'Got a face {fname}')
                # 人脸区域坐标
                rects[:, 2:] += rects[:, :2]
        except AttributeError:
            continue

        for x1, y1, x2, y2 in rects:
            # 在人脸周围画一圈绿色方框
            cv2.rectangle(img,(x1, y1),(x2, y2),(127,256,0),2)
        # 将画了方框的新图片存储到指定目录中
        cv2.imwrite(newname, img)

if __name__ == '__main__':
    detect()
