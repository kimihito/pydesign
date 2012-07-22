#!/usr/bin/env python
# coding: utf-8
class Pond(object):
    def __init__(self, number_ducks):
        self.ducks = []
        for i in xrange(number_ducks):
            self.ducks.append(Duck("アヒル%d"%(i)))
            #ここでDuckを作っている

    def simulate_one_day(self):
        for duck in self.ducks:
            duck.eat()
            duck.speak()
            duck.sleep()

class Duck(object):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("アヒル(%s)は食事をしています" %(self.name,))

    def speak(self):
        print("アヒル(%s)はガーガー鳴いています"%(self.name,))

    def sleep(self):
        print("アヒル(%s)は寝ています"%(self.name,))
