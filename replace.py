#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

rootDir = "E:\\reference\\"
suffix ='.md'
reSuffix = '.flv'

for dir in os.listdir(rootDir):
    dirPath = rootDir + dir
    if os.path.isdir(dirPath):
        print(dirPath)
    else:
        if dir.endswith(suffix):
            #print('Markdown file:{}'.format(dirPath))
            name=os.path.splitext(dirPath)[0]
            rename=name+reSuffix
            print(name)
            #os.rename(dirPath, rename)
