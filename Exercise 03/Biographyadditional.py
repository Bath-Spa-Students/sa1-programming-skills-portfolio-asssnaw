# The following code is used to ask the user for their name and hometown
name = input("Enter your full name: ")
hometown = input("Enter your hometown: ")

# the following code will repeatedly ask the user for age in integer units until the answer is given in integer
while True:
    try:
        age = int(input("Enter your age: "))  # this code will Try to convert the input to an integer
        break  # If the answer is  successfully converted to integer , the code will exit the loop
    except ValueError:
        print("Invalid input! Please enter a valid number for your age.")  # if the answer is not integer it will ask the user to input the answer again

# This code is used to store the information in dictionary 
person_info = {
    "name": name,
    "hometown": hometown,
    "age": age
}

# This code is used to print the information to show the final outputs
print(f"\nName: {person_info['name']}\nHometown: {person_info['hometown']}\nAge: {person_info['age']}")
