# These are the list of names
names = ["Jake", "Zac" , "Ian", "Ron" , "Sam" , "Dave"]

# this code is used to promt the user for a name that is the user wants to search
search = 'Sam'

#If the name entered by the user is mentioned in the list the following statement will be printed
if search in names:
    print(f"{search} found in the list!")
#If the name entered by the user is not mentioned in the list the following statement will be printed
else:
    print(f"{search} not found in the list.")
    

    
