file =  open("1_count_dna_nucleotides.fasta" , "rt").read()
chars = list(file)
counts = {}
for char in chars:
    if char in counts:
        counts[char] = counts[char] + 1
    else:
        counts[char] = 1
items = list(counts.items())
print(items)
    

