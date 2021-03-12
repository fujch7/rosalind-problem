dic = {}
gcdic = {}
chars = ['G','C']
with open('6_Computing_GC_Content.fasta') as fas:
    lines = fas.readlines()
for line in lines:
    str = ''
    if line[0] == '>':
        name = line[1:-1]
        dic[name] = ''
    else:
        line = line.rstrip()
        str = str + line
        dic[name] = dic[name] + str
for key, value in dic.items():
    n = 0 
    for char in value:
        if char in chars:
            n = n + 1
        gc = n / len(value)
    gcdic[gc] = key
max = sorted(gcdic.keys(),reverse = True)[0]
print(gcdic[max])
print(max*100)
print(gcdic)
