''' 
    A funky fresh tipping calculator.
    Created by Annie and Aaron Wormus 1/11/2021
'''

def main():

    # Welcome statements
    print("Welcome")
    print("Enter your total bill (the price before any discounts or promo's, don't be a jackass) : ")
    total = int(input())

    # Method calls
    twenty = twenty_percent_tip(total)
    even = even_number_tip(total, twenty)
    palindrome = palindrome_tip(total, twenty)
    repeat = repeating_tip(total, twenty)

    print_it(twenty, even, palindrome, repeat)

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
    return 1

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

# Prints calculated tips
    '''
        Variables: 
                predefined
        Returns: 
                *NONE*
    '''
def print_it(twenty, even, palindrome, repeat):
    print("The service sucked, but I'm still a decent human being: ", twenty ," (20%)")
    print("Round it out: ", even)
    print("Front to back: ",  palindrome)
    print("Did I stutter?: ", repeat)

main()