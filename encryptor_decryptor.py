
choice = 0
try:
    while(choice!=3):
        choice = int(input("\n---ENCRYTION MENU---\n1.Encrypted Data\n2.Decrypted Data\n3.Exit\n\n"))
        match choice:
            case 1:
                user_input = input("Enter the word: ")
                user_input = list(user_input)
                length = len(user_input)
                if length <= 3:
                    user_input.reverse()
                    print("Encrypted value is: ",user_input)
                elif length > 3:
                    wordsstart = "lat"
                    wordsstartrev = "tal"
                    wordsend = "ods"
                    newlist = user_input.copy()
                    newlist.reverse()
                    first_word = newlist.pop()
                    newlist.append(wordsstart)
                    newlist.reverse()
                    newlist.append(first_word)
                    newlist.append(wordsend)
                    newlist = "".join(newlist)
                    print("Encrypted value is: ",newlist)
            case 2:
                user_input = input("Enter the word: ")
                user_input = list(user_input)
                length = len(user_input)
                if length <= 3:
                    user_input.reverse()
                    print("Decrypted value is: ",user_input)
                elif length > 3:
                    user_input = "".join(user_input) 
                    user_input = user_input.replace(wordsend,"")
                    user_input = list(user_input)
                    user_input.reverse()
                    user_input = "".join(user_input)
                    user_input = user_input.replace(wordsstartrev,"")
                    user_input = list(user_input)
                    user_input.reverse()
                    last_character = user_input.pop()
                    user_input.reverse()
                    user_input.append(last_character)
                    user_input.reverse()
                    user_input = "".join(user_input)
                    print("Decrypted value is: ",user_input)
            case 3:
                print("Thanks for using the encryptor!")
            case _:
                print("Invalid Input!\nPlease Try  Again\n")
except:
    print("Error 404")       