class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("Goodbye!")

    def __str__(self):
        return f"{self.name} is {self.age} years old"



emma = Person("Emmanuel", 27)
# print(emma)
del(emma)