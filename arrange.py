with open("README.txt","r") as f:
    src = f.read().replace("\r","")

lines = filter(lambda x:x[0]!="#",filter(lambda x:len(x)!=0,src.split("\n")))

useless = " \r\n\t"
find_useless = lambda n:min(filter(lambda x:x!=-1,map(n.find,useless)))

output = "# windows-input-method-emoticon\r\n"

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
for i,j in dicts.items():
    output += "%s %s\r\n"%(i,j)

with open("README.txt","w") as f:
    f.write(output)
