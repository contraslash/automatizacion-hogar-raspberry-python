import sys

# You must add the custom compilation to snowboy in osx
sys.path.append("snowboy/swig/Python3")

import snowboydecoder

def detected_callback():
    print("hotword detected")

# File not included on repo, create your own at https://snowboy.kitt.ai/
detector = snowboydecoder.HotwordDetector("Hola.pmdl",sensitivity=0.5, audio_gain=1)
detector.start(detected_callback)