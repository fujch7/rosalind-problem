'''
最短motif长度为2，最长motif长度为最短序列的长度。
使用二分法查找最长的长度
'''
from def_func import ReadFastaFile


def motif_produce(mid):
    '''
    输入一个mid值（即k），返回一个含有所有k长度的motif的列表
    '''
    motif_list = []
    n = shortest_seq_data[1] - mid + 1
    for i in range(n):
        motif = shortest_seq_data[2][i:i+mid]
        motif_list.append(motif)
    return motif_list


def single_motif_test(motif):
    '''
    将一个motif与所有序列进行比对，
    如果有一个序列比对不成功则返回False并直接退出循环
    '''
    for seq in fasta_dic.values():
        if motif not in seq:
            return 0
            # break
        else:
            continue
    else:
        return 1


def all_motif_test(motif_list):
    '''
    传入一个k长度motif的列表
    循环使用single_motif_test函数判断
    使用二分法不断缩小最长motif的k值所在的范围，直至确定
    如果该列表存在shared motif则扩大范围
    如果不存在shared motif则缩小范围
    注意函数的递归调用要使用return返回函数自身
    '''
    all_shared_motif = []
    global left, right, mid
    for motif in motif_list:
        if single_motif_test(motif) == 1:
            # print('---->', left, mid, motif)
            if left == mid:
                # print(motif)
                # return motif_list
                # break
                if single_motif_test(shortest_seq_data[2]) == 1:
                    return shortest_seq_data[2]
                else:
                    all_shared_motif.append(motif)
            else:
                left = mid
                mid = (left + right)//2
                return all_motif_test(motif_produce(mid))
        elif single_motif_test(motif) == 0:
            continue

    if all_shared_motif:
        return all_shared_motif
    else:
        if mid == 2:
            print('There is no shared motif between these sequences!')
        else:
            right = mid
            mid = (left + right) // 2
            return all_motif_test(motif_produce(mid))


if __name__ == '__main__':
    data = ReadFastaFile()  # 创建读取fasta文件的对象
    fasta_dic = data.readfasta('14_find_shared_motif.fasta')  # 将序列文件读取为字典
    seqlen_dic = data.seqlen(fasta_dic)  # 创建序列长度的字典
    # print(fasta_dic)
    # print(seqlen_dic)
    # print(data.shortest_seq(seqlen_dic, fasta_dic))
    shortest_seq_data = data.shortest_seq(seqlen_dic, fasta_dic)  # 返回序列名，序列长度和序列，类型为列表
    left = 2  # 最短motif长度
    right = shortest_seq_data[1]  # 最长motif长度
    mid = (left + right) // 2  # motif长度中间值
    motif_list = motif_produce(mid)  # 产生第一个motif列表，每个motif长度为mid
    motif = all_motif_test(motif_list)  # 最终结果，一个包含所有最长shared motif的列表
    print(motif)
