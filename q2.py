#!usr/bin/python3
# Python dugga 
# Q2 

my_names = ["alice", "bob", "charlie"]

# Q2 a) fetch length of each name in my_names, append long names (4< char) to new list: long_names
long_names = []
for n in my_names:
    print(len(n))
    if len(n) > 4:
        long_names.append(n)
print(long_names)

# Q2 b) define a function, get_long_names, from your loop
#       input variable: my_names, save list to var my_long_names
def get_long_names(my_names):
    long_names = []
    for n in my_names:
        if len(n) > 4:
           long_names.append(n)
    return long_names

print(get_long_names(my_names))

# Q2 c) modify loop again, 
#       append *strings* of  new_list to my_names
new_list = ["doggy", 5, "elsa"]

def add_more_names(my_names, new_list):
    old_list = my_names
    for n in new_list:
           # Try: 
        if type(n) is str:
           old_list.append(n)
        elif not type(n) is str:
            raise TypeError(f"{n} doesn't look like a name, it has not been added to my list of names")
    return old_list

print(add_more_names(my_names, new_list))
print(my_names)