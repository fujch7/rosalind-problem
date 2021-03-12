from collections import Counter
from def_func import readfasta

fasta_dic = readfasta('11_consensus.fasta')
column = []
seqlist = []
#将序列存入seqlist列表中
for k, v in fasta_dic.items():
    seqlist.append(v)

seqlen = len(seqlist[0].rstrip())
n = len(seqlist)
#将列表转置，将每条序列的同一个位置的碱基连接起来作为新列表的一个元素
for m in range(seqlen):
    col = ''

    for i in range(n):
        col = col + seqlist[i][m]

    column.append(col)
#定义字符串，作为countbase的参数row传入
a = 'A: '
c = 'C: '
g = 'G: '
t = 'T: '

#计算每个元素中目的碱基(base)的个数，传入参数目的碱基base和字符串row
def countbase(base, row):
    for col in column:
        basenumber = col.count(base)
        row = row + str(basenumber) + ' '
    return row

#传入column列表，使用counter类创建对象，使用most_common方法统计字符串中各个碱基的个数，返回一个包含元组的列表。
def pop_max_str(column):
    consensus = ''

    for i in column:
        dict_sorted = Counter(i)
        consensus = consensus + dict_sorted.most_common()[0][0]
    return consensus
line1 = pop_max_str(column)+'\n'
line2 = countbase('A', a)+'\n'
line3 = countbase('C', c)+'\n'
line4 = countbase('G', g)+'\n'
line5 = countbase('T', t)+'\n'

with open('consensus.txt', 'a') as result:
    result = result.writelines([line1, line2, line3, line4, line5])
    

# print(pop_max_str(column))
# print(countbase('A', a))
# print(countbase('C', c))
# print(countbase('G', g))
# print(countbase('T', t))
