
from pypdf import PdfWriter, PdfReader
import os
import tkinter as tk
from tkinter import filedialog

#----------------------------- FUNCTIONS ----------------------------
#Merging the pdf files

def select_file():
    try:
        root = tk.Tk()
        root.withdraw()  # Hides the small tkinter window
        file_path = filedialog.askopenfilename()  # Opens the file dialog prompt
        if not file_path:  # Check if the file selection was cancelled
            print("File selection cancelled.")
            return None
        return file_path
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def merge_pdfs():

    input1 = select_file()
    input2 = select_file()

    
    pdf_files = [input1, input2]
    merger = PdfWriter()

    for pdf in pdf_files:
        merger.append(pdf)

    new_pdf = input('What will be the name of the new PDF: ')


    merger.write(new_pdf +'.pdf')
    merger.close()
    
    
    

#----------------------------------------------------------------
#rotation of a page in a pdf file
def rotate_pdf():

    pdf_file = open('all_merged_files.pdf', 'rb')
    reader = PdfReader(pdf_file) 
    writer = PdfWriter() 

    how_many=reader.get_num_pages()
    print(how_many)
    
    for pagenum in range(reader.get_num_pages()):
        page = reader.get_page(pagenum)
        page.rotate(90)
        writer.add_page(page)
    

    pdf_out = open('rotation.pdf', 'wb')
    writer.write(pdf_out)
    pdf_out.close()
    pdf_file.close()


def encrypt_pdf():

    pdf_file =open('mobile.pdf', 'rb')

    reader = PdfReader(pdf_file)
    writer = PdfWriter(clone_from=reader)

# Add a password to the new PDF
    writer.encrypt("Password1", algorithm="AES-256")

# Save the new PDF to a file
    with open("encrypted-pdf.pdf", "wb") as file:
        writer.write(file)


def decrypt_pdf():
    
    reader = PdfReader("encrypted-pdf.pdf")

    if reader.is_encrypted:
        reader.decrypt("Password1")

    writer = PdfWriter(clone_from=reader)

    # Save the new PDF to a file
    with open("decrypted-pdf.pdf", "wb") as file:
        writer.write(file)
        

#----------------------------------------------------------------

def display_menu():
    
    print('##############################################')
    print('             PDF File Manager MENU           ')
    print('\n1. Merge PDFs.')
    print('2. Rotate PDF.')
    print('3. Encrypt PDF.')
    print('4. Decrypt PDF.')
    print('5. Exit.')
    

#--------------------------------------------------------------------------
def user_choice():
    while True:
        try:
            choice = int(input('Enter your choice (1-5): '))
            if  choice < 1 or choice > 5:
                print('Invalid input. Please try again (1-5).')
                raise ValueError('Invalid choice')
            else:
                return choice
        except ValueError:
            print('Invalid input. Please try again (1-5).')

#--------------------------------------------------------------------------
def menu():
    while True:
        #print the menu
        display_menu()
        choice=user_choice()

        if choice == 1:
            merge_pdfs()
        elif choice == 2:
            rotate_pdf()
        elif choice == 3:
            encrypt_pdf()
        elif choice == 4:
            decrypt_pdf()
        elif choice == 5:
            print('Exiting the program. Goodbye!')
            break

#----------------------------------------------------------------



'''---------------------------------MAIN-------------------------------'''

menu()