#Problem 1
seq1 ="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
num_A = seq1.count("A")
num_T = seq1.count("T")
proAT = (num_A+num_T)/len(seq1)
print("In Problem1: \n""The number of T nucleotides is " + str(num_T) + 
      "\nThe number of A nucleotides is " + str(num_A) + 
      "\nThe proportion of A+T is " +str("{:.2f}".format(proAT)))
#Problem 2
seq_con = seq1.replace("A","M").replace("T","A").replace("M","T").replace("G","M").replace("C","G").replace("M","C")
print("\nIn Problem2:\nThe complement of the sequence is " + seq_con)
#Problem 3
seq3 ="ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
cut_point =seq3.find('GAATTC')
print("\nIn Problem3:\nThe position of the cut is " + str(cut_point + 1) +
      "\nThe length of the second fragment is " + str(len(seq3)-cut_point-1))
#Problem 4
seq4 = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1 = seq4[0:63]
exon2 = seq4[90:]
code_seq = exon1 + exon2
print("\nIn Problem4:\nThe length of the coding sequence is " + str(len(code_seq)) +
      " and the proportion is " + str("{:.2f}".format(len(code_seq)/123*100))+"%")
intron = seq4[63:90].lower()
long_seq = exon1 + intron + exon2
print("The long sequence is " + long_seq)