'''
@Author: sotao
@Date: 2019-12-04 16:22:36
@LastEditors: sotao
@LastEditTime: 2019-12-06 20:51:27
'''
import re
import os

def switch_time(fetch_address, save_address):
    with open(fetch_address) as fetch_object_1:
        lines = fetch_object_1.readlines()
    match_re = re.compile(r'[0-2]\d:[0-5]\d:[0-5]\d \S+')
    match_time_ls = []
    match_program_ls = []
    time_program_ls = []
    for line in lines:  # 依次读取每行
        line = line.strip()  # 去除每行首尾的空格
        # 匹配正则表达式的节目单，保存在match_re_list中
        match_re_list = match_re.findall(line)
        if len(match_re_list) > 0:                         # 列表中有元素
            time_program_ls = match_re_list[0].split(' ')  # 将match_re_list，以空格来分割成两个元素
            # 第一个元素（时间），保存在match_time_ls列表中
            match_time_ls.append(time_program_ls[0])
            # 第二个元素（节目名称），保存在match_program_ls列表中
            match_program_ls.append(time_program_ls[1])
        else:
            continue
    print(match_time_ls)
    print(match_program_ls)
    
    seconds_time_ls = []
    for match_time in match_time_ls:                           # 依次读取match_time_ls列表中元素
        if match_time!=None:
            apart_time_ls = match_time.split(':')                  # 将时间以“:”符号分割成列表
            apart_time_seconds = 3600 * \
            int(apart_time_ls[0]) + 60 * int(apart_time_ls[1]) + \
            int(apart_time_ls[2])                        # 将时间转换成秒数
            seconds_time_ls.append(apart_time_seconds)            # 将所有秒数放到seconds_time_ls列表内
        else:
            continue
    print(seconds_time_ls)
    time_length_ls = []
    for n in range(1, len(seconds_time_ls)):            # 循环列表元素个数减1次
        time_length = seconds_time_ls[n] - seconds_time_ls[n - 1]   # 列表内前后元素作差
        time_length_ls.append(str(time_length))  # 差值计算出来之后是int类型，转换成str后将各个差值放到列表中
    time_length_ls.append('0')
    print(time_length_ls)
    
    merge_time_length_program_ls = []
    # 将三个列表中的同位置元素合并成一个元素，存放在merge_time_length_program_ls列表中
    merge_time_length_program_ls = map(lambda x, y, z: x + ' ' + y + ' ' + z, match_time_ls, time_length_ls, match_program_ls)
    
    for t in merge_time_length_program_ls:                              # 依次读取列表中元素
        if t is not None:
            with open(save_address, 'a') as save_object_2:
                save_object_2.write(str(t) + '\n')  # 将每个元素写入记事本
