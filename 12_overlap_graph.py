import itertools
from def_func import readfasta

data = readfasta('12_overlap_graph.fasta')
# print(data)
# print(type(itertools.combinations(data, 2)))
# print(itertools.combinations(data, 2))
def overlap_graph(data, k):
    result = []
    seqid = ''
    for a, b in itertools.combinations(data, 2):
        # print(a, b)
        if data[a][-k:] == data[b][0:k]:
            seqid = a + ' ' + b + '\n'
            result.append(seqid)
        elif data[b][-k:] == data[a][0:k]:
            seqid = b + ' ' + a + '\n'
            result.append(seqid)
        else:
            print('无')
    with open('result.txt','a') as resultfile:
        resultfile.writelines(result)
if __name__ == '__main__':
    overlap_graph(data, 3)