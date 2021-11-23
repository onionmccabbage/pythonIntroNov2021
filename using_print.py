# we can use print formating with any print output or string

def prettyPrint(t=12, d='sunny', s=6.7):
    # the positions are either defaults or numerically specified
    s = 'The weather is {0} with a wind speed of {1:0.2f} at {2} degrees celcius'.format(d, s, t)
    print( s )

if __name__ == '__main__':
    prettyPrint()
    prettyPrint(-2, 'freezing', 32.345678) # override defaults
