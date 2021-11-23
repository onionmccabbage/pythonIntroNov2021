# import
import requests
from random import randint

# using 'in'
t = ('posts', 'albums', 'photos')
exist = 'users' in t
print(exist)

# iterate over a dict
d = {'name':'Grace Hopper', 'admin':False, 'address':['42', 'Primrose Av', 'Becknall']}
for k, v in d.items(): # careful - we want each item in the dict
    if(type(v)==list): # list is a data-type
        # iterate over the list
        for item in d[k]:
            print( '\t{}'.format(item) ) # \n for new line, \t for tab
    else:
        print(k, v)
        

