import math


#promt user for number of items and how many items fit in a box
items = int(input('Enter the numberof items: '))
box_size = int(input('Enter the number of items per box: '))


#calculations
boxes_needed = math.ceil(items/box_size)


#output
print (f'\nFor {items} items, packing {box_size} items in each box, you will need {boxes_needed} boxes.\n')