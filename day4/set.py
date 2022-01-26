#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   set.py
@Time    :   2022/01/11 11:10:09
@Author  :   Zhang Hong 
@Version :   1.0
@Contact :   zh224635@163.com
@License :   (C)Copyright 2021-2022, Liugroup-NLPR-CASIA
@Desc    :   不同元素放在一起成为集合
             集合本身为无序的。 不能为集合创建索引。 
             集合不能有重复元素
'''

# here put the import lib

# create set
set1 = set('abcdde')
set2 = set([1,2,3,4,5,6,7,8])
set3 = frozenset("xuanhun")

print(type(set1))
print(type(set3))
print(set2)

for item in set3:
    print(item)

#  Internal methods update the set
set2.add('j')
print(set2)

set2.remove(3)
print(set2)

set2.update([19,20,21,22,23,24,25,26])
print(set2)

print('==============union==================')

#union 

s1 = set('abcdde')
s2 = set([1,2,3,4,5])
s4 = s1 | s2
print(s4)