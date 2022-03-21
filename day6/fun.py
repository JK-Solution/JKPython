#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   fun.py
@Time    :   2022/03/05 14:18:42
@Author  :   Zhang Hong 
@Version :   1.0
@Contact :   zh224635@163.com
@License :   (C)Copyright 2021-2022, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib


from tkinter.filedialog import test


def testIfElse():
    '''The method judge num value

    Param x needs to be a Integer value'''
    x = int(input('请输入一个整数:'))
    if x == 0:
        print('%d == 0' % x)
    elif x < 0:
        print('%d < 0' % x)
    else:
        print('%d > 0' % x)


# testIfElse()
# print(testIfElse.__doc__)

def testFor():
    '''The method circulate list

    Cyclically print the elements of the list'''
    print('for testing..........')
    words = ['cat', 'windows', 'defenestrate']
    for word in words:
        print(word, len(word))


# testFor()
# print(testFor.__doc__)

# 利用切片复制列表


def testForSplit():
    '''The method used to split circulate list
    
    copy list ,change it is safer'''
    words = ['cat', 'windows', 'defenestrate']
    for word in words[:]:
        pass
        # if len(word) > 6:
        #     words.insert(0, word)
    print(words)

testForSplit()
print(testForSplit.__doc__)


# while 语句

def testWhile():
    '''The method used while
    
    Repeat an action until the end of the 10
    '''
    count = 0
    while count < 10:
        print('the index is : ' , count)
        count += 1

# testWhile()
# print(testWhile.__doc__)

# RANGE XRANGE

def testRange():
    '''The method test Range method generates a list
    
    fast generates list
    '''
    x = range(1,100,2)
    print(x)
    for i in x:
        print (i)

# testRange()
# print(testRange.__doc__)