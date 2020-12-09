# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#pip install selenium

import time
from selenium import webdriver

# private mode
'''
from selenium.webdriver.chrome.options import Options


options = Options()
#關閉瀏覽器跳出訊息
prefs = {
    'profile.default_content_setting_values' :
        {
        'notifications' : 2
         }
}
options.add_experimental_option('prefs',prefs)
options.add_argument("--headless")            #不開啟實體瀏覽器背景執行
options.add_argument("--start-maximized")     #最大化視窗
options.add_argument("--incognito")           #開啟無痕模式
'''

from selenium.webdriver.common.keys import Keys

Browser = webdriver.Chrome()
LoginUrl= ('https://softwork.tsh.tp.edu.tw/t-tools/index.php')
UserName= ('hk3345678')
UserPass= ('ilikemoney')

Browser.get(LoginUrl)
Browser.find_element_by_id('teacher_log').send_keys(UserName)
Browser.find_element_by_id('teacher_pw').send_keys(UserPass)
Browser.find_element_by_id('teacher_pw').send_keys(Keys.ENTER)
time.sleep(5) # Let the user actually see something!
'''
btn = Browser.find_element_by_name("Submit")
btn.click()
'''
dailycheckURL = ('https://softwork.tsh.tp.edu.tw/t-tools/dailycheck.php')
Browser.get(dailycheckURL)
Browser.save_screenshot('dailycheck.png')

dailycheckoutURL = ('https://softwork.tsh.tp.edu.tw/t-tools/dailycheck_show.php?action=checkout')
Browser.get(dailycheckoutURL)
Browser.save_screenshot('dailycheckout.png')
Browser.refresh()
time.sleep(5) # Let the user actually see something!
Browser.quit()