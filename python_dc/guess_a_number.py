# Number 1 - Guess a Number

secret_number = 5

guess_no = input('I am thinking of a number between 1 and 10, what is the number? ')


while guess_no != secret_number:
    if guess_no > 5:
        print('Nope! Try again. ')
        guess_no = input('I am thinking of a number between 1 and 10, what is the number? ')
    if guess_no < 5:
        print('Nope! Try again. ')
        guess_no = input('I am thinking of a number between 1 and 10, what is the number? ')
    else:
        break
        
print('Good job! you guessed the right number!')
   

# Number 2 - Give High-Low Hint

secret_number = 5

guess_no = input('I am thinking of a number between 1 and 10, what is the number? ')


while guess_no != secret_number:
    if guess_no > 5:
        print('Too high! Try again. ')
        guess_no = input('I am thinking of a number between 1 and 10, what is the number? ')
    if guess_no < 5:
        print('Too low! Try again. ')
        guess_no = input('I am thinking of a number between 1 and 10, what is the number? ')
    else:
        break
        
print('Good job! you guessed the right number!')

# Number 3 - Randomly Generated Secret Number

import random 
my_random_number = random.randint(1 , 10)


guess_no = input('I am thinking of a number between 1 and 10, what is the number? ')


while guess_no != my_random_number:
    if guess_no > my_random_number:
        print('Too high! Try again. ')
        guess_no = input('I am thinking of a number between 1 and 10, what is the number? ')
    if guess_no < my_random_number:
        print('Too low! Try again. ')
        guess_no = input('I am thinking of a number between 1 and 10, what is the number? ')
    else:
        break
        
print('Good job! you guessed the right number!')

# Number 4 - Limit Number of Guesses
import random

my_random_number = random.randint(1 , 10)

guess_no = input('I am thinking of a number between 1 and 10, what is the number? You only have five guesses! ')

guess = 5

while guess_no != my_random_number:
    if guess_no > my_random_number:
        guess = guess - 1
        print('Too high! Try again. You now have ' + str(guess) + ' guesses left!')
        guess_no = input('I am thinking of a number between 1 and 10, what is the number? ')
    if guess_no < my_random_number:
        guess = guess - 1
        print('Too low! Try again. You now have ' + str(guess) + ' guesses left!')
        guess_no = input('I am thinking of a number between 1 and 10, what is the number? ')
    else:
        break
        
print('Good job! you guessed the right number!')




