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
print(pd)

# 篩選美金對台幣匯率

print(pd['USDTWD'])


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
print(dfs)

currency = dfs[0]
currency.iloc[:,0:5]
