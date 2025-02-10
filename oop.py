# object oriented programming
class Person:
    def __init__(self, name, age):
        #this is a constructor method
        # it takes two parameter and initialize as attributes
        self.name = name
        self.age = age
    def myfunc(self):
        print(f"hello my name is {self.name} and age is {self.age}")
        # this is a method function
# create an object or an instance of a class
myobj = Person("Imani", 18)
myobj.myfunc()
myobj2 = Person("Sally", 15)
myobj2.myfunc()
myobj3 = Person("Maureen", 54)
myobj3.myfunc()
myobj4 = Person("Ishmael", 24)
myobj4.myfunc()
myobj5 = Person("talisha", 10)
myobj5.myfunc()