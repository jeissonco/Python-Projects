#Assessment 2 
# student ID: 20106991
# Author: Jeisson Nino


#Using linked lists to resolve the part A
class Node_of_list:
    def __init__(self,data):
        self.data=data  
        self.next_node=None 

class LinkedList:
    def __init__(self):
        # Initialize of the head node in the linked list
        self.first_node=None

    def append(self,data):
        new_node=Node_of_list(data)
        if not self.head:


#1.1.	Create a list from scenario above
#1.2.	Add a value to the list 
#1.3.	Delete a value from the list 
#1.4.	Sort all the data in the list in the ascending order. Sort all the data in the list in the descending order. 
#1.5.	Search for the value in the list asking user for input.
