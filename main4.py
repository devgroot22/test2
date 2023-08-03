from main3 import Person


import random
import abc


class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print(f"Object is being deconstructed!")


print(random.randint(1, 10))
p = Person("Mike", 25)
del p
