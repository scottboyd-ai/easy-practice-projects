roll = True
import random

print("Let's roll a dice")

while roll == True:
    print (random.randint(1,6))
    print ("Do you want to roll again? yes or no")
    cont = input()
    if cont == "yes":
        roll = True
    elif cont == "no":
        roll = False
