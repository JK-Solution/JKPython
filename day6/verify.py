#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   verify.py
@Time    :   2022/03/07 10:06:42
@Author  :   Zhang Hong 
@Version :   1.0
@Contact :   zh224635@163.com
@License :   (C)Copyright 2021-2022, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib

def verify():
    x = 0
    while(x == 0):
        username = input("请输入用户名:")
        if username == "seven":
            password = input("请输入密码:")
            if password == "123":
                print("login success")
                break
            else:
                print("login fail , password mismatch")
        else:
            print("login fail , username mismatch")

# verify()

def sum():
    '''The method is sum
    
    calculate 2 - 3 + 4 - 5 - 6 - 7 - 8 - 9 .. + 100 sum'''
    x = 3
    sum = 2
    while(x <= 100):
        sum += 1;
        x += 2;
    print("sum is " , sum)

sum()

