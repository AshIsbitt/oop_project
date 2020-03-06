from animal_class import Animal


class Reptile(Animal):

    def __init__(self, name, age, colour, heart, brain, scales, blood):
        super().__init__(name, age, colour, heart, brain)
        self.scales = scales
        self.blood = blood

    def make_sound(self):
        return 'ssssss'

    def prey(self):
        return "Mmm. Dinner"

    def seek_sun(self):
        return "Warmth"

    def seek_shade(self):
        return "Cool"


animal1 = Animal("Ringo", 12, 'Red', True, True)
reptile = Reptile("Tom", 15, 'Green', True, True, True, "cold")

print(reptile.scales)
print(reptile.age)