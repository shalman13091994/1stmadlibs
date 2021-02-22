#we have bunch of space in a paragraph that is to filled by the user input (words they choose) =matlib

#suppose we want to create a string that says "subsribe to _____"

# youtuber="kylie Ying(youtube)"
#
# #few ways to do this
#
# print("subscribe to "+youtuber)
# print("subscribe to {}".format(youtuber))
# #fstring by adding f at the start of the string
# print(f"subscribe to {youtuber} ")

adj=input("enter your adjective: ")
verb1=input("enter your first verb")
verb2=input("enter your second verb")
famousperson=input("enter ur famous person")

matlib=f"computer programming is so {adj}! it \n makes me so excited all the time because oi love to {verb1}.Stay hyderated and {verb2} like you are {famousperson}"
print(matlib)