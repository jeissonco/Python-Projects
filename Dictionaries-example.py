'''
Autor: Jeisson Nino
student ID: 20106991

Created: 13/05/2024

Version: 1.2 16/05/2024



following tasks to perform:

1.1.	Create a dictionary from the scenario above
1.2.	Add a value to the dictionary
1.3.	Delete a value from the dictionary
1.4.	Sort all the data in the dictionary in the ascending order. Sort all the data in the dictionary 
'''



#defining the dictionary to work with

#movies = { 'Finding Nemo' : 2003, 'Matrix'  : 1999, 'Titanic': 1997, 'Forrest Gump': 1994, 'The Lord of the Rings' : 2001, 'Narnia': 2005, 'Mission Impossible' : 1996, 'Shrek' : 2001, 'Batman': 2005, 'The Avengers': 2012, 'Fast and Furious 9': 2021,  'Spiderman': 2009}


# testing of the dictionary to work with
#print(movies)


import operator

#---------------------------- FUNCTIONS ----------------------------

# creation of the dictionary

def create_dictionary(data_type):
    # Creamos el diccionario con los datos proporcionados
    
        actors ={
            "Johnny Depp": 1963,
            "Emma Watson": 1990,
            "Leonardo DiCaprio": 1974,
            "Jennifer Lawrence": 1990,
            "Tom Hanks": 1956,
            "Meryl Streep": 1949,
            "Brad Pitt": 1963,
            "Angelina Jolie": 1975,
            "Denzel Washington": 1954,
            "Scarlett Johansson": 1984,
            "Robert Downey Jr.": 1965,
            "Anne Hathaway": 1982
        }

        movies={
            "Inception": 2010,
            "The Shawshank Redemption": 1994,
            "The Godfather": 1972,
            "Pulp Fiction": 1994,
            "The Dark Knight": 2008,
            "Forrest Gump": 1994,
            "Schindler's List": 1993,
            "The Lord of the Rings: The Return of the King": 2003,
            "Fight Club": 1999,
            "The Matrix": 1999,
            "The Silence of the Lambs": 1991,
            "Goodfellas": 1990
        }
        games = {
            "The Legend of Zelda: Breath of the Wild": 2017,
            "Red Dead Redemption 2": 2018,
            "The Witcher 3: Wild Hunt": 2015,
            "Grand Theft Auto V": 2013,
            "Dark Souls": 2011,
            "The Last of Us": 2013,
            "Skyrim": 2011,
            "Bloodborne": 2015,
            "Metal Gear Solid V: The Phantom Pain": 2015,
            "Fallout 4": 2015,
            "Mass Effect 2": 2010,
            "Uncharted 4: A Thief's End": 2016
        }

        if data_type == 'a':
            return actors
        elif data_type == 'g':
            return games
        elif data_type == 'm' :
            return movies
        else:
            return 'invalid input'


# adding data to the dictionary 

def add_data(dictionary, name):
    while True:
        try:
            year=int(input('\nGive the year of release or year birth: '))
            if year < 1000 or year >= 2025:
                raise ValueError('Invalid year')
            break
        except (ValueError):
            print('Please enter a valid year: ')

    dictionary[name] = year
    print(f'The following movie {name} was added to the database')


# Deleting data from the dictionary

def delete_data(dictionary):

#Avoid user errors by using try/except
    while True:
        try: 
            key = input('\nWhat data(key) do you want to delete?: ').title()
            if not key in dictionary: #Checkpoint to see if the key exits within the dictionary
                raise ValueError('This data does not exist in the dictionary')
            break
        except (ValueError):
            print('Please enter a valid key')

    #Due to the comparison before, here we know the key exits, therefore proceed to delete de key and value 
    dictionary.pop(key)

    return dictionary



# Ascending sorting function

def ascending_sorting(dictionary):

    while True:
        try:
            option = input('Do you want to sort the dictionary by the key or the value? (k=key, v=value)').lower()
            if option not in ('k', 'v'):
                raise ValueError('Wrong input (k=key, v=value)')
            break
        except (ValueError):
            print('Please enter a valir option')

    if option =='k':    
        #Create a list of the keys in the dictionary
        List_keys = list(dictionary.keys())

        List_keys.sort() #sort them

        #Using comprehension create the new sorted dictionary using the keys
        Sorted_keys = {i: dictionary[i] for i in List_keys}

        return Sorted_keys

    else:
        #Store the sorted dictionary by the values 
        return dict(sorted(dictionary.items(), key=lambda kv: (kv[1], kv[0])))

        #Use the sorted method to sort the dictionary and the key=lambda kv: 
        #This lambda function takes (key, value) and returns a tuple containing (value, key)
        #With the value as the first element the sorted function returns (value, key) sorted

        
 # Descending sorting function

def descending_sorting(dictionary):

    while True:
        try:
            option = input('Do you want to sort the dictionary by the key or the value? (k=key, v=value)').lower()
            if option not in ('k', 'v'):
                raise ValueError('Wrong input (k=key, v=value)')
            break
        except (ValueError):
            print('Please enter a valir option')

    if option == 'k':
        return dict(sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True))
    else:
        return dict(sorted(dictionary.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))


#---------------------------- MAIN ----------------------------


# 1.1.	Create a dictionary from the scenario above


while True:
    try:
        data_type = input('Provide the type of dictionary you want to create (a)=actors, (g)=games, (m)=movies: ').lower()
        if data_type not in ('a', 'g', 'm'):
            raise ValueError('Invalid input')
        break
    except ValueError as e:
        print(f'\n{e}: Please enter a valid dictionary type (a = actors, g = games, m = movies)')

# Assuming create_dictionary is defined elsewhere
data_base = create_dictionary(data_type)



#1.2.	Add a value to the dictionary

#This comparion will help to print a line according to the menu/type of dictionaries that we have
if data_type == 'a':
    data_type = 'actors'
elif data_type == 'g':
    data_type = 'games'
else:
    data_type = 'movies'


#Saving/assigning the the key of the dictionary 
data_name=input(f'\nGive a {data_type} to add to the database: ').title()



#Call the function with the dictionary and the key to add to the database, the value to add will be asked inside the function
add_data(data_base, data_name)

print('\n',data_base)


#1.3.	Delete a value from the dictionary

#Calling the function to delete a value from the database, the key will be asked inside the function

print('\n',delete_data(data_base))


#1.4A	Sort all the data in the dictionary in the ascending order and descending order

while True:
    try:
        option_sort = input('How do you want to sort the dictionary, ascending = (a) or descending = (d)?: ').lower()
        if option_sort not in ('a','d'):
            raise ValueError('Invalid option')
        break
    except ValueError:
        print('Remember Ascending = (a) or descending = (d): ')

    
if option_sort == 'a':
    ascending_data = ascending_sorting(data_base)
    print('\n',ascending_data)
else:
    descending_data =descending_sorting(data_base)
    print('\n',descending_data)

