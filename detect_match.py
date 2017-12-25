# Detect perfectly complimentary DNA strings
# Created 12.25.2017 by CB Fay

table = {
    'A' : 'T',
    'T' : 'A',
    'C' : 'G',
    'G' : 'C' }

def detect_match(x, y):
    if len(x) != len(y):
        print('Error: Uneven sequence lengths!')
        return False
    
    length = 0
    for i in range(len(x)):
        if table[x[i]] != y[i]:
            print('Error: Invalid pair at position {}:'.format(i), end='')
            print('  {} -> {}'.format(x[i], y[i]))
            return False
        length += 1
        
    print('Success! Matching sequences of length {}.'.format(length))
    return True
