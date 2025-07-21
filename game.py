import random
print("Hi🖐👋! Welcome to my game : Guessing a number.\nYou have 10 chances to guess the number.\nStart🎷! ") 
low = int (input ("Set a low Value") ) 
high=int (input ("Set a high Value") ) 
print (f"You have to guess number between{low}and{high}within 7 chances.\nStart!") 
num=random.randint(low, high) # to get a random number
chances=7 #chances
g=0 # initially 0 guesses 
while chances > g :
    g=g+1
    guess =int (input("Guess a number:")) 
    if guess==num :
        print("🤩WOW! You guessed correct number:",+num) 
        break
    elif g>=chances:
        print("Sorry😥 ! Correct Number is :",+num) 
    elif guess>num:
        print ("Too high! try low") 
    elif guess<num:
        print ("Too low! try high") 