# -*- coding: utf-8 -*-
"""
Created on Sun May  5 23:18:07 2024

@author: Jeisson Nino

"""

#-------------------- Creation of the linked list -----------------------
#Using linked lists to resolve the part A
class Node_of_list:
    def __init__(self,data):
        self.data=data  
        self.next_node=None 

class LinkedList:
    def __init__(self):
        # Initialize of the head node in the linked list
        self.first_node=None
        
#---------------------- Methods of the linked list asked in the Assessment Part A ----------------------------------

# Determine which type of list we are interested in:

# List of favourite actors/actresses

    def creation_of_list(self, option):

        favourite_actors = [
            "Meryl Streep",
            "Leonardo DiCaprio",
            "Viola Davis",
            "Tom Hanks",
            "Cate Blanchett",
            "Denzel Washington",
            "Natalie Portman",
            "Joaquin Phoenix",
            "Emma Stone",
            "Daniel Day-Lewis",
            "Lupita Nyong'o",
            "Robert Downey Jr."
        ]

        # List of favourite movies
        favourite_movies = [
            "The Shawshank Redemption",
            "Inception",
            "The Godfather",
            "Schindler's List",
            "Pulp Fiction",
            "The Dark Knight",
            "Forrest Gump",
            "Fight Club",
            "The Lord of the Rings: The Return of the King",
            "Titanic",
            "Gladiator",
            "The Matrix"
        ]

        # List of favourite games
        favourite_games = [
            "The Legend of Zelda: Breath of the Wild",
            "The Witcher 3: Wild Hunt",
            "Red Dead Redemption 2",
            "God of War (2018)",
            "The Last of Us",
            "Mass Effect 2",
            "Skyrim",
            "Portal 2",
            "Dark Souls",
            "Overwatch",
            "Minecraft",
            "Super Mario Odyssey"
        ]

        if option =='m':
            return favourite_movies
        elif option =='g':
            return favourite_games
        elif option =='a':
            return favourite_actors
    


# appending information to the linked list, adding new info to the list
    def append(self,data):
        new_node=Node_of_list(data)
        if not self.first_node:
            self.first_node = new_node
            return
        last_node = self.first_node
        
        while last_node.next_node:
            last_node = last_node.next_node
        last_node.next_node = new_node
        
#---------------------------------------------------------
        
#print all the information store in the linked list
    def print_list(self):
        current_node = self.first_node
        
        while current_node:
            
            print(current_node.data, end= ' | ')
            current_node = current_node.next_node
        print()
        
#---------------------------------------------------------       

#deletion function of a target in the list

    # this method marks the item=target we want to delete
    def delete(self, target):
        #temp_list=[]
        current = self.first_node  # Start with the head of the list
       
        while current: # Traverse the list
            if current.data == target: # Compare the list's data to the search value
                current.data = '99'    #this marks the data we want to delete
                #break
            current = current.next_node
            
            

    #This method will pass the list to a tmp list without the data marked as '99'     
    def tmp_list(self):
        temp_list = []
        current_node = self.first_node
        
        #print('before the loop')
        while current_node:
            
            if  current_node.data == '99':
                
                current_node = current_node.next_node
                continue
                
            else:
                temp_list.append(current_node.data)
                current_node = current_node.next_node
               

        return temp_list
    # This method remove nodes marked as '99'
    def refresh(self):
        
        current_node = self.first_node
        prev_node = None
        while current_node:
            if current_node.data == '99':
                if prev_node:
                    prev_node.next_node = current_node.next_node
                else:
                    self.first_node = current_node.next_node
            else:
                prev_node = current_node
            
            current_node = current_node.next_node
        
        


#---------------------------------------------------------

#searching function and display whats the positions of the data in the list
    
    def search(self, target):
        current = self.first_node  # Start with the head of the list
        position = 0  # Counter to keep track of the position
        while current: # Traverse the list
            if current.data == target: # Compare the list's data to the search value
                return f"Value '{target}' found at position {position}" # Print the value if a match is found
            current = current.next_node
            position += 1
        return f"Value '{target}' not found in the list" 
    
    

#-------------------------------------------------------------
    #Merge sort sorting
    
    def sortedMerge(self, a, b):
        result = None
        
        # Base cases
        if a == None:
            return b
        if b == None:
            return a
            
        # pick either a or b and recur
        if a.data <= b.data:
            result = a
            result.next_node = self.sortedMerge(a.next_node, b)
        else:
            result = b
            result.next_node = self.sortedMerge(a, b.next_node)
        return result
    
    def mergeSort(self, h):
        
        # Base case if head is None
        if h == None or h.next_node == None:
            return h

        # get the middle of the list 
        middle = self.getMiddle(h)
        nexttomiddle = middle.next_node

        # set the next of middle node to None
        middle.next_node = None

        # Apply mergeSort on left list 
        left = self.mergeSort(h)
        
        # Apply mergeSort on right list
        right = self.mergeSort(nexttomiddle)

        # Merge the left and right lists 
        sortedlist = self.sortedMerge(left, right)
        
        
        return sortedlist
    
    # Utility function to get the middle 
    # of the linked list 
    def getMiddle(self, head):
        if (head == None):
            return head

        slow = head
        fast = head

        while (fast.next_node != None and fast.next_node.next_node != None):
            slow = slow.next_node
            fast = fast.next_node.next_node
            
        return slow


#------------------------------------------------------------------------------

    def sortInverse(self):
        prev = None
        current_node = self.first_node
        while(current_node is not None): #if the current node isnt empty
            next_node = current_node.next_node 
            current_node.next_node = prev
            prev = current_node
            current_node = next_node
        self.first_node = prev

    

    
'''----------------------------------------------------------------------------------------------------------------------'''

#creating the object part_A as linked list 
part_A = LinkedList()


'''-----------------------------------------------------------------------------------------------------------------------
1.1.	Create a list from scenario above
'''

#Creation of the list according to the user choice
while True:
    try:
        option = input('Determine the type of list you want to create (a=actors) (g=games) (m=movies): ').lower()
        if option not in ('a','g','m'):
            raise ValueError('Invalid input')
        break
    except ValueError:
        print('Remember (a)=actors (g)=games (m)=movies')
    
#Once the type list has been choosen, we proceed to add this value to the linked list
list_type=part_A.creation_of_list(option)


    
'''-----------------------------------------------------------------------------------------------------------------------
1.2.	Add a value to the list 
'''
for element in list_type:
    part_A.append(element)
    

#testing adding aaa
addition=input('\ngive a value to add to the list: ').title()
part_A.append(addition)

print('\n--------------Linked list---------------------\n')
part_A.print_list()

'''------------------------------------------------------------------------------------------------------------------------
1.3.	Delete a value from the list 
'''
itemToDelete=input('\nGive the value to delete: ').title()

#starting the deletion process
part_A.delete(itemToDelete)

#printing the list after the deletion process
print('The new list will look like this: \n')
part_A.print_list()

tmp=part_A.tmp_list()
print('\n',tmp)

part_A.refresh()
print('\nAfter updating the information the list will look like this: ')
part_A.print_list()
#for data in tmp:
#    part_A.append(data)

#part_A.append(tmp)

#part_A.print_list()

'''------------------------------------------------------------------------------------------------------------------------
1.4.	Sort all the data in the list in the ascending order.  
'''
while True:
    try:
        ascending=input('\nDo you want to sort the list in ascending order?(y=yes n=no)').lower()
        if ascending not in('y','n'):
            raise ValueError
        break
    except ValueError:
        print('Invalid input (y=yes) (n=no)')

if(ascending=='y'):
    print('\nThis function will sort the data in ascending order\n\n')

    part_A.first_node = part_A.mergeSort(part_A.first_node)
    part_A.print_list()





'''Sort all the data in the list in the descending order.'''


while True:
    try:
        ascending=input('\nDo you want to sort the list in descending order?(y=yes n=no)').lower()
        if ascending not in('y','n'):
            raise ValueError
        break
    except ValueError:
        print('Invalid input (y=yes) (n=no)')

if(ascending=='y'):

    print('\nThis function will sort the data in descending order\n')

    part_A.sortInverse()
    part_A.print_list()

'''------------------------------------------------------------------------------------------------------------------------
1.5.	Search for the value in the list asking user for input.
'''

target = input('\nGive the item to search: ').title()
print(part_A.search(target))
                    



