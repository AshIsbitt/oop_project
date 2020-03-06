from animal_class import Animal


class Reptile(Animal):

    def make_sound(self):
        return 'ssssss'


animal1 = Animal("Ringo", 12, 'Red', True, True)
reptile = Reptile("Tom", 15, 'Green', True, True)
