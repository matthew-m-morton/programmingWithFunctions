"""
Write a Python program named discount.py that gets a customer's subtotal 
as input and gets the current day of the week from your computer's 
operating system. Your program must not ask the user to enter the day of the 
week. Instead, it must get the day of the week from your computer's operating system.

If the subtotal is $50 or greater and today is Tuesday or Wednesday, 
your program must subtract 10% from the subtotal. Your program must then compute 
the total amount due by adding sales tax of 6% to the subtotal. Your program must 
print the discount amount if applicable, the sales tax amount, and the total amount due.

Core Requirements

Your program asks the user for the subtotal but does not ask the user for the 
day of the week. Your program gets the day of the week from your computer's operating system.
Your program correctly computes and prints the discount amount if applicable.
Your program correctly computes and prints the sales tax amount and the total amount due.
"""

from datetime import datetime

subtotal = float(input('Please enter your subtotal? '))
discountamount = 0
amountneeded = 0
total = 0
salestax = total * .06

day_of_week = datetime.now().weekday()
print (day_of_week)


#day logic
if day_of_week == 1 or day_of_week == 2: 
    if subtotal < 50:
        amountneeded = 50 - subtotal
        print(f'If you spend {amountneeded}$ you will be eligible for a 10% discount.')  

    else:
        discountamount = subtotal * .1     
        total = subtotal - discountamount

        print(f'Discount amount: {discountamount}$') 

        print(f'Total: {total}')

