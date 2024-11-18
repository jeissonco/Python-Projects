
"""
MP 4 
Leader Jeisson N
The Python application will be a mortgage calculator, 
which will allow the client to choose the length of the mortgage, interest rate, down payment.

Date: 13/11/2024
Author: Jeisson N & Eyerusalem Desalegn
"""

import math


#------------------------------Functions------------------------------------------------

def display_menu():
    # Display the main menu with available options.
    print('##############################################')
    print('             Mortgage Calculator           ')
    print('1. Provide the length of the mortgage, interest rate and down payment.')
    print('2. Exit.')
     

#--------------------------------------------------------------------------
def user_choice():
    # Get the user's choice and validate it to be between 1 and 2.
    while True:
        try:
            choice = int(input('Enter your choice (1-2): '))
            if  choice < 1 or choice > 2:
                print('Invalid input. Please try again (1-2).')
                raise ValueError('Invalid choice')
            else:
                return choice
        except ValueError:
            print('Invalid input. Please try again (1-2).')

#--------------------------------------------------------------------------
import math

def property_price():
    # Prompt the user to enter the property price, which should be greater than $100,000.
    while True:
        try:
            property_price = float(input('Enter Property Price: '))
            if property_price < 100000:
                print('Invalid input. Property should be higher than $100,000.')
            else:
                return math.ceil(property_price)
        except ValueError:
            print('Invalid input. Please enter a valid number.')

def mort_duration():
    # Prompt the user to enter the mortgage duration (in years), between 1 and 30.
    while True:
        try:
            duration = int(input('Enter the length of the mortgage (in years): '))
            if  duration < 1 or duration > 30:
                print('Invalid input. The mortgage duration should be between 1 and 30 years.')
            else:
                return duration
        except ValueError:
            print('Invalid input. Please enter a number.')
            

def interest_rate():
    # Prompt the user to enter the interest rate, which must be a positive number.
    while True:
        try:
            interest_rate = float(input('Enter the interest rate: '))
            if interest_rate < 0:
                print('Invalid input. Interest rate should be a positive number.')
            else:
                return interest_rate/100
        except ValueError:
            print('Invalid input. Please enter a number.')
            

def initial_payment():
    # Prompt the user to enter the down payment, which should be non-negative.
    while True:
        try:
            initial_payment = float(input('Enter the down payment: '))
            if initial_payment < 0:
                print('Invalid input. Down payment should be between 0 and the property price.')
            else:
                return math.ceil(initial_payment)
        except ValueError:
            print('Invalid input. Please enter a number.')

def calculate_monthly_payment(p, d, i, d_pay):
    # Calculate the monthly mortgage payment based on the provided parameters.

    # calculate the number of payments and the monthly interest rate
    number_payments = d * 12
    # calculate the interest rate monthly
    monthly_int_rate = i / 12
    # calculate the total amount to be paid after the down payment is subtracted from the price
    finance = p - d_pay

    # calculate the monthly mortgage payment using the formula
    mortgage = finance * ((monthly_int_rate * (1 + monthly_int_rate) ** number_payments) / ((1 + monthly_int_rate) ** number_payments - 1))

    return mortgage

def get_data():
    # Get data from the user: property price, duration, interest rate, and down payment.
    # Then calculate and display the monthly payment.
    price = property_price()
    duration = mort_duration()
    interest = interest_rate()
    down_payment = initial_payment()
    
    result = calculate_monthly_payment(price, duration, interest, down_payment)

    print("The monthly payment will be: ", round(result,2 ))
    print('\n')
#--------------------------------------------------------------------------

def menu():
    # Display the menu and handle user choice until the user decides to exit.
    while True:
        # print the menu
        display_menu()
        choice = user_choice()

        if choice == 1:
            get_data()
        elif choice == 2:
            print('Exiting the program. Goodbye!')
            break


"""----------------Deployment of the menu---------------"""
menu()
