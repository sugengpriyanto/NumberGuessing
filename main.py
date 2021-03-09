#random number
from random import randint

easy_level = 10
hard_level = 5
#set difficulty
def set_diff():
  diff = input("Choose a difficulty. Type 'easy' or 'hard'")
  if diff == "easy":
    return easy_level
  elif diff == "hard":
    return hard_level
  else:
    print("You type a wrong input")

#check answer
def check_answer(guess, answer, turns):
  if guess > answer:
    print("To high")
    return turns - 1
  elif guess < answer:
    print("Too low")
    return turns -1
  elif guess == answer:
    print(f"You right! the answer is {answer}")

def play():
  print("Welcome to the Number Guessing Game")
  print("I'm thinking of a number between 1 and 100")
  answer = randint(1, 100)
  print(f"ssstt... the answer is {answer}")

  turns = set_diff()
  guess = 0

  #repeating guess
  while guess != answer:
    print(f"You have remaining {turns} chances to guess")
    #guess a number
    guess = int(input("Guess a number: "))

    #track lives
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You lose")
    elif guess != answer:
      print("Guess again")

play()