#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   string.py
@Time    :   2022/01/08 15:56:30
@Author  :   Zhang Hong 
@Version :   1.0
@Contact :   zh224635@163.com
@License :   (C)Copyright 2021-2022, Liugroup-NLPR-CASIA
@Desc    :   数据类型
'''

# here put the import lib

# 字符串格式化

# %s 占位符
print("My name is %s , My email is %s , My phone number is %s" %('张宏','zh224635@163.com','17660644635'))

# string 对象 format 函数
print("My name is {name} , My email is {email} , My phone number is {phoneName}".format(name="Jack",email="Jack",phoneName="Jack"))


print("---------------------------------每日作业-----------------------------")

# 编写代码实现逆序输出一个列表。

#list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# reverse function 
# list.reverse();

# sort function
#list.sort(reverse=True);
#print(list);

#编写代码实现查找并替换一个字符串中的一段连续内容

str1 = 'My name is 张宏 , My email is zh224635@163.com , My phone number is 17660644635'
print(str1.find('number'))

