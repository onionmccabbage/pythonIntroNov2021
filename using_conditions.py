# logical conditions can branch decisions in code
# loops may run using 'for' or 'while'
# keep asking for a number until zero is entered
i = 99 # give i an initial value!
while i != 0: # pften called a run loop
    n = input('enter a number ')
    # validate the input
    if n.isnumeric(): # check if the string can be cast to an integer
        # ok - go ahead and cast as a number
        i = int(float(n))
        # check what was entered
        if i<0:
            print(i, 'is less than zero')
        elif i>0:
            print(i, 'is greater than zero')
        elif i==0: # double-equals to CHECK equality
            print(i, 'is zero')
            break # breaks out of a loop
        else:
            print(n, 'is not a number')



