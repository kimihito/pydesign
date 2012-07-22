#!/usr/bin/env python
# coding: utf-8
class Pond(object):
    def __init__(self, number_animals, animal_class, number_plants, plant_class):
        self.animal_class = animal_class
        self.plant_class = plant_class

        self.animals = []
        for i in xrange(number_animals):
            animal = self.new_organism("animal","動物%d"%(i,))
            self.animals.append(animal)

        self.plants = []
        for i in xrange(number_plants):
            plant = self.new_organism("plant", "植物%d"%(i,))
            self.plants.append(plant)

    def new_organism(self, type, name):
        if type == "plant":
            return self.plant_class(name)
        elif type == "animal":
            return self.animal_class(name)
        else:
            assert False, "wrong organism type %r"%(type,)

pond = Pond(10, Frog, 5, Algae)
print pond.simulate_one_day()
