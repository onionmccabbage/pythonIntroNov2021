# range and generators are very powerful tools in Python
# we can generate a list of values
num_l = [ num for num in range(0, 100, 3) ] # start, stop-before, step
print(num_l, type(num_l))

# we can also just use the generator as an object...
num_g = ( num for num in range(0, 100, 3) )
print(type(num_g)) # NOT a tuple

# we can iterate over a generator
for i in num_g:
    print(i, end=' ') # we can specify any end character for print!

print()

for i in num_g: # nope - the generator is exhausted!
    print(i)

# we often use a range to iterate (so the range numbers do not persist in memory)
r = 0
for j in range(1,10000):
    r += j

print(r)

# we can also iterate over a dict like this...
p = 'are we there yet?'
# this is called dictionary comprehension
chars = {letter: p.count(letter) for letter in p}
print(chars)

# mini challenge
# make a generator for all the odd numbers up to 100
odds = ( num for num in range(1, 100, 2)) # all the odd numbers!!
# or
odds = ( num for num in range(0, 100) if num%2 == 1 ) # all the odd numbers
for i in odds:
    print(i)