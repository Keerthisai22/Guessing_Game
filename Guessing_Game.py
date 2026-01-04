import random
secret=random.randint(1,10)

print("\n--- Number Guessing Game (1 to 10) ---\n")

while True:
    guess=int(input("Enter the Guess="))
    
    if guess<secret:
        print("Too Low")
    elif guess>secret:
        print("Too High")
    else:
        print("Congratz! You guessed it correctly 🎉")
        break
    
    
