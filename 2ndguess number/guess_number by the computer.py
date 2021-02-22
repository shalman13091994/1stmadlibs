#we have secret number and we want computer to guess it without saying the number
import random

def computer_guess(x):
    low=1
    high=x

    # we are replying to computer in our input in terms of string so we are giving
    feedback='' #decalaring feedback as string
    while feedback!='c': #c is for correct
        # low!=high  if both equals then it will execute final statement
         if low!=high:
           guess=random.randint(low,high)#(1,x)
         else:
          guess =high #could also be high because high=low

         feedback=input(f"Is {guess} is low(l),high(h),correct(c): ")
         if feedback =='h':
               high=guess-1
         elif feedback=='l':
              low=guess+1

    print(f"the computer guessed your number, {guess}, correctly!")

computer_guess(10)
