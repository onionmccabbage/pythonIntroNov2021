from using_classes_a import Person # we need the Person class

class Coder(Person): # inherit from the Person class
    def __init__(self, name, age, email, language):
        super().__init__(name, age, email) # call parent clas
        self.__language = language # additional members
    def __str__(self):
        # return '{} age {} email {} language {}'.format(self.__name, self.getAge(), self.__email, self.__language )
        return '{} age {} language {}'.format(self._Person__name, self.getAge(), self.__language)

if __name__ == '__main__':
    c = Coder('Grace', 84, 'grace@nasa.com', 'Python')
    print(c)
    print(c._Coder__language) # direct access!!!!!!