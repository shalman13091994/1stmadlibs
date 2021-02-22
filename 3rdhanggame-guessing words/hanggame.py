from words import words
import random
import string #(string.ascii_uppercase)

def get_validwords(words):
    word=random.choice(words)#randomly choose the words from the list

    ## this loop is for removing the space and -
    while "-" in words or " "in word:
        word=random.choice(words)#randomly choose the words from the list (words.py)


    return word.upper()


#guessing the name by the letters one by one from the words

def hangman():
   word=get_validwords(words)
   word_letters=set(word)#letters in the word is in the form of set -immutable
   alphabets=set(string.ascii_uppercase) #ALL ENGLISH ALPHABETS
   usedletter=set( )#what the user has guessed that to be stored
   #lives if it became zero it will end the game

   lives=6


   while len(word_letters) > 0 and lives >0:  # lenght of the letter greater than zero
       #letter that we used
       #' '.join['a','b','cd']---> 'a b cd' its separated by space
       print("you have", lives,"lives left and you have used these letters: " ,' '.join(usedletter))

       #what current word that's we guessed like (APP-E)

       # single line if else and for loop it should be in list
       #it will execute for loop first then if else
       # [i for i in word] # if in usedletter

       word_list=[i if i in usedletter else '-' for i in word]
       print("current word: ", ' '.join(word_list))

       #getting user input
       user_input=input("Guess word: ").upper()

        #if inpput is T from alphabets will be add with the empty set
        # for adding the guessed letter which i haven't used from the word

       if user_input in alphabets - usedletter: #usedletter is empty set
            usedletter.add(user_input)

            #to remove the guessed letter from the word
      #example: guess word:'T' then T will be removed from the word_letter
    # guess word:'T' will removed from the wordset (Tiger) and T will be display in the current word

            if user_input in word_letters:
                word_letters.remove(user_input)

              #if user already guessed letter in usedletter

            else:
                lives=lives-1 #takes away a live if guessed letter is wrong
                print("letter is not in word")

       # to tell that same word has been used
       elif user_input in usedletter:
                    print(f"you already used that letter")
       #if it is other than string then we have show this
       else:
                    print("Invalid character!! Try again")

    #while loop exits here when len(word_letters) == 0 and lives==0


   if lives==0:
       print("you died, SORRY.the word was",word)
   else:
       print(f"Hurray!!!! you found the word is {word} ")

hangman()