import sys

def gcd(x, y):
    if not y: return x
    z = x % y
    return gcd(y, z)

def iter_gcd(x, y):
    """ Runs the Euclidean algorithm on two integers. """
    if x < 1 or y < 1:
        raise ValueError('Must be positive integers.')
    if x == y:
        announce(x, y, x)
        return x

    if x > y: # makes sure that y>x
        q = x
        x = y
        y = q

    a = y
    b = x
    c = y
    while not ( c == 0 or c == 1 ): # The algorithm.
        while c > b: 
            c = a - b
            a = c
        a = b
        b = c
        c = a - b

    announce(b, x, y)
    return b
         
def announce(r, x, y):
    print('The greatest common factor of {} and {} is {}.'.format(x, y, r))

def main():
    s = input("Please enter two integers, separated by a space: ")
    l = []
    for t in s.split(): # Processes string into list of integers.
        try:
            l.append(int(t))
        except ValueError:
            pass
    gcd(l[0], l[1])

