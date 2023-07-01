import unittest
from datetime import datetime, timedelta

import cv2

from apply.issue.iss_video.db import hik_


class Test(unittest.TestCase):
    def test0(self):
        onvif = "rtsp://admin:Nshf@188688@44.39.107.85:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif"
        assert onvif == hik_.onvif
        cap = cv2.VideoCapture(hik_.onvif)
        assert cap.isOpened(), f"没有打开; 地址: {hik_.onvif}"

        end = datetime.now() + timedelta(seconds=30)
        with open(f"opencv_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.mp4", mode='ab') as f:
            while end > datetime.now():
                ret, frame = cap.read()
                f.write(frame)
                # cv2.imwrite(f"opencv_{datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.jpg", frame)
                f.flush()

        cap.release()

    def test_01(self):
        cap = cv2.VideoCapture(
            "rtsp://admin:Nshf@188688@44.39.107.85:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif")
        assert cap.isOpened(), f"没有打开; 地址: {hik_.onvif}"
        end = datetime.now() + timedelta(seconds=30)
        with open(f"opencv_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.mp4", mode='ab') as f:
            while end > datetime.now():
                ret, frame = cap.read()
                f.write(frame)
                f.flush()

            # cv2.imwrite(f"opencv_{datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.jpg", frame)
        cap.release()

    def test1(self):
        cap = cv2.VideoCapture(hik_.onvif)
        assert cap.isOpened(), f"没有打开; 地址: {hik_.onvif}"

    def test3(self):
        cap = cv2.VideoCapture(hik_.net)
        print(f"打开: {cap.isOpened()}")
        while cap.isOpened():
            ret, frame = cap.read()
            cv2.imwrite(f"opencv_{datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.jpg", frame)

    def test2(self):
        cv2.namedWindow("preview")
        vc = cv2.VideoCapture(0)

        if vc.isOpened():
            rval, frame = vc.read()
        else:
            rval = False
        print(rval)
        while rval:
            cv2.imshow("preview", frame)
            rval, frame = vc.read()
            key = cv2.waitKey(20)
            if key == 27:
                break
        vc.release()
        cv2.destroyWindow("preview")

    def test3(self):
        cv2.namedWindow("preview")
        vc = cv2.VideoCapture(0)

        if vc.isOpened():
            rval, frame = vc.read()
        else:
            rval = False
        print(rval)
        while rval:
            cv2.imshow("preview", frame)
            rval, frame = vc.read()
            key = cv2.waitKey(20)
            if key == 27:
                break
        vc.release()
        cv2.destroyWindow("preview")
