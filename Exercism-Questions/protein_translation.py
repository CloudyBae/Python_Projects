"""Translate RNA sequences into proteins.
RNA can be broken into three nucleotide sequences called codons, and then translated to a polypeptide like so:
RNA: "AUGUUUUCU" => translates to
Codons: "AUG", "UUU", "UCU" => which become a polypeptide with the following sequence =>
Protein: "Methionine", "Phenylalanine", "Serine"
There are 64 codons which in turn correspond to 20 amino acids; however, all of the codon sequences and resulting amino acids are not important in this exercise. 
If it works for one codon, the program should work for all of them. However, feel free to expand the list in the test suite to include them all.
There are also three terminating codons (also known as 'STOP' codons); if any of these codons are encountered (by the ribosome), 
all translation ends and the protein is terminated."""

protein = {"AUG": "Methionine", "UUU": "Phenylalanine", "UUC": "Phenylalanine", "UUA": "Leucine", "UUG": "Leucine",
           "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine", "UAU": "Tyrosine", "UAC": "Tyrosine", "UGU": "Cysteine",
           "UGC": "Cysteine", "UGG": "Tryptophan", "UAA": "STOP", "UAG": "STOP", "UGA": "STOP"}

def proteins(strand):
    codons = [strand[i:i+3] for i in range(0, len(strand), 3)]
    protein_list = []
       
    for value in codons:        
        protein_name = protein[value]
        protein_list.append(protein_name)
        
    if "STOP" in protein_list:
        stop_index = protein_list.index("STOP")
        return protein_list[:stop_index]
    else:
        return protein_list