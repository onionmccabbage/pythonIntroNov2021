# a class can capture aspects of reality
# e.g. a person has a name, age, email...
# all classes implicitly inherit from the object class 
class Person(): # self represents this class
    '''
    Explain your class in a docstring like this
    This class declares a 'Person' 
    Parameters: name, age, email
    'age' must be a positive integer
    '''
    def __init__(self, name, age, email): # this is like a constructor
        self.__name = name # we use double-underscore to 'mangle' the name, preventing direct access to it
        self.setAge(age) # make use of our setter
        self.__email = email
    # we can override the default __str__ method, which is used by the print statement
    def __str__(self): # all methods of a class MUST take self as first parameter
        return  '{} age {} email {}'.format(self.__name, self.getAge(), self.__email )
    # we can declare getter and setter methods to access class members
    def getAge(self):
        return self.__age
    def setAge(self, new_age):
        if int(float(new_age)) > 0:
        # if  ( type(new_age)==int and new_age>0 ) or new_age.isnumeric() : # isnumeric() checks it cntains ONLY digits
            self.__age = new_age
        else:
            self.__age = 32 # sensible default

class Thing(): # we can declare multiple classes in one module
    pass

if __name__ == '__main__':
    Ada = Person('Ada', -99, 'ada@babbage.ie')
    Ada.age = -99 # validate against this - use name mangling - this line fails silently
    print(Ada.age) # we have created a NEW arbitrary property, tis is NOT the internal __age
    # print(Ada.name, Ada.age, Ada.email)
    print(Ada)
    print(Ada.__doc__) # print the docstring