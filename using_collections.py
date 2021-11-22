# we can use list, tuple, dictionary and set collections
# a dict is a non-indexed collection. More like a hash
d = {"name":'Timnit', 'age':42, 'member':True}
print(d['name']) # access keys using square-bracket syntax
d['age'] = 53
d['status'] = 'admin'
print(d) # careful the members may not be in the order of creation
print(d.keys(), d.values(), type(d))

# alternative creation syntax (actually casting to another data type)
l = list( (4,3,2) ) # make a list out of a tuple
# or
l = [4,3,2]
# or
l = list( [4,3,2] )


t = tuple(l)
d = dict()
d['item'] = 'frog'
print(l, t, d, type(t))

# careful....
q = (5,) # what is this.... the comma means it will be a tuple
print(type(q))

# a set is like a dict with no keys (and unique members)
s = {7,6,7,5,4} # NOT an indexed collection
s.add(3)
print(s, type(s))

# strings and characters
s = 'lunchtime'
print(type(s[0])) # char???