#!/usr/bin/env python
# coding: utf-8

# 日期: 2020. 11. 03
# 課程: 程式語言與設計

# """
# 09/11
# """

# In[2]:


# 四則運算
pv = 10000*(1+0.03)
print(pv/0.03)


# In[4]:


# 記憶體位置
id(pv)


# In[5]:


# 字串相加
str1 = 'Just'
str2 = 'in'
str3 = str1 + str2
print(str3)


# """
# 09/15
# """

# In[7]:


# BMI身體質量指數
# 體重
Wight = 72
# 身高
#Hight = 174.5
print('請輸入身高')
Hight = int(input())

# 計算BMI
x = Hight/100
BMI = Wight/(x*x)

#print(BMI)
type(BMI)


# In[8]:


# 排序
a = [50, 20, 60, 40, 30]
print('a: ', a)
a.sort()
print('排序後的結果 a: ', a)


# """
# 09/26
# 10/09
# """

# In[11]:


# 作業一.1 判斷 3和5的倍數

Num = int(input())# 3, 5最小公倍數
if (Num%15 == 0 ):
    print('Num同時為3和5的倍數')
else :
    print('Num不是我們要找的數')


# In[13]:


# 作業一.2 輸入兩數，輸出兩數的乘積

Num121 = int(input('輸入數字(1): '))
Num122 = int(input('輸入數字(2): '))

#計算乘積並輸出
Ans12 = Num121*Num122
print('兩數乘積: ', Ans12)


# """
# 10/14
# 10/16
# 不同進位間的轉換
# 迴圈介紹
# """

# """
# 10/23
# """

# In[14]:


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


# In[16]:


# ver. 10/30
# 視窗輸入數值資料
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 09:02:01 2020

@author: user
"""
get_ipython().system('pip install PySimpleGUI')
import PySimpleGUI as sg                        # Part 1 - The import

# Define the window's contents
layout = [  [sg.Text("What's your name?")],     # Part 2 - The Layout
            [sg.Input()],
            [sg.Button('Ok')] ]

# Create the window
window = sg.Window('Window Title', layout)      # Part 3 - Window Defintion

# Display and interact with the Window
event, values = window.read()                   # Part 4 - Event loop or Window.read call

# Do something with the information gathered
print('Hello', values[0], "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()                                  # Part 5 - Close the Window


# In[17]:


# 作業二.2 網路爬蟲
# 1.全球即時匯率API
"""import requests
import pandas as pd

r=requests.get('https://tw.rter.info/capi.php')"""
# 全球即時匯率API
import requests
import pandas as pd

r=requests.get('https://tw.rter.info/capi.php')
#r
currency=r.json()
#currency

pd = pd.DataFrame(currency)
pd


# In[19]:


# 篩選美金對台幣匯率
pd['USDTWD']


# In[23]:


#抓取台灣銀行牌告匯率
"""import pandas as pd
from datetime import datetime

#source
url="http://rate.bot.com.tw/xrt?Lang=zh-TW"

#讀取網頁
dfs=pd.read_html(url)"""
import pandas as pd
from datetime import datetime

#source
url="http://rate.bot.com.tw/xrt?Lang=zh-TW"

#讀取網頁
dfs = pd.read_html(url)
dfs


# In[25]:


currency = dfs[0]
currency.iloc[:,0:5]


# """
# 追加request商家評論爬蟲
# """

# In[1]:


"""
Python 爬取Google map最新商家資訊評論!- 實作"動態網頁"爬蟲
"""

#引入函式庫
import requests 
import json

# 超連結
url = 'https://www.google.com.tw/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765758354820525099!2y10702812502251526020!2m2!1i8!2i10!3e1!4m5!3b1!4b1!5b1!6b1!7b1!5m2!1sZ8efX5C2J4z_0gTnxJOICQ!7e81'
# 發送get請求
text = requests.get(url).text
# 取代掉特殊字元，這個字元是為了資訊安全而設定的喔。
pretext = ')]}\''
text = text.replace(pretext,'')
# 把字串讀取成json
soup = json.loads(text)

# 取出包含留言的List 。
conlist = soup[2]

# 逐筆抓出
for i in conlist:
    print("username:"+str(i[0][1]))
    print("time:"+str(i[1]))
    print("comment:"+str(i[3]))


# In[ ]:




