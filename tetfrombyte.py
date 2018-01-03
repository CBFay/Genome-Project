# Convert an 8-bit Integer value into a 4 digit Quaternary value or Nucleotide sequence
# Created on 1.02.2018 by CB Fay

def tetfrombyte(byte, numeric=False):
    
    nt = {0:'A', 1:'T', 2:'C', 3:'G'}
    tet = ''
    
    if numeric == True:
        for i in range(3, -1, -1):
            tet += str((byte // 4**i % 4))
    else:
        for i in range(3, -1, -1):
            tet += nt[(byte // 4**i % 4)]
            
    return tet
