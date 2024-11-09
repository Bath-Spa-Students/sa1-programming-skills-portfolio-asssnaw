#These are the List of names of strings
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# this code is used to promt the user for a name that is the user wants to search
search = input("Enter the name you want to search for: ")

# The code used makes the program search if the name is mentioned in the list 
if search in names:
    print(f"{search} found in the list!") #The following statement is printed if the name is there in the list
else:
    print(f"{search} not found in the list.") #The following statement is printed if the name is not there in the list
