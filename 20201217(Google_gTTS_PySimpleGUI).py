# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 09:11:39 2020

@author: user
"""

# https://pypi.org/project/PySimpleGUI/
import PySimpleGUI as sg
from gtts import gTTS

# Define the window's contents
layout = [[sg.Text("請輸入想要轉換的文字?")],
          [sg.Input(key='-INPUT-')],
          [sg.Text("語言"), sg.Combo(['en', 'zh-TW', 'ja'], key='combo')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window('資料處理科多媒體製作_文字轉語音', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    # ------  gTTS  ------ #
    tts = gTTS(text=values['-INPUT-'], lang=values['combo'])
    tts.save("good.mp3")
    # ------gTTS end------ #
    window['-OUTPUT-'].update('gTTS: ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()