class my_list:

    def __init__(self, name, list):
        self.name = name
        self.list=[]

    def add_values_to_list(self, list):

        for element in list:
            self.list.append(element)

    def print_out(self, list):
        
        for i in range(len(list)):
            print(self.list[i])


list_of_movies = ['toy story', 'Finding Nemo']

movies = my_list('Movies',list_of_movies)

        