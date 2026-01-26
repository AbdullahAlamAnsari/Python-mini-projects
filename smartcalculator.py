number_1 = int(input("Enter the number 1: "))
number_2 = int(input("Enter the number 2: "))


op = input("Enter the operator + , - , * , % , / , ** : ")


if(op == "+" or op == "-" or op is "/" or op is "*" or op is "**" or op is "%" ):
    match op:
        case "+":
            print(number_1 + number_2)
        case "-":
            print(number_1 - number_2)
        case "*":
            print(number_1 * number_2)
        case "/":
            float(print(number_1 / number_2))
        case "**":
            print(number_1 ** number_2)
        case "%":
            if(number_2 == 0):
                print("Invalid denominator")
            else:
                print(number_1 % number_2)
else:
    print("Invalid Input")

    
    
