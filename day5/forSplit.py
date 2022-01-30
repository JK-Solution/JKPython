#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   forSplit.py
@Time    :   2022/01/29 09:52:29
@Author  :   Zhang Hong 
@Version :   1.0
@Contact :   zh224635@163.com
@License :   (C)Copyright 2021-2022, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib

# 利用切片复制列表
# 切割标识 [:]  
# 效果 可以在迭代序列的时候修改集合，不会影响序列正常迭代

words = ['cat' , 'dog' , 'windows']

for word in words[:]:
    if len(word) > 6:
        words.insert(0,word)
print(words)