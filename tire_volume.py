import math
from datetime import datetime

#variable declarations
date = datetime.now()
number = 0

#data collections
width = float(input('Enter the width of the tire in mm (ex 205): '))
aspectRatio = float(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = float(input('Enter the diameter of the tire in inches (ex 15): '))

#calculations
volume = (math.pi * (width**2) * aspectRatio * (width * aspectRatio + (2540*diameter))) / 10000000000

#results
print(f'The approximate volume is {volume:.02f} liters')

#followup question
newTires = input('Would you like to purchase a set of new tires (yes/no)? ')

if newTires.lower() == 'yes':
    number = input('What is your phone number? ')

#record data to volumes.txt file
with open("volumes.txt", "at") as volumes:
    print(f'{date:%Y-%m-%d}, {width:.00f}, {aspectRatio:.00f}, {diameter:.00f}, {volume:.02f}', file=volumes)
    if newTires.lower() == 'yes':
        print(f'Phone number: {number}', file = volumes)