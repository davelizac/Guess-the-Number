from Art import logo
import random

print(logo)

print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.")

def random_number():
    chosen_number = random.choice(range(1, 101))   
    return chosen_number

number_to_guess = random_number()

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

def attempts_number():
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5

attempts = attempts_number()

print(f"You have {attempts} attempts remaining to guess the number.")

def guessing_the_number(attempts):   
    
    while attempts != 0:
        users_guess = int(input("Make a guess: "))
        
        if users_guess != number_to_guess and users_guess < number_to_guess:
            attempts -= 1
            print(f"Your guess is too low\nYou have {attempts} attempts remaining")
        if users_guess != number_to_guess and users_guess > number_to_guess:
            attempts -= 1
            print(f"Your guess is too high\nYou have {attempts} attempts remaining")
    
        if users_guess == number_to_guess:
            return f"You got it! {number_to_guess}"
            
        if attempts == 0:
            return f"The number was: {number_to_guess}. You lose!"

game = guessing_the_number(attempts)

print(game)
 


