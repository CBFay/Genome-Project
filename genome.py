# Useful operations on DNA representative Strings
# Created 12.25.2017 by CB Fay

pair = {
    'A' : 'T',
    'T' : 'A',
    'C' : 'G',
    'G' : 'C' }

def ismatch(x, y):
    """Detect perfectly complimentary DNA strings."""
    if len(x) != len(y):
        print('Error: Uneven sequence lengths!')
        return False
    
    length = 0
    for i in range(len(x)):
        if pair[x[i]] != y[i]:
            print('Error: Invalid pair at position {}:'.format(i), end='')
            print('  {} -> {}'.format(x[i], y[i]))
            return False
        length += 1
        
    print('Success! Matching sequences of length {}.'.format(length))
    return True


def compliment(x):
    """Return the compliment to a base sequence."""
    y = ''
    for i in x:
        try:
            y += pair[i]
        except KeyError:
            print('Invalid character {} at position {}.'.format(
                repr(i), len(y)+1))
            return None
    return y
