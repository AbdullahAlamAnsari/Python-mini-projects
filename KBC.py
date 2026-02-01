questions = [
    "What is the capital of Pakistan?",
    "Which planet is known as the Red Planet?",
    "Who wrote the play 'Romeo and Juliet'?",
    "What is the chemical symbol for water?",
    "Which year did Pakistan gain independence?"
]

answers = [
    "Islamabad",
    "Mars",
    "William Shakespeare",
    "H2O",
    "1947"
]

options = [
    "A) Karachi  B) Lahore  C) Islamabad  D) Peshawar",
    "A) Venus  B) Mars  C) Jupiter  D) Saturn",
    "A) William Wordsworth  B) William Shakespeare  C) Charles Dickens  D) Jane Austen",
    "A) H2  B) O2  C) H2O  D) CO2",
    "A) 1945  B) 1947  C) 1950  D) 1955"
]

score = 0
run = True
maxrange = len(questions)

while run:
    for i in range(maxrange):
        print("\nQ" + str(i+1) + ": " + questions[i])
        print("Options: " + options[i])
        
        answer = input("Write the answer please: ").strip()
        
        if answer.title() == answers[i]:  
            score += 1000
            print("Correct! You won: " + str(score) + " RS")
        else:
            print("Incorrect! YOU LOST THE GAME")
            print("GAME OVER. Total winnings: " + str(score) + " RS")
            run = False
            break 

        if run:  
            userinput = input("Do you want to play more? (Y/N): ").strip().upper()
        if userinput == 'Y':
            continue
        else:
            print("Thanks for playing! You won: " + str(score) + " RS")
            run = False
            break
 
    
    