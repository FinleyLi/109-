# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 16:23:22 2020

@author: Lenovo_X230
"""
'''
# 作業二.1 P.91計算匯率
# 輸入舊匯率
Old_Rate = int(input("請輸入舊匯率 = "))
#Old_Rate = 31.4

# 輸入新匯率
New_Rate = int(input("請輸入新匯率 = "))

# 計算匯率變動幅度並列印
Change = ( (Old_Rate - New_Rate) / New_Rate) * 100
print(Change)

# 判斷匯率變動為升值或貶值
if Change > 0 :
    Result = "升值"
else :
    Result = "貶值"
print("貨幣升貶值幅度 = % 4.2f%s 表示 %s" % (Change, "%", Result))
'''
import PySimpleGUI as sg


##----Rate Change FUNCTIONS-------------------------------##
def exchange_rate(Old_Rate, New_Rate):
    Old_Rate, New_Rate = float(Old_Rate), float(New_Rate)
    # 計算匯率變動幅度並列印
    Change = round(( (Old_Rate - New_Rate) / New_Rate) * 100, 2)
    
    # 判斷匯率變動為升值或貶值
    if Change > 0 :
        Result = "升值"
    else :
        Result = "貶值"
    return f'貨幣升貶值幅度 {Change}%, 表示{Result}'

def main():
    ##-----WINDOW AND LAYOUT---------------------------------##
    sg.theme('Dark Blue 3')  # please make your creations colorful
    layout = [  [sg.Text('請輸入舊匯率'), sg.InputText(size=(15,), key='o-IN-')],
                [sg.Text('請輸入新匯率'), sg.InputText(size=(15,), key='n-IN-')],
                [sg.Multiline('This is what a Multi-line Text Element looks like', key='-ML-', size=(45,5))],
                [sg.Button('Go', key='submit'), sg.Quit('Cancel', key='Exit')] ]

    window = sg.Window('Get Rate example', layout)
    #-----MAIN EVENT LOOP------------------------------------##
    while True:
        event, values = window.read()
        if event == 'submit':
            rate = exchange_rate(values['o-IN-'], values['n-IN-'])
            if rate:
                window.Element('-ML-').Update(rate)
            else:
                window.Element('-ML-').Update('Something is Error!', text_color='red')
        if event is None or event == sg.WIN_CLOSED or event == 'Exit':
            break
    window.close()

##-----DEFAULT SETTINGS----------------------------------##
if __name__ == '__main__' :
	main()
