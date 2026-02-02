password = input("Enter the password: ")

largealp = 0
smallalp = 0
symbol = 0
number = 0
length = len(password)
for i in password:
    

    if i.isupper():
        largealp += 1
        continue
    elif i.islower():
        smallalp += 1
        continue
    elif i.isnumeric():
        number += 1
        continue
    elif not i.isalnum():
        symbol += 1
        continue





if length>=8 and largealp>=1 and smallalp>=2 and number >=2 and symbol >=1:
    print("STRONG PASSWORD!")
else:
    print("WEAK PASSWORD!!!")