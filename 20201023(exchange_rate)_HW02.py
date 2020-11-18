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
