import random
from art import logo
print("Welcome to Guess THAT Number!")
print("Today's number is between 1 and 100. Good luck!")
yes_num= random.choice(range(101))

level=input("Choose a difficulty. 'easy' or 'hard'? ")
"""***Create a logo to go in right here**"""
"""Welcome to the guessing game"""
lives= 0
def difficultity():
    global lives
    if level == 'hard':
        lives += 5
        print(f"You have {lives} lives.")
    elif level == 'easy':
        lives += 10
        print(f"You have {lives} lives")
    else: 
        print("Please choose a valid input")
        
difficultity()



def guess():
    global lives
    make_guess= int(input("Make a guess:"))
    if make_guess < yes_num:
        lives -=1
        print("Too low")
        print(f"You have {lives} lives.")
    if make_guess > yes_num:
        lives -= 1
        print("Too high")
        print(f"You have {lives} lives.")
    else:
        if make_guess== yes_num:
            print(f"You win. The answer is {yes_num}.")
            exit()
    
    while lives == 0:
        print("You have run out of lives! Game over")
        break
    
                   
guess()

""" Try to move guess function into guess again and see if it works as one function"""
def guess_again():

    
    
    while lives != 0:
        guess()
   
    
        
    
guess_again()





    

