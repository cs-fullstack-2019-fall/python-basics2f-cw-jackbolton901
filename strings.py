# Afternoon Classwork
# Problem 1

greeting = "Hello"
myName = "Jack"
myAge = "29"
print(greeting + " " + myName + "!!! I hear that you are " + myAge + " today.")
print(f'{greeting} {myName}!!! I hear that you are {myAge} today.')
#
# # Problem 2
#
passW = input("Enter a password  ")
guessW = input("What do you think the password is?  ")
while guessW != passW:
    guessW = input("Guess Again!!  ")

# Problem 3

rang = range(0, 50 + 1, 1)
for x in rang:
    print(f'{x} {x} {x}')


# Problem 4

import random

rand1 = random.randint(1, 5)
randguess = 0
while randguess != rand1:
    randguess = int(input("What do you think the number is?  "))
