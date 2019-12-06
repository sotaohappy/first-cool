'''
@Author: sotao
@Date: 2019-12-06 09:29:23
@LastEditors: sotao
@LastEditTime: 2019-12-06 10:10:56
'''
import os
from switch_time import switch_time

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
