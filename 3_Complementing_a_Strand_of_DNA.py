file = open("3_Complementing_a_Strand_of_DNA.fasta","rt").read()
file = file.replace("A","t")
file = file.replace("T","a")
file = file.replace("C","g")
file = file.replace("G","c")
file = file.upper()
file = file[::-1]
ofile = open("3_result_Complementing_a_Strand_of_DNA.fasta","w+")
ofile.write(file)