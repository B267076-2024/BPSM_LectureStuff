#!/usr/bin/python3
#Get the content of the sequence
my_seq =open("/home/s2668298/Exercises/Lecture12/seq1.txt")
all_seq=my_seq.read()
#Check if all the sequences are DNA and find there are "K,L,S,X,t", 
# which are wrong characters in DNA seq,so detele them
print(sorted(all_seq))
cor_seq=all_seq.replace("K","").replace("L","").replace("S","").replace("X","").replace("t","T")
print(cor_seq)
#Seperrate the first and the second exon
exon_1=cor_seq[0:63]
exon_2=cor_seq[90:]
my_fasta_file=open("fas1.txt","w")
my_fasta_file.write(">First Exon and length is "+ str(len(exon_1))+"\n"
                    +exon_1+"\n>Second Exon and length is "+str(len(exon_2))+"\n"+exon_2)
my_fasta_file.close()
print(open("fas1.txt").read().rstrip("\n"))

