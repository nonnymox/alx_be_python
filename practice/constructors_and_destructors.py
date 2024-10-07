# # Constructors and Destructors
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __del__(self):
#         print(f"Goodbye {self.name}!")
#
#     def __str__(self):
#         return f"{self.name} is {self.age} years old"
#
#
# emma = Person("Emmanuel", 27)
# print(emma)
# del emma

# Magic Methods (repr and str)
# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def __str__(self):
#         return f"The book title is '{self.title}' by {self.author} and contains {self.pages} pages"
#
#
# mocking_bird = Book("To Kill a Mocking Bird", "Harper Lee", 336)
# print(mocking_bird)
# Class Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name}: Eating the crap you call food bruv.")

    def sleep(self):
        print(f"{self.name}: Gotta nap now fam.")


class Dog(Animal):
    def bark(self):
        print(f"{self.name}: 'Woof Woof', Happy now?")


river = Animal("River")
river.eat()
river.sleep()
molly = Dog("Molly")
molly.bark()
molly.eat()
molly.sleep()
