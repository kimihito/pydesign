#!/usr/bin/env python
# coding: utf-8
class Pond(object):
    def __init__(self, number_animals, number_plants):
        self.animals = []
        for i in xrange(number_animals):
            animal = self.new_animal("動物%d"%(i,))
            self.animals.append(animal)

        self.plants = []
        for i in xrange(number_plants):
            plant = self.new_plant("植物%d"%(i,))
            self.plants.append(plant)

class DuckWaterLilyPond(Pond):
    #ここにメソッドを定義

class FrogAlgaePond(Pond):
    #ここにメソッドを定義
