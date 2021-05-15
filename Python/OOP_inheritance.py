## inheritance
## CASE: you have two class is too similar

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what to say")

class Cat(Pet):
    def __init__(self,name,age,color):
        # super() will use the Pet 's __init__ function
        super().__init__(name,age)
        self.color = color
    
    def speak(self):
        print("Meowww")
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")


class Dog(Pet):
    def speak(self):
        print("Bark Bark")

p = Pet("pet",19)
p.show()
p.speak()

c = Cat("cat",10,"Yellow")
c.show()
c.speak()

d = Dog("doggie",2)
d.show()
d.speak()


