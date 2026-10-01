#in this practice project will make a game of rock, paper, scissors
import random
print("----------Welcome To Rock Paper Scissors----------")
options = ("rock", "paper", "scissors")
score = 0
tie = 0
lost = 0
attempts = 0

while True:
    answer = random.choice(options)
    guess = input("Enter A Choice - (1. Rock) (2. Paper) (3. Scissors): (q to quit) ")
    guess = guess.lower()

    if guess == "q":
        break;
    
    attempts +=1
    if guess == answer:
        print(f"That's A Tie, The Ai Chose {answer} aswell")
        tie+=1

    elif guess == "rock" and answer == "paper":
        print(f"You Lose This Round!, Ai chose {answer}")
        lost+=1

    elif guess == "rock" and answer == "scissors":
        print(f"You Won This Round!, Ai chose {answer}")
        score +=1

    elif guess == "paper" and answer =="rock":
        print(f"You Won This Round!, Ai chose {answer}")
        score +=1

    elif guess == "paper" and answer == "scissors":
        print(f"You Lose This Round!, Ai chose {answer}")
        lost+=1

    elif guess == "scissors" and answer == "rock":
        print(f"You Lose This Round!, Ai chose {answer}")
        lost+=1

    elif guess == "scissors" and answer == "paper":
        print(f"You Won This Round!, Ai chose {answer}")
        score +=1

    else:
        print("That's not a valid Answer")
        attempts -=1

print(f"Your Total Score Is {score} with {tie} ties and {lost} loses")
print(f"You took {attempts} attempts Hence {score}/{attempts} wins")
