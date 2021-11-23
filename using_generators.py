# a generator will generate values

def makeGen(max):
    g = (num for num in range(0, max)) # returns a generater object
    return g # return the generator object

def useGen(j):
    for i in j:
        print(i, end=', ') # we can optionaly end print with any character

# we can write custom generators
def myGen(start=1, stop_before=10, step=2): # start, stop-before, step for incremental multiples
    '''
    Generate increasing multiples of a range of numbers
    '''
    number = start
    while number < stop_before:
        yield number # yield will return the next value in the generated sequence
        number = number * step # same as number *= step

if __name__ == '__main__': # good practice
    n = makeGen(1000) # generates 0-999
    print(n) # we have a generator object
    # useGen(n) # prints all the generated values
    # make use of our custom generator
    r = myGen(stop_before=200)
    print(r) # it is a generator (because it has a 'yield' statement)
    for x in r: # we can only harvest members of a generator ONCE, then it is exhausted
        print(x, end=', ')