#guessing a random number from the computer using random(default)

import random

def guess(x):
    # random.randint will provide the random integers
    #thus, start with off 1 i.e.,..(1,x)

    random_num=random.randint(1,x) #there should be two argument in default ()

    # initialisation of local variable 'choose'

    choose=0
    while choose!=random_num:

        choose=int(input(f"enter the number between 1 and {x}: "))
#to give hint so that we can find the computer's guessed number

        if choose >random_num:
            print("entered number is too high")
        elif choose < random_num:
            print("entered number is too low")

#when while choose equals the guessed number it will break the if loops directly execute this statement

    print(f"hurray!!!, you have guessed correct number is {random_num}")




guess(10)

