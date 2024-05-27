from pypdf import PdfReader
from pypdf import PdfWriter

'''
1.	Write a Python program that provides the ability to: 
1.1.	Merge at least two PDF files into one. Use list data structure with at least two PDF files. As an optional bonus you can create an empty list and ask for user input to populate empty list with user defined PDF files.
1.2.	Rotate a page in PDF file.
1.3.	Encrypt PDF file.
1.4.	Decrypt PDF file.

'''
#----------------------------- FUNCTIONS ----------------------------
#Merging the pdf files
def merge_pdfs():


    input1 = open('Invoice31.pdf', 'rb')
    input2 = open('invoice32.pdf', 'rb')

    
    pdf_files = [input1, input2]
    merger = PdfWriter()

    for pdf in pdf_files:
        merger.append(pdf)

    merger.write('all_invoices_merged.pdf')
    merger.close()

    reader =PdfReader('merged.pdf')
    num_pages = len(reader.pages)
    for num in range(num_pages):
        page = reader.pages[num]
        text = page.extract_text()
        print(f'------------------------------- PAGE {num+1}-----------------------------')
        print(text,'\n')

        
#----------------------------------------------------------------
#rotation of a page in a pdf file
def rotate_pdf():


    file = open('rotation.pdf','br')
    
    

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

#------------------------------------------------------------------------

#1.1 Merge at least two PDF files into one. Use list data structure with at least two PDF files.
#    As an optional bonus you can create an empty list and ask for user input to populate empty 
#    list with user defined PDF files.

# open the pdf file in binary mode = 'br' and write the file to pdf_file_obj1 
with open('Invoice31.pdf', 'rb') as pdf_file_obj1:


    #Initialize the pdf reader object to read the PDF file
    pdf_file_obj1 = PdfReader(pdf_file_obj1)
    
    #Access the first page of the pdf file
    firstPage = pdf_file_obj1.pages[0]
    #assign the extracted text to text variable
    text1 =firstPage.extract_text() 
    #print(text1)




with open('Invoice32.pdf', 'rb') as pdf_file_obj2:

    #Initialize the pdf reader object to read the PDF file
    pdf_file_obj2 = PdfReader(pdf_file_obj2)
    
    #Access the first page of the pdf file
    firstPage = pdf_file_obj2.pages[0]
    #assign the extracted text to text variable
    text2 =firstPage.extract_text() 
    #print(text2)



#creation of the 
#list_pdf = [text1, text2]

#for i in range(len(list_pdf)):
    #print(list_pdf[i])




'''---------------------------------MAIN-------------------------------'''

menu()