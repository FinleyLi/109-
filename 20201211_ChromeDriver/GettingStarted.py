# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#pip install selenium

import time
import random # 隨機數
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 隨機數
def dice():
	return random.randint(1, 120) # 至多延遲120秒

# 開啟校務系統差勤
Browser = webdriver.Chrome()
LoginUrl= ('https://softwork.tsh.tp.edu.tw/t-tools/index.php')
UserName= ('hk3345678')
UserPass= ('ilikemoney')
time.sleep(dice()) # 設定等待登入時間每日皆不同

# 登入差勤打卡簽到
Browser.get(LoginUrl)
Browser.find_element_by_id('teacher_log').send_keys(UserName)
Browser.find_element_by_id('teacher_pw').send_keys(UserPass)
Browser.find_element_by_id('teacher_pw').send_keys(Keys.ENTER)
time.sleep(5) # Let the user actually see something!
'''
# 校務系統使用jQuery Mobile無按鈕可選
btn = Browser.find_element_by_name("Submit")
btn.click()
'''
# 進入"簽到退(專任)"
dailycheckURL = ('https://softwork.tsh.tp.edu.tw/t-tools/dailycheck.php')
Browser.get(dailycheckURL)
Browser.save_screenshot('dailycheck.png')

# 簽退
dailycheckoutURL = ('https://softwork.tsh.tp.edu.tw/t-tools/dailycheck_show.php?action=checkout')
Browser.get(dailycheckoutURL)
Browser.save_screenshot('dailycheckout.png')
Browser.refresh() # 重新整理網頁確認成功
time.sleep(5) # Let the user actually see something!

# 關閉Chrome
Browser.quit()