# This is the coding for the primitive advanced requirements 

# 1) Ignore capitalization

#The Question "What is the capital for France" is assigned to the varriable Question_1 

Question_1 = str(input("What is the capital of France?"))

# Once the user types the correct answer paris in oreder for the question to accept all the ways of typing paris we will use elif meathod
#if the user types "Paris"
if Question_1 == "Paris":
    print("The answer is correct") # the answer will appear to be correct

#if the user types "paris"
elif Question_1 == "paris":
    print("The answer is correct") # the answer will appear correct

# if the user types "paRis"
elif Question_1 == "paRis":
    print("The answer is correct") #the answer will appear correct

# if the user types any other answer except for the ones mentioned above 
else:
    print("The answer is wrong") #the answer will appear to be wrong

#Extending the program into quiz that asks for the capitals of 10 european countires

# We will use the bellow code to display the question asking the capital of Albania to the varriable Question_2

Question_2 = str(input("What is the capital of Albania?"))
#If the user types the correct answer (i.e. Tirana)
if Question_2 == "Tirana":
    print("The answer is correct") # the answer will appear correct
#If the user types the wrong answer
else:
    print("The answer is wrong.") # the answer will appear wrong

#We will use the bellow code to display the question asking the capital of Andorra to the varriable Question_3
Question_3 = str(input("What is the capital of Andorra"))
# if the user types the correct answer (i.e. Andorra La Vieja)
if Question_3 == "Andorra La Vieja":
    print("The answer is correct.") #The answer will appear correct
# if the user types the wrong answer 
else:
    print("The answer is wrong") #The answer will appear wrong

#We will use the bellow code to display the question asking the capital of Armenia to the varriable Question_4
Question_4 = str(input("What is the capital of Armenia?"))
# if user types the correct answer (i.e. Yerevan)
if Question_4 == "Yerevan":
    print("The answer is correct.") #The answer will appear correct
#If the user types the wrong answer
else:
    print("The asnwer is wrong.") #The answer will appear wrong

#We will use the bellow code to display the question asking the capital of Austria to the variable Question_5
Question_5 = str(input("What is the capital of Austria?"))
#If the user types the correct answer (i.e. Vienna)
if Question_5 == "Vienna":
    print("The answer is correct.") #The answer will appear correct
# if the user types the wrong answer
else :
    print("The answer is wrong") #the answer will appear wrong

#We will use the bellow code to display the question asking the capital of Azerbaijan to the varriable Question_6
Question_6 = str(input("What is the capital of Azerbaijan"))
# if the user types the correct answer (i.e. Baku)
if Question_6 == "Baku":
    print("The answer is correct.") #the answer will appear correct
# if the user types the wrong answer
else:
    print("The answer is wrong") #the answer will appear wrong

#We will use the bellow code to display the question asking the capital of Belarus assigned to the varriable Question_7
Question_7 = str(input("What is the capital of Belarus?"))
# if the user types the correct answer (i.e. Minsk)
if Question_7 == "Minsk":
    print("The answer is correct") # the answer will appear correct
# if the user types the wrong answer
else:
    print("The answer is wrong") #the answer will appear wrong

#We will use the bellow code to display the question asking the capital of Belguim assigned to the varriable Question_8
Question_8 = str(input("What is the capital of Belguim?"))
# if the user types the correct answer (i.e. Brussels)
if Question_8 == "Brussels":
    print("The answer is correct.") #the answer will appear correct
# if the user types the wrong answer 
else:
    print("The answer is wrong") #the answer will appear wrong

#We will use the bellow code to display the question asking the ctapital of Finland assigned to the variable Question_9
Question_9 = str(input("What is the capital of Finland?"))
# if the user types the correct answer
if Question_9 == "Helsinki":
    print("The answer is correct")# the answer will appear correct
# if thw user types the wrong answer
else:
    print("The answer is wrong") # the answer will appear wrong

#We will use the bellow code to display the question asking the capital of Denmark assigned to the variable Question_10
Question_10 = str(input("What is the capital of Denmark?"))
#If the user types the correct answer
if Question_10 == "Copenhagen":
    print("The answer is correct")# the answer will appear correct
#if the user types the wrong answer
else:
    print("The answer is wrong")#the answer will appear wrong

#We will use the bellow code to display the question asking the capital of Cyprus assigned to the variable Question_11
Question_11 = str(input("What is the capital of Cyprus?"))
#if the user types the correct answer
if Question_11 == "Nicosia":
    print("The answer is correct") #the answer will appear correct
#if the user types the wrong answer 
else:
    print("The answer id wrong.") #the answer will appear wrong
