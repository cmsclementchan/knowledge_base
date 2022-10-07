# static method
    # Flagging a method as a static method is not just a hint that a method won’t modify class or instance state — this restriction is also enforced by the Python runtime.
# class attribute
# class method
# reference : https://realpython.com/instance-class-and-static-methods-demystified/#class-methods



class Person:
    # class attribute
    number_of_people = 0 
    # constant for all 
    GRAVITY = -9.8

    def __init__(self, name):
        self.name = name
        Person.add_person()

    #not specific to the instance
    #instead of taking self, taking cls...
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

    @staticmethod
    def changing_principle():
        print("changing_principle")


p1 = Person("Clement")
p1.number_of_people = 4
print(p1.number_of_people)

p2 = Person("Tim")
print(Person.number_of_people_())

p2.changing_principle()
