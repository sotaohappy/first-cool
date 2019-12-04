'''
@Author: sotao
@Date: 2019-12-03 16:44:07
@LastEditors: sotao
@LastEditTime: 2019-12-04 10:54:43
'''
import os

def switch(sname_1,sname_2):
    with open(sname_1) as s_object_1:
        lines = s_object_1.readlines()
    seconds_ls = []   
    for line in lines:            #依次读取每行
        line = line.strip()           #去除每行首尾的空格
        data_ls = line.split(':')     #将时间以“:”符号分割成列表
        data_seconds = 3600 * int(data_ls[0]) + 60 * int(data_ls[1]) + int(data_ls[2])    #将时间转换成秒数
        seconds_ls.append(data_seconds)   #将所有秒数放到列表seconds_ls里
    time_ls = []
    for n in range(1, len(seconds_ls)):      #循环列表元素个数减1次         
        time = seconds_ls[n] - seconds_ls[n -1]     #列表内前后元素作差
        time_ls.append(time)    #将各个差值放到列表中 

    for t in time_ls:          #依次读取列表中元素
        if t is not None:
            with open(sname_2, 'a') as s_object_2:
                s_object_2.write(str(t) + '\n')      #将每个元素写入记事本

epgdir = input("EPG源文件地址：")
epglist = os.listdir(epgdir)    #取当前文件中所有EPG文档的名称，存在epglist列表中
print(epglist)
print(len(epglist))
epgsave = input("EPG保存地址： ")
for epgname in epglist:   #依次读取列表中EPG文档的名称
    epgadd = os.path.join(epgsave, epgname)   #合并出创建新EPG文件
    print(epgadd)
    epgadd_1 = os.path.join(epgdir, epgname)
    switch(epgadd_1, epgadd)
