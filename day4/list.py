#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   list.py
@Time    :   2022/01/09 20:29:18
@Author  :   Zhang Hong 
@Version :   1.0
@Contact :   zh224635@163.com
@License :   (C)Copyright 2021-2022, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib

list1 = ['physics' , 'linear' , 'angular']

#更新列表

list1[1] = 'pig'

print(list1)

#删除元素

del(list1[1])

print(list1)

#操作符
print('操作符 + --------------------------------')
print(list1 + list1)
print('操作符 * --------------------------------')
list2 = ['fuck'] * 100
print(list2)