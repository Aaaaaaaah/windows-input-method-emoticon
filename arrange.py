#!/usr/bin/env python

import time

with open("README.txt","r") as f:
    src = f.read().replace("\r","")

lines = filter(lambda x:x[0]!="*",filter(lambda x:len(x)!=0,src.split("\n")))

useless = " \r\n\t"
find_useless = lambda n:min(filter(lambda x:x!=-1,map(n.find,useless)))

t = time.ctime()
l = len(t)
a = b = (31-l)/2
if a+b < 31-l:
    b+=1
output = "*********************************\r\n* Windows-Input-Method-Emoticon *\r\n*%s%s%s*\r\n*********************************\r\n\r\n"%(" "*a,time.ctime()," "*b)

dicts = {}
for i in lines:
    try:
        t = i
        while t[0] in useless:
            t=t[1:]
        s = find_useless(t)
        chinese = t[:s]
        t = t[s:]
        while t[0] in useless:
            t=t[1:]
        while t[-1] in useless:
            t=t[:-1]
        emoticon = t
        dicts[chinese] = emoticon
    except:
        pass

lists = dicts.items()
lists.sort()

for i,j in lists:
    output += "%s %s\r\n\r\n"%(i,j)

with open("README.txt","w") as f:
    f.write(output)
