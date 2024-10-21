def reverse_complement(rna_string):
    rna_complement = ""
    rna_counterparts = {"A": "U", "U": "A", "G": "C", "C": "G"}
    for i in range(1, len(rna_string) + 1):
        rna_complement += rna_counterparts[rna_string[-i]]
    return rna_complement


print(reverse_complement("GUGU"))
print(reverse_complement("UCUCG"))
print(reverse_complement("CAGGU"))
print(reverse_complement("UUAUACCCGAGUCGGAUUUGUCACU"))
