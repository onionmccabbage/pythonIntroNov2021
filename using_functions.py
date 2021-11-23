# we can encapsulate functionality like this
def cube(x):
    ''' NB triple quotes allow MULTI-LINE STRINGS
    This is a docstring - an opportunity to explain the purpose of the function
    Here we return the cube of a single given argument
    '''
    return x**3

# we can return the hypotenuse given x and y
def pythag(x=3, y=4): # these are positional arguments with default values
    return (x*x + y*y)**0.5

def myKwargs( **kwargs ): # any keyword-arguments will exist in a dict
    print(kwargs)

# we can access the arguments of any function
def myArgs( *args ): # any positional arguments will exist in a tuple (zero or more)
    # the args collection will have ALL the arguments of this function
    for item in args:
        print( item )
    print( type(args), args[3] )

# by convention, we do the following....
if __name__ == '__main__':
    print(cube(3))
    print(cube(2))
    print(cube(8765))
    # hyportenuse of a 3-4 triangle (5)
    print( pythag(3, 4) ) # 5 - these are positional arguments
    print( pythag(y=30, x=40) ) # 50 - NB these are NAMED arguments
    print( pythag() ) # no arguments provided, so use the defaults

    myArgs( 0, True, 'wow thats cool', [4,3,2] ) # these are positional arguments - a Tuple

    myKwargs( name='Ada', age=56, l=[7,6,5], isAdmin=False )