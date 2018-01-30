import re
import sys

#s='{通配符{子通配符}}你好，今天开学了{通配符},你好'
s = 'nihao (woyehao(haha(heihei))(())) woshi lixianyu a '
print("s", s)
#a1 = re.compile(r'\{.*?\}' )
a1 = re.compile(r'\(.+\)')
#a1 = re.compile(r'([()]*)')
d = a1.sub('', s)
print("d:", d)
#print(type(d))
a1 = re.compile(r'\{[^}]*\}' )
d = a1.sub('',s)
print("d",d)
