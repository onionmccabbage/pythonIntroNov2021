# here is a Python comment
a = 3 # an integer
b = 7

c = a/b # result is a float
c = b//a # returns 2 - integer part of division
c = b%a # 1 - the remainder

c = b**a # 343 is seven cubed
c = 'hello' # a string
print(c, type(c), type(a)) # the brackets are optional in Python 2

# python is restricted ONLY by resources available
g = 10**10000
# print(g)

# as well as simple data types we have collection data types (zero-based)
s = 'here is a string of characters'
print(s[10:15:2]) # start:stop-before:step
print(s[::-1]) # prints backwards!

# lists and tuples may contain ANY data types
l = [6, 5.2, 4, True, 'nearly coffee', c, (9,8,7)] # mutable list (uses square brackets)
# lists are great for receiving KPI or other historical data points
t = (8, 7, 6, l) # immutable tuple (uses round brackets)
t[3][0] = 99 # not mutating the tuple, but mutating the list within it!
l.append(-2)
l.remove(5.2)
# t[0] = 99 # NOOOOO! cannot be done

#            tuple count() will return number of occurrences of an item
print(l, t, type(l), type(t), t.count(8), len(t))

# can we remove members by index - answer after coffee
l.pop(3) # remove list item at index position 3
print(l)

# ask the user for a value
u = input('Please enter a number ') # input is ALWAYS a string!!!!!!!!!!!!!!
# print the type of the user input
print(type(u))# always a string!!
# we can cast to a data type
i = int(float(u)) # ALWAYS make a float first, just in case!!
print(i, type(i))

# Boolean True and False (Python initial caps)
# (there is also a None type)
print(''  == None) # False
u = None # u now refers to NO data type
print( [] == False) # no, False
print( 0  == False) # yes, it is True to say that zero is equivalent to False