file = open("ebola_isolate.txt", "r")
gene = file.read().replace('\n', '')

compliment = {'A':'T', 'G':'C', 'T':'A', 'C':'G'}

# using the join method to string-ify a list
inverse = "".join([compliment[base] for base in gene])

# slice reversal
sample = gene[:10]
reverse = sample[::-1]
