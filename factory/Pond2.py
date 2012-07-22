#!/usr/bin/env python
# coding: utf-8
class Pond(object):
    def __init__(self, number_animals):
        self.animals = []
        for i in xrange(number_animals):
            animal = self.new_animal("動物%d"%(i,))
            self.animals.append(animal)

    def simulate_one_day(self):
        for animal in self.animals:
            animal.eat()
            animal.speak()
            animal.sleep()

    def new_animal(self, name):
        raise NotImplementedError

class FrogPond(Pond):
    """カエルだらけの池"""
    def new_animal(self,name):
        return Frog(name)

class DuckPond(Pond):
    """アヒルだらけの池"""
    def new_animal(self, name):
        return Duck(name)
