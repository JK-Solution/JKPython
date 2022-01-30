#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   for.py
@Time    :   2022/01/29 09:51:53
@Author  :   Zhang Hong 
@Version :   1.0
@Contact :   zh224635@163.com
@License :   (C)Copyright 2021-2022, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib

# for 
# python中for语句依据任意序列/字符串的子项，按照其在序列中的顺序来迭代

words = ['cat' , 'dog' , 'windows']

for word in words:
    print(word , len(word) , word.index)
