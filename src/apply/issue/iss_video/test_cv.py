import unittest

import cv2


class Test(unittest.TestCase):
    def test1(self):
        # cap = cv2.VideoCapture(0) 打开本机摄像头
        cap = cv2.VideoCapture("test.mp4")
        assert cap.isOpened(), "没有打开"

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))
        print(
            {
                "获取视频宽度": width,
                "获取视频高度": height,
                "获取视频帧率": fps,
                "获取视频编码": fourcc,
            }
        )
        writer = cv2.VideoWriter("out.mp4", fourcc, fps, (width, height))
        while cap.isOpened():
            ret, frame = cap.read()
            cv2.imshow("teswell", frame)
            key = cv2.waitKey(24)
            writer.write(frame)

            if key == ord('q'):
                break
        cap.release()
        cv2.destroyAllWiindows()
