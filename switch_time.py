'''
@Author: sotao
@Date: 2019-12-04 16:22:36
@LastEditors: sotao
@LastEditTime: 2019-12-04 17:19:32
'''
import re
import os


def switch(switch_1, switch_2):
    with open(switch_1) as switch_object_1:
        lines = switch_object_1.readlines()
    seconds_ls = []
    for line in lines:                             # 依次读取每行
        line = line.strip()                        # 去除每行首尾的空格
        data_ls = line.split(':')                  # 将时间以“:”符号分割成列表
        data_seconds = 3600 * \
            int(data_ls[0]) + 60 * int(data_ls[1]) + \
            int(data_ls[2])                        # 将时间转换成秒数
        seconds_ls.append(data_seconds)            # 将所有秒数放到列表seconds_ls里
    time_ls = []
    for n in range(1, len(seconds_ls)):            # 循环列表元素个数减1次
        time = seconds_ls[n] - seconds_ls[n - 1]   # 列表内前后元素作差
        time_ls.append(time)                       # 将各个差值放到列表中

    for t in time_ls:                              # 依次读取列表中元素
        if t is not None:
            with open(switch_2, 'a') as switch_object_2:
                switch_object_2.write(str(t) + '\n')  # 将每个元素写入记事本


def switch_time(fetch_address, save_address):
    with open(fetch_address) as fetch_object_1:
        lines = fetch_object_1.readlines()
    match_1 = re.compile(r'[0-2]\d:[0-5]\d:[0-5]\d')  #通过正则表达式提取出时间
    match_ls = []
    for line in lines:                                 #依次读取每行
        line = line.strip()                            #去除每行首尾的空格
        rematch = re.match(match_1, line)
        match_ls.append(rematch)
    '''
    以上写出的函数部分 是 把匹配的时间 保存在列表中
    下面的函数 处理 将处理列表中的时间 转换成秒数 并把转好的数据保存 一个列表中
    重新写出一个 正则表达式 将读取的 时间  节目名称 分别保存另外在两个列表中
    将这三个列表 每个元素 合并成一个小列表 再把各个小列表合并成一个大列表
    对于 播出频道 和  每天的日期  再读取 存放 在一个列表中
    合并以上列表中的数据 按照 节目单格式 整体输出 到 save_address 的地址

    '''
    

# 取当前文件中所有EPG文档的名称，存在epg_name_ls列表中
epg_fetch_address = input("EPG源文件地址：")
epg_name_ls = os.listdir(epg_fetch_address)
print(epg_name_ls)
print(len(epg_name_ls))
epg_save_address = input("EPG保存地址： ")
for epg_name in epg_name_ls:                                           # 依次读取列表中EPG文档的名称
    epg_merge_save_address = os.path.join(
        epg_save_address, epg_name)  # 合并出保存新EPG文件路径
    print(epg_merge_save_address)
    epg_merge_fetch_address = os.path.join(
        epg_fetch_address, epg_name)                                   # 合并出读取源EPG文件路径
    switch_time(epg_merge_fetch_address, epg_merge_save_address)
