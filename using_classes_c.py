# in modern Python we can use decorators
# imagine an 'Album' class with id, title and content

class Album(object): # no need to write object, it is the default!!
    def __init__(self, id, title, content):
        self.__id      = id # call the setter method
        self.__title   = title
        self.__content = content
    # here we use 'decorator' syntax for our getter and setter methods
    @property # this is a built-in decorator
    def id(self): # this is the getter
        return self.__id
    @id.setter
    def id(self, new_id): # this is the setter
        if int(float(new_id)) > 0:
            self.__id = new_id
        else:
            raise Exception # we could define our own Exception 
    @property # this is a built-in decorator
    def title(self): # this is the getter
        return self.__title
    @title.setter
    def title(self, new_title): # this is the setter
        if new_title !='':
            self.__title = new_title
        else:
            raise Exception # we could define our own Exception 
    @property # this is a built-in decorator
    def content(self): # this is the getter
        return self.__content
    @content.setter
    def content(self, new_content): # this is the setter
        if new_content !='':
            self.__content = new_content
        else:
            raise Exception # we could define our own Exception 
    def __str__(self): # override the print method
        return '{} {} {}'.format(self.id, self.title, self.content)


if __name__ == '__main__':
    a = Album(1, 'Lunches I have known', 'Cucumber Sandwiches with Juice')
    print(a)
