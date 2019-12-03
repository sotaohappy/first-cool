import re
a = re.compile(r'[0-2]\d:[0-5]\d:[0-5]\d \S+') 
b = "07:00:00 中华人民共和国国歌"
m = re.match(a, b)
print(m.group())