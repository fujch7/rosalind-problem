dict = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "UCU": "S", "UCC": "S", "UCA": "S",
        "UCG": "S", "UAU": "Y", "UAC": "Y", "UAA": "", "UAG": "", "UGU": "C", "UGC": "C", "UGA": "",
        "UGG": "W", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L", "CCU": "P", "CCC": "P", "CCA": "P",
        "CCG": "P", "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q", "CGU": "R", "CGC": "R",
        "CGA": "R", "CGG": "R", "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M", "ACU": "T",
        "ACC": "T", "ACA": "T", "ACG": "T", "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
        "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R", "GUU": "V", "GUC": "V",
        "GUA": "V", "GUG": "V", "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E", "GGU": "G", "GGC": "G",
        "GGA": "G", "GGG": "G"}
with open('9_translate.fasta') as file:
    file = file.readlines()
rna = file[0].rstrip()
codons = []
protein = ''
n = int(len(rna) / 3)
print(n)
for i in range(n):
    codons.append(rna[3 * i:3 * i + 3])
print(codons)
for codon in codons:
    protein = protein + dict[codon]

with open('9_protein.fasta', 'a') as result:
    result = result.write(protein)
