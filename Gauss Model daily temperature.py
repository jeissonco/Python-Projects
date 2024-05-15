import random 

# ID:20106991 Jeisson Nino North Metropolitan TAFE
# 10/04/2024
#---------------------------------------------FUNCTIONS-------------------------------------------------------

#Create the temperature list
def temperature_data(mu, sigma):
    monthly_temperature= []
    for x in range(31):
        daily_temperature=[]
        for y in range(24):
     
        #radon gauss function to simulate temperature during 24 hours, I've used the function round to have only 2 digits after the point(2).
            daily_temperature.append(round(random.gauss(mu, sigma), 1))

        monthly_temperature.append(daily_temperature)

    return monthly_temperature

#------------------------------------------------------------------------------------------------------------
#Display the average temperature at noon

def average_temperature_noon(list):
    
    average=0
    for days in list:
        counter=0
        for temp in days:
            counter+=1
           # print(counter,' checking values: ',temp)
            if counter == 12:
            #    print('key value ->', temp)
                average+=temp
    

    return average/31

#------------------------------------------------------------------------------------------------------------
#sorting the list in ascending order

def sorting_ascending(list_temperature):

    #list comprehension
    #new_list_sorted = [ [hourly_temp for hourly_temp in days] for days in list_temperature]
    #return print(new_list_sorted)


    new_list_to_sort=[]
    for days in list_temperature:
        list_temporary=[]
        for hourly_temp in days:
            list_temporary.append(hourly_temp)

        list_temporary.sort()
        new_list_to_sort.append(list_temporary) 

    return new_list_to_sort

#------------------------------------------------------------------------------------------------------------
#Binary search function
def binary_search(list, item):
    #Counter variable is set to 1 if the temperature is found in the 1st day
    counter = 1
    
    #Accessing the nested list
    for days in list:
        
        
        #the positions of part that we are going to check
        first_position=0

        last_position=len(days)


        while first_position <= last_position:
            #index=[]
            #dividing the list in the half to do the search
            mid=(last_position+first_position) // 2

            #if the element in the mid position is less than the target item, it'll move the first position to the mid+1, and ignore the left half of the list
            if days[mid] < item:
                first_position= mid +1
                
            #if the element in the mid position is greater than the target, it'll move the last position to the mid-1, and ignore the right half of the list
            elif days[mid] > item:
                last_position=mid-1

            #we have found our target item in the mid
            else:
                
                return days[mid], counter
        counter+=1      


    #the target item is not in the list
    return None


#-------------------------------------------------------------------------------------------------------------

def finding_temperature_on_a_date(temperature, target_date, date):
        
    if temperature != None:
        return print ('The temperature to search ',date,' is in the list\nWe found the temperature on this date: ',target_date)
    else:
        return print("The temperature to search was not registered during the day")



#--------------------------------------------------------------------------------------------------------------
#this function makes the list of the highest and lowest temperatures of the days    
def daily_highs_and_lows(list):
    maximum_temperature=[]
    minimum_temperature=[]

   
    for day in list:
     #Here I am moving through the list of sorted temperature, and taking the last position which will be the highest temperature of the day    
        max=day[-1]
        maximum_temperature.append(max)

        min=day[0]
        minimum_temperature.append(min)

    return maximum_temperature, minimum_temperature


#---------------------------------------------------------------------------------------------------------------

#MAIN
#this is the average value(temperature)


while True:        
    try: 
        average= float(input("Give an average temperature for the days: "))
        #this is the standard deviation 
        deviation= float(input("Give the deviation standard of this: "))
        break 
    except:
        print('invalid value, numbers please not letters or characters')

#list for the montly temperature, it has a 24hr list itself
temps =[]


#Calling the function to create the temps lists with the 24hr records 
temps=temperature_data(average, deviation)
print(temps)


#checking the average temp at noon

noon = average_temperature_noon(temps)
print('\nthe average temperature at noon is: ',round(noon, 1))

#Sort the existing array of daily temps in ascending order
print("\ndaily temperature list in ascending order")

#new list created with the temperature sorted ascending.
sorted_list=sorting_ascending(temps)
print(sorted_list)

#Binary search
#item to search 
target=float(input('\nType the temperature to search: '))


#Here we receive a response from our binary search either the exact temperature when is found and the date, or a none value saying that the temperate is not in that day
search, which_date=binary_search(sorted_list, target)


#Print if the temperature to search and the day are found or not
finding_temperature_on_a_date(search, which_date, target)

daily_highs, daily_lows=daily_highs_and_lows(sorted_list)
print('\ndaily Highs temperatures :',daily_highs)
print('\ndaily lows temperatures: ', daily_lows)
