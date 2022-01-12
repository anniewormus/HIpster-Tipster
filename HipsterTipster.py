''' 
    A funky fresh tipping calculator.
    Created by Annie and Aaron Wormus 1/11/2021
'''

# Imports
import math

def main():

    # Welcome statements
    print("Welcome")
    print("Enter your total bill (the price before any discounts or promo's, don't be a jackass) : ")
    total = float(input())

    # Method calls
    twenty = twenty_percent_tip(total)
    even = even_number_tip(total, twenty)
    palindrome = palindrome_tip(total, twenty)
    repeat = repeating_tip(total, twenty)

    print_it(total, twenty, even, palindrome, repeat)

# Calculates 20% of the bill
    '''
        Variables: 
                total - the total bill entered by user
                tip - 20% of the total bill
        Returns: 
                tip
    '''
def twenty_percent_tip(total):
    tip = total * .20
    return tip

# Calculates the closest even number with a tip greater than 20% of the total
    '''
        Variables: 
                total - the total bill entered by user
                twenty - 20% of the total bill
        Returns: 
                tip
    '''
def even_number_tip(total, twenty):
    baseline = twenty+total
    baseline = math.ceil(baseline)

    return baseline

# Calculates the closest palindrome with a tip greater than 20% of the total
    '''
        Variables: 
                total - the total bill entered by user
                twenty - 20% of the total bill
        Returns: 
                tip
    '''
def palindrome_tip(total, twenty):
    return 1

# Calculates the closest repdigit with a tip greater than 20% of the total
    '''
        Variables: 
                total - the total bill entered by user
                twenty - 20% of the total bill
        Returns: 
                tip
    '''
def repeating_tip(total, twenty):
    return 1

# Formats the number to 2 decimal places
    '''
        Variables: 
                x - number to be formatted
        Returns: 
                formatted_val
    '''
def format(x):
    formatted_val = '{:.2f}'.format(x)
    return float(formatted_val)

# Prints calculated tips
    '''
        Variables: 
                predefined
        Returns: 
                *NONE*
    '''
def print_it(total, twenty, even, palindrome, repeat):
    print("The service sucked, but I'm still a decent human being")
    print_tip_total(twenty, twenty+total)

    print("Round it out: ")
    print_tip_total(even-total, even)

    print("Front to back: ")
    print_tip_total(0, 0)

    print("Did I stutter?: ")
    print_tip_total(0, 0)

def print_tip_total(tip, total):

    # Formats numbers
    format_tip = format(tip)
    format_total = format(total)

    print("\t\tTip: $", format_tip)
    print("\t\tTotal: $", format_total)

# Calls main
main()