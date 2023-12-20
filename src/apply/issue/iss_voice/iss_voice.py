import sys
from io import BytesIO
from unittest import TestCase

import pyttsx4


# gtts 需要科学上网
# pyttsx4
# pywin32
# speech

class TestSqlLite(TestCase):
    engine = pyttsx4.init()

    def test_run(self):
        engine = self.engine
        engine.say('this is an english text to voice test.')
        engine.runAndWait()

        self.engine.save_to_file('i am Hello World, i am a programmer. i think life is short.', 'test1.wav')
        self.engine.runAndWait()

    def test_run2(self):
        from pydub import AudioSegment
        from pydub.playback import play

        engine = pyttsx4.init()
        b = BytesIO()
        engine.save_to_file('i am Hello World', b)
        engine.runAndWait()
        # the bs is raw data of the audio.
        bs = b.getvalue()
        # add an wav file format header
        d = b'WAVEfmt\x20\x12\x00\x00\x00\x01\x00\x01\x00\x22\x56\x00\x00\x44\xac\x00\x00\x02\x00\x10\x00\x00\x00data'
        b = bytes(b'RIFF') + (len(bs) + 38).to_bytes(4, byteorder='little') + d + (len(bs)).to_bytes(4,
                                                                                                     byteorder='little') + bs
        # changed to BytesIO
        b = BytesIO(b)
        audio = AudioSegment.from_file(b, format="wav")
        play(audio)
        sys.exit(0)

    def test_run3(self):  # cloning voice
        engine = pyttsx4.init('coqui_ai_tts')
        engine.setProperty('speaker_wav', './docs/i_have_a_dream_10s.wav')

        engine.say('this is an english text to voice test, listen it carefully and tell who i am.')
        engine.runAndWait()

    def test_run3(self):
        engine = pyttsx4.init('coqui_ai_tts')
        engine.setProperty('speaker_wav', './someones_voice.wav')

        engine.say('this is an english text to voice test.')
        engine.runAndWait()
