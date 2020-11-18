# 輸入一個整數
# 輸出判斷是否為3或5的倍數

#1
x = int(input('請輸入一個整數：'))
if x%3 ==0:
    if x%5 ==0:
        print(x, '即是3的倍數又是5的倍數')
    else:
        print(x, '不是3或5的倍數')
else:
    print(x, '不是3或5的倍數')


# 作業一.1 判斷 3和5的倍數

Num = int(input())# 3, 5最小公倍數
if (Num%15 == 0 ):
    print('Num同時為3和5的倍數')
else :
    print('Num不是我們要找的數')
    
    
# 作業一.2 輸入兩數，輸出兩數的乘積

Num121 = int(input('輸入數字(1): '))
Num122 = int(input('輸入數字(2): '))

#計算乘積並輸出
Ans12 = Num121*Num122
print('兩數乘積: ', Ans12)
