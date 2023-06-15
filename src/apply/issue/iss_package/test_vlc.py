# -*- coding:utf-8 -*-
"""
@Time: 2023/6/15
@Description:
"""
from unittest import TestCase

import vlc


# pip install python-vlc


class TestVlc(TestCase):

    def test_run(self):
        player = vlc.MediaPlayer('rtsp://example.com/media.mp4')
        player.play()
