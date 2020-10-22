'''
Desimir Berardo
CS100 113
10/22/2020
'''

import random

rand = random.randint(0, 50)
count = 1
number = rand

print('im thinking of a number between 1 and 50. You have five tries to guess it')
while True:
    if count > 5:
        print('Game over! The number was: ' + str(number))
        break
    guess = int(input('Guess ' + str(count) + "?: "))
    count += 1
    if guess > number:
        print(str(guess) + ' is too high')
    elif guess < number:
        print(str(guess) + ' is too low')
    elif guess == number:
        print(str(guess) + ' is correct! You win!!!!')
        break