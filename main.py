# import package.module
import utility.furniture as furn
from utility.accountancy import table #this is all 'name-spacing'
import explore
# we can import modules from the python standard library
import random # useful for random values
import math   # sin, cos, sqrt etc.
# we can also use libraries that are not part of python
# (but first we must use pip to install them)
import requests # fails unless we have already isntalled the 'requests' library

# there is always a 'global' namespace for each module
g = 'this is the global namespace, outside any function'

def main():
    # make use of our global assets
    global g # we tend to avoid using globals
    g = 'altered'
    # make both tables
    f = furn.table(40, 80)
    #   package.module
    a = table(3,7) # we already imported this from utility.accountancy
    return [f, a]

if __name__ == '__main__':
    # only THIS module code will run
    print( main() )
    print(g)