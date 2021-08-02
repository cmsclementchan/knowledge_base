# static method
# class attribute
# class method

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


p1 = Person("Clement")

p2 = Person("Tim")
print(Person.number_of_people_())

