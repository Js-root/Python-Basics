#In This Practice Project We Would Create A Python Quiz Game

questions = ("Which planet is known as the Red Planet?",
             "What is the capital city of Japan?",
             "How many sides does a hexagon have?",
             "Who wrote Romeo and Juliet?",
             "What is the largest ocean on Earth?")

options = ( ("A. Venus", "B. Mars", "C. Jupiter", "D. Mercury")
           ,("A. Seoul", "B. Beijing", "C. Tokyo", "D. Bangkok")
           ,("A. 5", "B. 6", "C. 7", "D. 8")
           ,("A. Charles Dickens", "B. Mark Twain", "C. William Shakespeare", "D. George Orwell")
           ,("A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"))

answers = ("B","C","B","C","D")
guesses = []
score = 0
question_Number = 0
rando = 0

for i in questions:
    print("----------------------------------------------")
    print(i)
    for x in options[question_Number]:
        print(x)

    guess = input("Enter Answer (A,B,C,D): ")
    guess = guess.upper()
    guesses.append(guess)
    question_Number +=1

for i in guesses:
    if guesses[rando] == answers[rando]:
        score+=1
        rando += 1
        print("✅")
    else:
        rando += 1
        print("❌")

print(f"Your Score Is: {score}")