file = open("2_transcribe_dna_into_rna.fasta", "rt").read()
file = file.replace("T","U")
ofile = open("2_result_transcribe_dna_into_rna.fasta","w+")
ofile.write(file)