# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 10:51:34 2020

@author: Lenovo_X230
"""

import PySimpleGUI as sg
##----Dictionary FUNCTIONS realize Java Switch-case-------------------------------##
def zero():
    return "zero" 
def one():
    return "one" 
def two(): 
    return "two" 
switcher = { 
    0: zero, 
    1: one, 
    2: two 
    } 
def numbers_to_strings(argument): 
    # Get the function from switcher dictionary 
    func = switcher.get(argument, "nothing") 
    # Execute the function 
    return func()
'''
Input: numbers_to_strings(1) 
Output: One
'''

##----CALCULATOR BMI FUNCTIONS-------------------------------##
def calc_bmi(h, w):
    #-----HELPER FUNCTIONS
    try:
        h, w = float(h), float(w)
        bmi = round(w / h**2, 1)
        if bmi < 18.5:
            standard = '過輕'
        elif 18.5 <= bmi <= 23.9:
            standard = '正常'
        elif 24.0 <= bmi <= 27.9:
            standard = '過重'
        else:
            standard = '肥胖'
    except (ValueError, ZeroDivisionError):
        return None
    else:
        return f'BMI: {bmi}, {standard}'

def main():
    ##-----WINDOW AND LAYOUT---------------------------------##
    sg.theme('Dark Blue 3')  # please make your creations colorful
    layout = [  [sg.Text('身高'), sg.InputText(size=(15,), key='H-IN-')],
                [sg.Text('體重'), sg.InputText(size=(15,), key='W-IN-')],
                [sg.Combo(['BMI計算機', '文字轉語音'], enable_events=True, key='combo', size=(15,1))],
                [sg.Multiline('This is what a Multi-line Text Element looks like', key='-ML-', size=(45,5))],
                [sg.Button('Go', key='submit'), sg.Quit('Cancel', key='Exit')] ]

    window = sg.Window('Get BMI example', layout)
    #-----MAIN EVENT LOOP------------------------------------##
    while True:
        event, values = window.read()
        if event == 'submit':
            bmi = calc_bmi(values['H-IN-'], values['W-IN-'])
            if bmi:
                window.Element('-ML-').Update(bmi)
            else:
                window.Element('-ML-').Update('Something is Error!', text_color='red')
        if event is None or event == sg.WIN_CLOSED or event == 'Exit':
            break
    window.close()

##-----DEFAULT SETTINGS----------------------------------##
if __name__ == '__main__' :
	main()