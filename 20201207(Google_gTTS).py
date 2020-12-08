"""
@ver. 12/07
@-*- coding: utf-8 -*-
@author: Finley
@input: text
@output: sound
"""

#pip install gTTS

from gtts import gTTS
import os

tts = gTTS(text= 'Good morning', lang='en')
tts.save("english.mp3")

tts = gTTS(text= '', lang='zh-TW')
tts.save("chinese.mp3")

tts = gTTS(text= '', lang='ja')
tts.save("japanese.mp3")