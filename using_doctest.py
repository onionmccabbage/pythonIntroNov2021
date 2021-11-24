import doctest

def cube(x):
    '''
    this function returns the cube of a number
    >>> cube(3)
    27
    >>> cube(-1)
    -1
    '''
    return x*x*x # or return x**3

if __name__ == '__main__':
    doctest.testmod(verbose=True) # test this module
    # cube(3) # expect 27