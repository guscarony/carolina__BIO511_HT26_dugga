#!usr/bin/python3

# Define var my_list with contents
#my_list = [1, 5, '4', 'six', 3.14]
my_list = [1, 5, '4', 3.14]


def clean_list(my_list):    # define func clean_list
    new_list = []       # Define empty list
    for x in my_list:   # iterate over items (x) in list
    #    print(x)       # juuust checking
        new_list.append(int(x)) # converts items (x) in list to ints, appends converted item to new_list
        if x is str:            # checks if item is a string
            raise TypeError(f'Error. {x} is not convertible to integer, items must be numerical. List conversion terminated') # oh wat
        if x is float:          # checks if item is a  float
            print(f'Warning! {x} is a float, decimals are removed in list conversion')          
            # Warning not printed, check back
            # If time, add 'continue anyway? y/n
    return new_list     # passes new_list to output

print(clean_list(my_list))  #prints the function output of my_list 


new_list_b = [2, 4, 6, 3]