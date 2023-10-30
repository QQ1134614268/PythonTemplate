# -*- coding:utf-8 -*-
"""
@Time: 2023/6/15
@Description:
"""
import subprocess
from unittest import TestCase

import cv2
import numpy as np


class TestCv2(TestCase):

    def test_run(self):

        cmd = 'ffmpeg -i rtsp://example.com/stream -f image2pipe -pix_fmt bgr24 -vcodec rawvideo -an -'
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

        while True:
            raw_image = p.stdout.read(640 * 480 * 3)
            if len(raw_image) != 640 * 480 * 3:
                break
            image = np.frombuffer(raw_image, dtype='uint8').reshape((480, 640, 3))
            cv2.imshow('frame', image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cv2.destroyAllWindows()
        cv2.CAP_INTELPERC_IMAGE

    def test_run2(self):
        # opencv-python-headless  不能显示图像
        # opencv-python

        img = cv2.imread('ros_book.png')
        cv2.imshow('img', img)  # 以cv.imshow()显示图像

        k = cv2.waitKey(0)
        print(k)  # Esc对应27
