import re
import os
def tiquepg(fname_1,fname_2):
    with open(fname_1) as f_object_1:
        lines = f_object_1.readlines()
    match_1 = re.compile(r'[0-2]\d:[0-5]\d:[0-5]\d')
    for line in lines:
        line = line.strip() 
        rematch = re.match(match_1, line)
        if rematch is not None:
            with open(fname_2, 'a') as f_object_2:
                f_object_2.write(rematch.group() + '\n')

epgdir = input("EPG源文件地址：")
epglist = os.listdir(epgdir)    #取当前文件中所有EPG文档的名称，存在epglist列表中
print(epglist)
print(len(epglist))
epgsave = input("EPG保存地址： ")
for epgname in epglist:   #依次读取列表中EPG文档的名称
    epgadd = os.path.join(epgsave, epgname)   #合并出创建新EPG文件
    print(epgadd)
    epgadd_1 = os.path.join(epgdir, epgname)
    tiquepg(epgadd_1, epgadd)



