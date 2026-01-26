import random

user_input = int(input("Enter the number from 1-6: " ))
if(user_input <1 or user_input>6):
    print("\nINVALID NUMBER")
computer_input = random.randint(1,6)
if(user_input == computer_input):
    print("\nYOUR NUMBER: ",user_input," COMPUTER NUMBER: ",computer_input)
    print("\nDRAW")
elif(user_input < computer_input):
    print("\nYOUR NUMBER: ",user_input," COMPUTER NUMBER: ",computer_input)
    print("\nCOMPUTER WON!")
elif(user_input > computer_input):
    print("\nYOUR NUMBER: ",user_input," COMPUTER NUMBER: ",computer_input)
    print("\nUSER WON!")
else:
    print("\nINVALID ATTEMPT")


