#!/usr/bin/python3
#Include some packages
import os, subprocess, shutil
#Change the working directory
os.chdir("/home/s2668298/Exercises/Lecture12")
#Get the content of the sequence
my_seq =open("/home/s2668298/Exercises/Lecture12/seq1.txt")#Used the Linux command cp to get 
all_seq=my_seq.read()
#Check if all the sequences are DNA and find there are "K,L,S,X,t", 
# which are wrong characters in DNA seq,so detele them
print(sorted(all_seq))
cor_seq=all_seq.replace("K","").replace("L","").replace("S","").replace("X","").replace("t","T")
print(cor_seq)
#Seperrate the first and the second exon
exon_1=cor_seq[0:63]
exon_2=cor_seq[90:].rstrip("\n")
non1=cor_seq[63:90]
#my_fasta_file=open("fas1.txt","w")
#my_fasta_file.write(">First Exon and length is "+ str(len(exon_1))+"\n"
#                    +exon_1+"\n>Second Exon and length is "+str(len(exon_2))+"\n"+exon_2)
#my_fasta_file.close()
#print(open("fas1.txt").read().rstrip("\n"))


#Remote Sequence: split the coding:29-409(come from the genbank CDS annotation) 
#and the non-coding area
my_seq2=open("/home/s2668298/Exercises/Lecture12/seq2.fasta")
re_seq=my_seq2.read().replace("\n","")
print("\n"+re_seq)
coding_seq = re_seq[28:409]
non_coding_seq1 =re_seq[0:28]
non_coding_seq2 =re_seq[409:]
#Create the file for each part of the sequence
my_fasta_file=open("Two_seq.fasta","w")
my_fasta_file.write(">Local_Sequence_length"+str(len(cor_seq))+"\n"+cor_seq+
                    "\n>Remote_Sequence_length"+str(len(re_seq))+"\n"+re_seq+"\n")
my_fasta_file.close()
code_file=open("Coding_Sequence.fasta","w")
code_file.write("Local_Exon1_length"+str(len(exon_1))+"\n"+exon_1+"\n"+
                "Local_Exon2_length"+str(len(exon_2))+"\n"+exon_2+"\n"+
                "Remote_exon_length"+str(len(coding_seq))+"\n"+coding_seq+"\n")
code_file.close()
non_code_file=open("Non_Coding_Sequence.fasta","w")
non_code_file.write("local_sequence_non_coding_length" + str(len(non1))+"\n"+non1+
                    "\nremote_sequence_non_coding1_length"+str(len(non_coding_seq1))+"\n"+non_coding_seq1+
                    "\nremote_sequence_non_coding2_length"+str(len(non_coding_seq2))+"\n"+non_coding_seq2)
non_code_file.close()




