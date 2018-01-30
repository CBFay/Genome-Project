# read and analyze an Ebola virus isolate
# https://www.ncbi.nlm.nih.gov/nuccore/KU182909.1
# created 1.30.2017 by CB Fay

file = open("ebola_isolate.txt", "r")
gene = file.read().replace('\n', '')

G = 0
C = 0
A = 0
T = 0

count = 0
for nucleotide in gene:
    base = nucleotide.upper()
    if base == 'G':
        G += 1
    elif base == 'C':
        C += 1
    elif base == 'A':
        A += 1
    elif base == 'T':
        T += 1
    else:
        print('Error, invalid base {} at index {}.'.format(base, count))
        file.close()
        exit()
        
    count += 1
    
print('G:', G)
print('C:', C)
print('A:', A)
print('T:', T)
print('Total:', count)


file.close()
