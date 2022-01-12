''' 
    A funky fresh tipping calculator.
    Created by Annie Wormus 1/11/2021
'''

''' 20% tip - they sucked but you're a decent human being
    round up even - 
    palindrome number
    all same number
'''

def main():

    print("Welcome")
    print("Enter your total bill (the price before any discounts or promo's, don't be a jackass) : ")
    total = int(input())

    twenty = twenty_percent_tip(total)
    even = even_number_tip(total)
    palindrome = palindrome_tip(total)
    repeat = repeating_tip(total)

    print_it(twenty, even, palindrome, repeat)


def twenty_percent_tip(total):
    print("twenty percent")
    tip = total * .20
    return tip

def even_number_tip(total):
    print("even number")
    return 1

def palindrome_tip(total):
    print("palindrome")
    return 1

def repeating_tip(total):
    print("repeating number")
    return 1

# def percentage(tipAmount):
#     print("tip amount")

def print_it(twenty, even, palindrome, repeat):
    print("The service sucked, but I'm still a decent human being: " + twenty + " (20%)")
    print("Round it out: " + even)
    print("Front to back: " + palindrome)
    print("Did I stutter?: " + repeat)

main()