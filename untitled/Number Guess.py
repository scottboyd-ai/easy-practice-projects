import random

print ("I'm thinking of a number between 1 and 100")

num = random.randint(1,100)

guess_num = 0

while guess_num < 100:
    print ("What's the number?")
    user_num = int(input())

    guess_num = guess_num + 1

    if user_num == num:
        print ("You crafty son of a bitch")
        break
    elif user_num > num:
        print ("Guess lower")
    elif user_num < num:
        print ("Guess higher")