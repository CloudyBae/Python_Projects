"""You work for a bioengineering company that specializes in developing therapeutic solutions.
Your team has just been given a new project to develop a targeted therapy for a rare type of cancer.
Instructions
Your task is determine the RNA complement of a given DNA sequence.
Both DNA and RNA strands are a sequence of nucleotides.
The four nucleotides found in DNA are adenine (A), cytosine (C), guanine (G) and thymine (T).
The four nucleotides found in RNA are adenine (A), cytosine (C), guanine (G) and uracil (U).
Given a DNA strand, its transcribed RNA strand is formed by replacing each nucleotide with its complement:
G -> C
C -> G
T -> A
A -> U"""
strand = {"G":"C", "C":"G", "T":"A", "A":"U"}

def to_rna(dna_strand):
    rna = ""
    for i in dna_strand:
        rna += strand[i]
    return rna
