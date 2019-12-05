'''
@Author: sotao
@Date: 2019-12-05 14:30:44
@LastEditors: sotao
@LastEditTime: 2019-12-05 16:52:44
'''
import os
import re

def switch_time(fetch_address, save_address):
    with open(fetch_address) as fetch_object_1:
        lines = fetch_object_1.readlines()
    match_re = re.compile(r'[0-2]\d:[0-5]\d:[0-5]\d \S+')
    match_time_ls = []
    match_program_ls = []
    time_program_ls = []
    for line in lines:  # 依次读取每行
        line = line.strip()  # 去除每行首尾的空格
        match_re_list = match_re.findall(line)
        if len(match_re_list) > 0:
            time_program_ls = match_re_list[0].split(' ')
            match_time_ls.append(time_program_ls[0])
            match_program_ls.append(time_program_ls[1])
        else:
            continue
    print(match_time_ls)
    print(match_program_ls)

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


