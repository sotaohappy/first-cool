# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 13:25:24 2018

@author: sotao
"""

import os

def editepg(filename_1, filename_2):
    with open(filename_1) as file_object_1:
        lines = file_object_1.readlines()
    number = 0
    for line in lines:                           #依次读取每行
        line = line.strip() 
        if not len(line):                        #判断是否是空行
            number += 1
            if number == 3:
                break
        if number == 1 or number == 2:
            with open(filename_2, 'a') as file_object_2:
                file_object_2.write(line + '\n')





epgdir = input("EPG源文件地址：")
epglist = os.listdir(epgdir)    #取当前文件中所有EPG文档的名称，存在epglist列表中
print(epglist)
print(len(epglist))
epgsave = input("EPG保存地址： ")
for epgname in epglist:   #依次读取列表中EPG文档的名称
    epgadd = os.path.join(epgsave, epgname)   #合并出创建新EPG文件
    print(epgadd)
    epgadd_1 = os.path.join(epgdir, epgname)
    editepg(epgadd_1, epgadd)

