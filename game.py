import random
n=5
choice=random.randint(0,9)
print("lets start a game with rinki...")
while(n>=0):
     Guess=int(input("Enter your Guess:\n"))

     n=n-1
     if Guess>choice:
            print("The number you guessed is greater")
     elif Guess<choice:
            print("The number you guessed is smaller")
     else:
            print("Congo....you win a game")    
