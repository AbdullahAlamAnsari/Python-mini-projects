balance = 1000
pin = 1257
deposit = 0
withdraw = 0

answer = int(input("ENTER THE ACCOUNT PIN: "))
if(answer == pin):
    choice = int(input("\n---ATM MENU---\n1.DEPOSIT\n2.BALANCE CHECK\n3.WITHDRAW\n4.EXIT\n"))
    if(choice == 1 or choice == 2 or choice == 3 or choice == 4):
        match choice:
            case 1:
                if(balance == 0):
                    balance = int(input(print("\nYOUR BALANCE IS ",balance ,"FIRST PLEASE ENTER THE BALANCE: ")))
                elif(deposit<0):
                    print("\nINVALID AMOUNT")
                else:
                    deposit =  int(input(print("Enter the deposited amount: ")))
                    balance = balance + deposit
                    print("YOU HAVE DEPOSITED : ",deposit,"PKR AND THE REMAINING BALANCE IS: ",balance ,"PKR")
            case 2:
                print("YOUR CURRENT BALANCE IS: ",balance)
            case 3:
                if(balance == 0):
                    balance = int(input(print("\nYOUR BALANCE IS ",balance ,"FIRST PLEASE ENTER THE BALANCE: ")))
                elif(deposit<0):
                    print("\nINVALID AMOUNT")
                else:
                    withdraw =  int(input(print("Enter the amount you want to withdraw: ")))
                    balance = balance - withdraw
                    print("YOU HAVE WITHDREW : ",withdraw,"PKR AND THE REMAINING BALANCE IS: ",balance ,"PKR")
            case 4:
                quit()
                
else: 
    print("INVALID PIN")