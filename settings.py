import random


yes_num= random.choice(range(101))
lives= 5
level=input("Choose a difficulty. 'easy' or 'hard'? ")
make_guess= int(input("Make a guess:"))
game_on = False

print(make_guess())