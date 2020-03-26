#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, shutil

rootDir = "\\replace\\test"
nameFile = '\\replace\\test.txt'

def factoryReplace(dirPath):
    if not os.path.exists(dirPath):
        print(dirPath, 'is not exist')
        return

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
    if not os.path.exists(dirPath):
        print(dirPath, 'is not exist')
        return

    if not os.path.exists(nameText):
        print(nameText, 'is not exist')
        return
    
    with open(nameText, 'r', encoding='UTF-8') as f:
        for file in os.listdir(dirPath):
            filePath = dirPath + '\\' + file
            if os.path.isfile(filePath):
                print('old file\t',filePath)
                newName = f.readline()
                if newName != '':
                    if newName.strip() != '':
                        newName = dirPath + '\\' + newName.strip() + os.path.splitext(file)[1]
                        print('new file\t', newName)
                        os.rename(filePath, newName)
                else:
                    break


if __name__ == '__main__':
    #factoryReplace(rootDir)
    fileRename(rootDir, nameFile)
