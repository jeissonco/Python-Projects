# @Autor: Jeisson Nino
#   v1. building the menu and first functions                                    18/03/2025
#   v2. returning the info gathered from function add_student                    24/03/2025
#   v3. corrections of the try and exception cases in the function add_student, inclussion of the    26/03/2025
#       regular expression library to handle the user's input
#   v4.Add student option and view student functions completed                    26/03/2025
#   v5. correcting the logic of the question that asks to return to menu          31/03/2025
#   v6. Final review and adjust the remove function                                14/04/2025

# ASS1 fundamentals of programming 

#-------------------LIBRARIES----------------
import os
import re
from sys import exit
#import tkinter as tk


#-----------------------------------FUNCTIONS--------------------------------
#This function clears up the terminal for better user experience
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

#----------------------------------------------------------------------------
#This function printes the menu of the program
def display_menu():
    print('#########################################################')
    print('             KAPLAN Student Management System           ')
    print('\n1. Add Student.')
    print('2. Remove Student.')
    print('3. View Students.')
    print('4. Exit.')
#----------------------------------------------------------------------------
# try and exception handler for the user inputs
def user_choice():
    while True:
        try:
            choice = int(input('Enter your choice (1-4): '))
            
            if  choice < 1 or choice > 5:
                raise ValueError
            else:
                return choice
            #if the error was raise, it'll print this message and then the display menu
        except ValueError:
            clear_console()
            print('Invalid input. Please try again (1-4).')
            display_menu()



#----------------------------------------------------------------
#This function verifies that the name entered is in valid format
def valid_name():

    while True:
        try:
            name = input("Enter the student name: ")
            #Here I use the regular expression library to check if the student name is valid
            """
            name should match any of the criteria defined in the function below
            A-Z ---> is to check any capital letters from A to Z
            a-z ---> is to check any lower letters from a to z
            s ----> is to allow spaces between characters
            + ---> indicates that is has to be at least 1 character
            """
            if not re.match(r"^[A-Za-z\s]+$", name):
                raise ValueError("Invalid student name, only Letters and spaces allowed.")
        #if the student name is valid 
            break 
        except ValueError:
            print("Please enter a valid student name ")
            
    
    return name.title()

#----------------------------------------------------------------
def valid_subject():
    while True:
        try:
            subject = input("Enter the subject: ")
            #0-9 will match numbers in the user's input 
            #Ex: TECH1200 will be a valid input for the variable
            if not re.match(r"^[A-Za-z0-9\s]+$", subject):
                raise ValueError("Invalid option, only Letters and spaces allowed.")
        #if the option is valid 
            break 
        except ValueError:
            print("Please enter a valid option")

        #asking for more subjects to add if the user wants

        

    return subject.upper()

def valid_grade():
    while True:
        try:
            grade = float(input("Enter the grade: "))
            #0-9 will match numbers in the user's input 
            #Ex: TECH1200 will be a valid input for the variable
            if grade < 0 or grade > 100:
                raise ValueError("Invalid option, grade must be 0-100.")
        #if the option is valid 
            break 
        except ValueError:
            print("Please enter a valid option")

        #asking for more subjects to add if the user wants

        

    return grade
#----------------------------------------------------------------
def add_student(student_data):

    while True:
        clear_console()

        #Here I start the information gathering, validating a correct input for the name of the student
        student_name = valid_name()
        # add the student name into the dictionary

        #if the student name is not in the dictionary it will be added to it
        if student_name not in student_data: 
            student_data[student_name] = {}


        while True:
            # Now I will gather information about the subjects that the student is enrolled into and validate a correct input
            student_class = valid_subject()

            # if the class/subject is not in the dictionary it will be added to it  
            if student_class not in student_data[student_name]:
                student_data[student_name][student_class] = {}

                
                #Adding the grade of the class/subject to the student 
                while True:
                    grade = valid_grade()
                    student_data[student_name][student_class] = grade
                    break
                    
            
        
            while True:
                try:
                    check_point = input(f'Do you want to add another subject for the student {student_name} ? (y/n): ').lower()
                    #Verify if checkpoint is not either 'n' or 'y' options and raise the error  
                    if check_point not in ('n', 'y'):
                        raise ValueError
                    break        
                except ValueError :
                    print("Please enter a valid option")
                
                
            
            if check_point == 'y':
                continue
            break

        # Checkpoint to verify the student was added successfully
        print("---------------------------------------------")
        print(f'Current list of students:\n {student_data}')


        
        while True:
            try:
                check_point = input("Do you want to add another student? (y/n): ").lower()
                #Verify if checkpoint is not either 'n' or 'y' options and raise the error 

                clear_console()
                if check_point not in ('n', 'y'):
                    raise ValueError
                break
            except ValueError :
                print("Please enter a valid option")
        
        

        #this will finish the addition of students by breaking the original loop
        if check_point == 'n':
            break
    return student_data

#----------------------------------------------------------------------------
def rm_student(student_data):
    
    while True:
        clear_console()
        print("*************** REMOVING/DELETING STUDENT ********************\n")
        selected_student = valid_name()

        if selected_student in student_data:
            del student_data[selected_student]
            print(f'The student: {selected_student} was deleted successfully')

        elif selected_student not in student_data:
            print(f'Student: {selected_student} not found')
        
        while True:
            try:
                choice = input("Do you want to delete another student? (y/n): ").lower()
                #Verify if checkpoint is not either 'n' or 'y' options and raise the error      
                if choice not in ('n', 'y'):
                    raise ValueError
                elif choice == 'y': #if true, this breaks out the try/except inner loop to restart the outer loop
                    clear_console()
                    break 
                elif choice == 'n':#if true, it breaks out the iner loop to exit the entire function
                    clear_console()
                    break
            except ValueError :
                print("Please enter a valid option")     
        if choice == 'n':   
            break
        
        
    while True:
        try:
            check_point = input("Do you want return to the menu? (y/n): ").lower()
            
            #This will finish the program, since the user decided to not return to the menu again
            if check_point == 'n':
                exit()

            clear_console()
            #Verify if checkpoint is not either 'n' or 'y' options and raise the error 
            if check_point not in ('n', 'y'):
                raise ValueError
            break
        except ValueError :
            print("Please enter a valid option")

        
        return student_data


#----------------------------------------------------------------------------

def view_students(student_data):

    print("------------------------------------------------------------")
    print('Current list of students:')

    # itirates the dictionary and prints the list of students
    for key, value in student_data.items():
        for subject, grade in value.items():
            if  grade >= 85 and grade <=100:
                grade = 'HD'
            elif grade >=75 and grade <=84:
                grade = 'D'
            elif grade >= 65 and grade <=74:
                grade = 'C'
            elif grade >= 50 and grade <=64:
                grade = 'P'
            else:
                grade = 'F'
            print(f'- {key}: {subject} --> {grade}')

    while True:
        try:
            check_point = input("Do you want return to the menu? (y/n): ").lower()
            
            #This will finish the program, since the user decided to not return to the menu again
            if check_point == 'n':
                exit()
            clear_console()

            #Verify if checkpoint is not either 'n' or 'y' options and raise the error 
            if check_point not in ('n', 'y'):
                raise ValueError
            break
               
        except ValueError :
            print("Please enter a valid option")
                
        


#------------------------------------------------------------------------
#----------------------MAIN---------------------------------------

#data_base = {}

#This dictionary was added for testing purposes if needed comment the data_base={} 
# variable and work with the following one

data_base = {'Jeisson Nino': {'TECH1100' : 90, 'TECH1200' : 67}, 'Daniel Diaz': {'TECH1300' : 88, 'TECH1100' : 79}}

while True:
        #print the menu
        display_menu()
        choice=user_choice()
        if choice == 1:
            add_student(data_base)
        elif choice == 2:
            rm_student(data_base)
        elif choice == 3:
            view_students(data_base)

        elif choice == 4:
            print('Exiting the program. Goodbye!')
            break




