#guess the number

import random
n = random.randint(1,100)

#print (n)
print ("Welcome to the Guess the Number Game.")
inp = int(input("Guess the number between 1 and 100: "))

while inp != n :
    if inp > n :
        print ('You have entered bigger number.')
        inp = int(input("Guess the number between 1 and 100: "))
    elif inp < n :
        print ('You have entered smaller number.')
        inp = int(input("Guess the number between 1 and 100: "))
print ("That's correct! Well Done")
            


