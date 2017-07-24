# Exercise 42: Is-A, Has-A, Objects and Classes

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## class Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Class Dog has-a __init__that takes self and name parameters
        self.name = name

## class Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## class Cat has-a __init__ that takes self and name parameters
        self.name = name

## class Person is-a object
class Person(object):

    def __init__(self, name):
        ## class Person has-a __init__ that takes self and name parameters
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## class Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## what is this strange magic?
        ## Return a proxy object that delegates method calls to a parent or sibling class of type.
        super(Employee, self).__init__(name)
        ## Employee has-a salary attribute
        self.salary = salary

## class Fish is-a object
class Fish(object):
    pass

## class Salmon is-a Fish
class Salmon(Fish):
    pass

## Class Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is a Cat
satan = Cat("Satan")

## mary is a Person
mary = Person("Mary")

## mary has-a pet which is-a satan=>pet attribute of mary is-a satan
mary.pet = satan

## frank is-an Employee + instance
frank = Employee("Frank", 120000)

## frank has-a pet which is-a rover->pet attribute of frank is-a rover
frank.pet = rover

## flipper is-a fish + instance
flipper = Fish()

## crouse is-a Salmon + instance
crouse = Salmon()

## harry is-a Halibut + instance
harry = Halibut()
