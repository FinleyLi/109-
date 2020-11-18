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

# 排序
a = [50, 20, 60, 40, 30]
print('a: ', a)
a.sort()
print('排序後的結果 a: ', a)
