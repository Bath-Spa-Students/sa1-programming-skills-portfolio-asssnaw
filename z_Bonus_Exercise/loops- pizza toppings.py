# The following code guides the uder on how to exit the loop
print("Enter 'quit' once you finished adding pizza toppings.")

while True: #The loop starts here asking the user for what topping they want to add
    topping = input("Enter what pizza topping do you want: ").strip()
    
    # This code checks if the user wants to quit the loop.
    if topping.lower() == 'quit':
    #If the user has entered quit and wants to quit the loop the following statement will be printed.
        print("Thank you, Finished adding toppings to your delicous pizza!")
        break #This will break the loop here

    #The loop will continue if the user wants to add more pizza toppings
    else:
        #The following statement will be printed assuring the user that the topping was added on the pizza
        print(f"Great choice!, I'll add {topping} to your pizza.")

#And the loop will continue asking the user for next topping until the user typed 'quit' to break the loop