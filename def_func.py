class ReadFastaFile:

    def readfasta(self, fasta_path):
        '''
        输入fasta文件路径作为参数，返回一个包含序列名和序列的字典
        '''
        fasta_dic = {}
        with open(fasta_path) as fas:
            lines = fas.readlines()
        for line in lines:
            str = ''
            if line[0] == '>':
                name = line[1:-1]
                fasta_dic[name] = ''
            else:
                line = line.rstrip()
                str = str + line
                fasta_dic[name] = fasta_dic[name] + str
        return fasta_dic

    def seqlen(self, fasta_dic):
        '''
        输入fasta_dic，返回一个包含序列名和序列长度的字典
        '''
        seqlen_dic = {}
        for k, v in fasta_dic.items():
            seqlen_dic[k] = len(v)
        return seqlen_dic

    def longest_seq(self, seqlen_dic, fasta_dic):
        '''
        输入seqlen_dic和fasta_dic，
        可选择返回最长序列名，最长序列，最长序列长度(int)，以及三者组成的列表
        '''
        self.key_longest = max(seqlen_dic.keys(), key=(lambda k: seqlen_dic[k]))
        self.seq_longest = fasta_dic[self.key_longest]
        self.len_longest = len(self.seq_longest)
        self.longest_seq_data = [self.key_longest, self.len_longest, self.seq_longest]
        return self.longest_seq_data

    def shortest_seq(self, seqlen_dic, fasta_dic):
        '''
        输入seqlen_dic和fasta_dic，
        可选择返回最短序列名，最短序列，最短序列长度(int)，以及三者组成的列表
        '''
        self.key_shortest = min(seqlen_dic.keys(), key=(lambda k: seqlen_dic[k]))
        self.seq_shortest = fasta_dic[self.key_shortest]
        self.len_shortest = len(self.seq_shortest)
        self.shortest_seq_data = [self.key_shortest, self.len_shortest, self.seq_shortest]
        return self.shortest_seq_data