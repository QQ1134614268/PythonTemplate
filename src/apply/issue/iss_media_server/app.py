# -*- coding:utf-8 -*-
"""
@Time: 2023/6/14
@Description:
"""
import os

import cv2
from flask import Flask, render_template, Response

# ffmpeg 实现暂停,变倍速, 抽帧, 快进快退, 4k 2k 码流

app = Flask(__name__, template_folder=os.path.abspath(os.path.dirname(__file__)))


@app.route('/')
def index():
    return render_template('index1.html')


cap = cv2.VideoCapture(0)


def gen_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, debug=True, threaded=True)
    # server = pywsgi.WSGIServer(('192.168.1.10', 5000), app)
    # server.serve_forever()
    # server = make_server('192.168.1.10', 5000, app)
    # server.serve_forever()
