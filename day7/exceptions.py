#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   exceptions.py
@Time    :   2022/03/19 15:04:12
@Author  :   Zhang Hong 
@Version :   1.0
@Contact :   zh224635@163.com
@License :   (C)Copyright 2021-2022, Liugroup-NLPR-CASIA
@Desc    :   多异常捕捉
'''

# here put the import lib

import sys

try:
    f = open('integers.txt')
    s = f.readline()
    i = int(s.strip())
except (IOError, ValueError):
    print("An IO error or a ValueError occurred")
except:
    print("An unexpected error occurred")
    raise