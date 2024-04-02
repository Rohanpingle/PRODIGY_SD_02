
import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
          guess = int(input("Guess the number (between 1 and 100): "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} correctly!")
                print(f"It took you {attempts} attempts to win the game.")
                break  
        except ValueError:
            print("Please enter a valid number.")

guess_the_number()
