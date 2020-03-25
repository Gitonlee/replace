#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, shutil

rootDir = "C:\\Users\\lilei\\Desktop\\test - 副本"


def factoryReplace(dirPath):
    for subDir in os.listdir(dirPath):
        subDirPath = dirPath + '\\' + subDir
        if os.path.isdir(subDirPath):
            for subsubDir in os.listdir(subDirPath):
                subsubDirPath = subDirPath + '\\' + subsubDir
                if os.path.isdir(subsubDirPath):
                    for file in os.listdir(subsubDirPath):
                        filePath = subsubDirPath + '\\' + file
                        if filePath.endswith('.blv'):
                            name = os.path.splitext(filePath)[0]
                            rename = name + '.flv'
                            os.rename(filePath, rename)
                            print('rename file\t', rename)
                            newFilePath = subDirPath + '\\' + os.path.basename(os.path.splitext(filePath)[0]) + '.flv'
                            shutil.move(rename, newFilePath)
                            print('move file\t', newFilePath)
                        else:
                            os.remove(filePath)
                            print('remove file\t', filePath)
                    shutil.rmtree(subsubDirPath)
                    print('remove folder\t', subsubDirPath)
                else:
                    if not subsubDirPath.endswith('.flv'):
                        os.remove(subsubDirPath)
                        print('remove file\t', subsubDirPath)
        else:
            print('Non dictory path\t', subDirPath)

    print('factory replace finish!')
        

def fileRename(dirPath, nameText):
    for subDir in os.listdir(dirPath):
        subDirPath = dirPath + '\\' + subDir
        if os.path.isdir(subDirPath):
            pass
    pass


if __name__ == '__main__':
    factoryReplace(rootDir)
