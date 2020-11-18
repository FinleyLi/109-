#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
座號:5
姓名:何昱靚
"""


# In[1]:


#一、四則運算
#甲、計算20000*(1+0.03)的結果

print('1.',20000*(1+0.3))

#乙、計算2**10的結果

print('2.',2**10)


# In[3]:


#二、字串相加、複製處理
#甲、字串相加的結果
str1='Sun'
str2='day'
str3=str1+str2
print('1.',str3)
#乙、計算字串長度
print('2.',len(str3))


# In[4]:


#數字加總
#三個數值的總和
NumA=int(input('請輸入數字1.'))
NumB=int(input('請輸入數字2.'))
NumC=int(input('請輸入數字3.'))

Ans=NumA+NumB+NumC
print('3數總和:',Ans)


# In[6]:


#資料型別轉換函數操作
#二進位
NumD=100
print('1.',bin(NumD))
#十六進為
print('2.',hex(NumD))


# In[12]:


#計算本利和
i=int(input("請輸入年利率 = "))
p=int(input("請輸入本金 = "))
n=int(input("請輸入存數年數 = "))

Principal_Interest = p*((1+i)**n)
print('本金加利息合計 = %8.2f' % (Principal_Interest))


# In[14]:


#依照報考汽機車駕照年齡資格(18 歲)判斷
Age_Drive = int(input("請輸入您年齡 = "))
if Age_Drive >=18 :
    print('可以報考汽機車駕照')
else :
    print('不可以報考汽機車駕照')


# In[15]:


#計算貨幣升貶值幅度
Old_Rate = int(input("請輸入舊匯率"))
New_Rate = int(input("請輸入新匯率"))
Change = ((Old_Rate - New_Rate))*100
print(Change)
if Change >0 :
    Result = "升值"
    print("貨幣升值幅度 = % 4.2f%s" % (Change, "%" ,Result))


# In[ ]:




