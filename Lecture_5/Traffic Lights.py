import random 
RED = 1
ORANGE = 2
GREEN = 3

options = """
1.Car
2.Fire Engine
3.Ambulance
4.Bike
5.Police 
"""
CAR = 1
FIRE_ENGINE = 2
AMBULANCE = 3
BIKE = 4
POLICE = 5

print(options)
traffic_light = random.randint(1,3)
vehicle = int(input("Enter a number from 1-5: "))
