# A game I wrote to practice with functions, recursion, and variable scope
# Try to guess the computer's randomly selected number in as few attempts as possible

import random

computer_num = random.randint(1,100)

print "I'm thinking of a number between 1 and 100."
print "Can your guess what it is?"

counter = 0

def get_num():
  guess = ''
  while not guess.isdigit() or int(guess) < 1 or int(guess) > 100:
    print "Please enter a number between 1 and 100:"
    guess = raw_input()
  global counter
  counter += 1
  return int(guess)

def guess_num():
  num_guessed = get_num() 
  global counter 
  if num_guessed < computer_num:
    print "A little too low. try again:"
    guess_num()
  elif num_guessed > computer_num:
    print "A little too high. Try again:"
    guess_num()
  else:
    print "Great guess! You got it in only %s guesses" %(counter) 

guess_num()