'''
@Author: sotao
@Date: 2019-12-06 11:36:25
@LastEditors: sotao
@LastEditTime: 2019-12-06 11:45:32
'''
import re
def find_date_channel(txt_line):
    date_re = re.compile(r'^播出日期 \S+')
    date_re_list = date_re.findall(txt_line)
    channel_re = re.compile(r'^频道名称 \S+')
    channel_re_list = channel_re.findall(txt_line)
