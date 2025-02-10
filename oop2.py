# using create a class caller class that have following attribute model color yr of manufacturew
# inpliment
# cinstructor method and method function that prints (my favorite car model,it is this in color and manufacture
# in - yyea)
class Car:
    def __init__(self ,model,color, year,):
        self.color= color
        self.model = model
        self.year = year
    def myfunc(self):
        print(f"My favorite car model is {self.model},its is {self.color} in color"
              f" and manufactured in the year of {self.year}")
myobj = Car("Ford", "Red", 1999)
myobj.myfunc()
myobj2 = Car("McLaren", "White", 2010)
myobj2.myfunc()
myobj3 = Car("Volvo", "grey", 2006)
myobj3.myfunc()
myobj4 = Car("Maserati", "Green", 1995)
myobj4.myfunc()
myobj5 = Car("Alfa romeo", "Navy blue", 2020)
myobj5.myfunc()