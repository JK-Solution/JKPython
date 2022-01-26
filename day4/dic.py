#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   dic.py
@Time    :   2022/01/11 10:20:cl48
@Author  :   Zhang Hong 
@Version :   1.0
@Contact :   zh224635@163.com
@License :   (C)Copyright 2021-2022, Liugroup-NLPR-CASIA
@Desc    :   字典， 可变容器模型。 
             每个键值对用冒号分割， 整个字典包括在花括号中，格式如下
             d = {key1: value1, key2: value2} 
             键必须时唯一的。 键必须是不可变的 。 访问字典中没有的键，会输出错误。
             键必须不可变。 可以使用数字，字符串，元组当作key ， 不可使用列表
            
'''

# here put the import lib

dict = {'Name':'Zara','Age':7,'Class':'First'}

print("dict['Name'] : " , dict['Name'])

print("dict['Age'] : " , dict['Age'])

dict['Age'] = 10

print("dict['Age'] : " , dict['Age'])

# delete dict

del dict['Age']  # delete form dict Age properties

dict.clear() # clear all dict properties

del dict # remove dict
