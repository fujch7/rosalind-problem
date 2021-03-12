with open('10_motif.fasta') as file:
    content = file.readlines()
sequence = content[0].rstrip()
motif = content[1].rstrip()
seqlen = len(sequence)
motiflen = len(motif)
n = seqlen - motiflen + 1
location = ''
for i in range(n):
    try:
        kmer = sequence[i:i + motiflen]
        if motif == kmer:
            q = i + 1
            location = location + str(q) + ' '
        else:
            continue
    except Exception as err:
        print('错误原因:', err)

print(location)
