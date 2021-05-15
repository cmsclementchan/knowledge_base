# Object Orientated Programming
# In python, everything is Object! 

# you are creating a int object.
x = 1 

#
string = "hello"
print(string.upper())

## Class 
class Dog:
    # a special method()
    def __init__(self,name):
        self.name = name
        print(f'{name} is created!')
        pass

    def get_name(self):
        return self.name
    
    #method
    def add_one(self,x):
        return x+1

    def bark(self):
        print("bark!")

## instance of the Class 
d = Dog("Tim")
d.bark()
d.add_one(5)

## instance of the Class
d2 = Dog("Bill")
print(d2.get_name())


# default is __main__.instance
print(type(d))

