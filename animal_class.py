# Define our Animal class

class Animal:
    def __init__(self, name, age, colour, heart, brain):
        self.name = name
        self.age = age
        self.colour = colour
        self.heart = heart
        self.brain = brain

    def eat(self):
        return "Yum"

    def sleep(self):
        return "Zzz"

    def reproduce(self):
        return "I'm gonna need some privacy here..."

    def potty(self):
        return "0_0 HUMM!!! o_0 AHH! SPLOSH o_o"

    def make_sound(self):
        return "Woof"


# Create an object

ringo = Animal("Ringo", 12, 'Red', True, True)

# print object
print(ringo)
# print class
print(type(ringo))

# run methods
print(ringo.eat())
print(ringo.sleep())
print(ringo.reproduce())

# check attributes
print(ringo.name.capitalize())
print(ringo.age)
print(ringo.brain)
