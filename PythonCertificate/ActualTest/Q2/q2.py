#!/bin/python3

class Car:
    def __init__(self, max_speed, unit):
        self.max_speed = max_speed
        self.unit = unit
        print("Car with the maximum speed of {} {}".format(self.max_speed, self.unit))

if __name__ == '__main__':
    car = Car(120, "mph")
