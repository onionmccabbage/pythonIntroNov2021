# we can override any lf the built in methods of Python
# built-in methods include =, ==, +, -, /, * etc.

class Word():
    '''
    This class compares words regardless of case
    e.g. hello == Hello should be True
    '''
    def __init__(self, text):
        self.text = text
    def __eq__(self, other_word): # override the built-in __eq__ (for ==)
        return self.text.lower() == other_word.text.lower()

# use with great care!!!!!!
# __ne__ not equal
# __gt__ greater than
# __lt__ less than
# __ge__ and __le__ greater-or-equal and less-or-equal

# other 'magic methods'
# __add__( self, other ) self + other
# __sub__( self, other ) self - other
# __mul__( self, other ) self * other
# __floordiv__( self, other ) self // other
# __truediv__( self, other ) self / other
# __mod__( self, other ) self % other
# __pow__( self, other ) self ** other
# __len__ is the length of the object

if __name__ == '__main__':
    w1 = Word('hello')
    w2 = Word('Hello')
    print( w1 == w2 ) # True