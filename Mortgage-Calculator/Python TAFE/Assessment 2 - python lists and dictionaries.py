# Student ID: 20106991
# Name: Jeison Nino
# Diploma Advance Networking


#PART A  ---------------------- LISTS


#A list that stores at least 12 of your fav actors/actresses' names.
#A list that stores at least 12 of your fav movies.
#A list that stores at least 12 of your fav games.




#Creation of the lists
"""
list_of_actors = ['Tom Hanks', 'Leonardo DiCaprio', 'Denzel Washington', 'Tom Cruise', 'Johnny Depp', 'Will Smith', 'Harrison Ford', 'Robert Downy Jr', 'AL Pacino', 'Morgan freeman', 'Samuel L. Jackson', 'Brad Pitt']
        
list_of_movies = ['The Godfather', 'The Dark Knight', 'Schindlers List', 'Pulp Fiction', 'Forrest Gump', 'Fight Club', 'Inception', 'The Matrix', 'Goodfellas', ' Dune', 'se7en', 'Interstellar']

list_of_games = ['Fortnite', 'Hades', 'Resident Evil', 'God of War', 'Pac-Man', 'Super Mario Bros', 'Donkey Kong', 'Apex', 'Minecraft', 'Zelda', 'World of Warcraft', 'Tetris']

"""

#------------------------Menu Part A -------------------------------

# 1 create a list

def creation_of_list():

    counter=0
    while True:

        type_of_list=input('this list is a list of : ')
        
        try:
            if type_of_list.lower() == 'actors' or type_of_list.lower() == 'games' or type_of_list.lower() == 'movies':
                    new_list=[]
                    for i in range(3):
                        
                        data=input(f"Type the value to add to the list {type_of_list}: ")
                        new_list.append(data)


            return new_list        
        
        except:
            print('Not a type of list that we are expecting (actors/movies/games), try again')    

# 2 add value to the list

# 3 Delete a value from the list
# 4 sort all the dat ain the list in the ascending order/ descending order
# 5 search the value in the list asking the user for input




#-------------------------- Create a 3 Lists---------------------------------------------------------------------------- 


# Adding a value to the list



"""
def adding_values(list_to_add, value)
    
    return
"""

new_list=creation_of_list()
print(new_list)


def menu():
    print('--------------------MENU-----------------------')
    print('This assessment has 2 parts: part A(Lists) and part B(Dictionaries)')
    print('type what part do you want to try first (A/B)?')
    print('If you want to close the program (X)')
    while True:
        option=input('you choice (A/B/C): ')
        option.upper()
        try:
            if option == 'A':
                #run the part A
            elif option == 'B':
                #run the part B
            else:
                #finish the program
                break
        except:
            print('not a valid input. (A=lists) (B=Dictionaries) (x=close)')


# Delete a value from the list



# Sort all the data in the list in the ascending order. 



# Sort the data in the list in the descending order.



# Search for a value in the list asking user for input.