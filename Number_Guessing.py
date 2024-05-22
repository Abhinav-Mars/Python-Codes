import random
numbers = []

for key in range(1,101):
    numbers.append(key)
    
global thinking_number

thinking_number = random.choice(numbers)

def number_check(number):
    if number == thinking_number:
        return "success"
    elif number != thinking_number:
        if number > thinking_number:
            if number - thinking_number > 20:
                print(f"The number you guessed is too higher\n")
            elif number - thinking_number <= 20:
                print(f"The number you guessed is a little bit higher\n")
        elif number < thinking_number:
            if thinking_number - number > 20:
                print(f"The number you guessed is too lower\n")
            elif number - thinking_number <= 20:
                print(f"The number you have guessed is a little bit lower\n")
            
print("\nWELCOME TO THE NUMBER GUESSING GAME!!!!!\n")

choice = input("Enter 'easy' or 'hard'\n")
print("\n")


if choice == "easy":
    number_of_tries = 10
elif choice == "hard":
    number_of_tries = 5
    
while number_of_tries > 0:
    print(f"You have {number_of_tries} attempts remaining")
    guessed_number = int(input("Guess the number\n"))
    
    if number_check(guessed_number) == "success":
        print(f"Yes you are right.The correct number is {guessed_number}...YOU WIN\n")
        break
    number_of_tries = number_of_tries - 1
    
if number_of_tries == 0:
    print("Out of attempts...YOU LOSE") 
    
    