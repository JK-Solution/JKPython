#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   Exception.py
@Time    :   2022/03/19 14:45:27
@Author  :   Zhang Hong 
@Version :   1.0
@Contact :   zh224635@163.com
@License :   (C)Copyright 2021-2022, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib

while True:
    try:
        n = input("请输入一个整数: ")
        n = int(n)
        break
    except ValueError as e:
        print("无效数字，再次输入...", e)
print("输入成功!")