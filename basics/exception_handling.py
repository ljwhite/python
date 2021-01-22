import random

# while True:
#     try:
#         number = int(input("Please enter a number : "))
#         break
#
#     except ValueError:
#         print("You didn't enter a number")
#     except:
#         print("An unknown error occurreed")
#
# print("Thank you for entering a number")

# guessing game
x = random.randrange(1,11)
while True:
    number = int(input("Please guess a number from 1-10 : "))
    if number == x:
        print("Congrats! You guessed it")
        break
    else:
        print("nope! try again...")