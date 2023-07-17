# Guess the number game in Python
import random
print("The Number Guessing Game")
#computer will select random number
num = random.randint(1,20)

chances =0
print("Guess a Number between 1 to 19")
while chances < 5:  # here taking 5 guessing chances, incase we have to take '3' ---> chances < 3
    guess = int(input("enter any number: "))
    if guess == num:
        print("congrats! you won")
        break
    elif guess > num :
        print("your guess is higher. pls select a lower number", guess)
    else:
        print("your guess is lower. pls select higher number",guess)
    chances +=1

if not chances > 5:
    print("sorry! you losse to guess")


