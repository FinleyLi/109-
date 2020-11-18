import random
import inspect

print(inspect.getsource(random.randint))
print(inspect.getsource(print))

print(inspect.getsource(sorted)) # raises a TypeError
type(sorted) # <class 'builtin_function_or_method'>


#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
二進制相關知識，包括轉換為十進制，移位操作和邏輯操作
"""

def decimal_to_binary(decimal_val):
    '''
    十進制轉為二進制
    :param decimal_val:
    :return:
    '''
    print('transfer %d to binary' % decimal_val)
    recursion_result = change(decimal_val)
    print('遞迴實現轉換結果：', recursion_result)


# 十進制轉二進制的方法：除2取餘，逆序排列, https://blog.csdn.net/shirley_sweet/article/details/73896279
def change(n):
    result = '0'
    if n == 0:  # 輸入為0的情況
        return result
    else:
        result = change(n // 2)  # 調用自身
        return result + str(n % 2)

if __name__ == '__main__':
    dec_val = 64

    print('use build function to transform decimal value')
    decimal_to_binary(dec_val)


dec = int(input('請輸入10進位數值:'))

print( '轉換為2進位: ', bin(dec))
