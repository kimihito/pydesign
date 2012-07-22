#!/usr/bin/env python
# coding: utf-8
class Habitat(object):
    def __init__(self, number_animals, number_plants, organism_factory):
        self.animals = []
        for i in xrange(number_animals):
            animal = organism_factory.new_animal("動物%d"%(i,))
            self.animals.append(animal)

        self.plants = []
        for i in xrange(number_plants):
            plant = organism_factory.new_planti("植物%d"%(i,))
            self.plants.append(plant)

class JunggleOrganismFactory(object):
    def new_animal(self, name):
        return Tiger(name)

    def new_plant(self, name):
        return Tree(name)

class PondOrganismFactory(object):
    def new_animal(self, name):
        return Duck(name)

    def new_plant(self, name):
        return WaterLily(name)
