# class Shape:
#     def __init__(self):
#         pass
#
#     def calculate_area(self):
#         pass
#
#
# class Rectangle(Shape):
#     def __init__(self):
#         super().__init__()
#
#     def calculate_area(self):
#         print("length times breadth")
#
#
# rect = Rectangle()
# rect.calculate_area()


# class Bird:
#     def __init__(self):
#         pass
#
#     def fly(self):
#         print("I am flying...")
#
#
# class Mammal:
#     def __init__(self):
#         pass
#
#     def run(self):
#         print("I am running now!")
#
#
# class Bat(Mammal, Bird):
#     def __init__(self):
#        pass
#
# ben = Bat()
# ben.run()
# ben.fly()

class Dog:
    def __init__(self):
        pass

    def make_sound(self):
        print("WOOF WOOF")


class Cat:
    def __init__(self):
        pass

    def make_sound(self):
        print("MEOW")


class Bird:
    def __init__(self):
        pass

    def make_sound(self):
        print("CHIRP CHIRP")


animals = [Dog(), Cat(), Bird()]


def let_them_speak():
    for animal in animals:
        animal.make_sound()


let_them_speak()
