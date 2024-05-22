from game_data import data
import random

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

continue_game = True

choice1 = random.choice(data)
print(f"\nCompare A : {choice1['name']}, a {choice1['description']}, from {choice1['country']}")
print(vs)

user_score = 0

while continue_game:

    choice2 = random.choice(data)

    if choice1 == choice2:
        choice2 = random.choice(data)
    print(f"Compare B : {choice2['name']}, a {choice2['description']}, from {choice2['country']}")

    user_choice = input("\nWho will have more followers\n")
    if choice1['follower_count'] > choice2['follower_count'] and user_choice == 'A':
        user_score += 1
        print(f"\nYou are correct...Your score is {user_score}\n")
        print(f"Compare A : {choice1['name']}, a {choice1['description']}, from {choice1['country']}")
        print(vs)
    elif choice1['follower_count'] > choice2['follower_count'] and user_choice == 'B':
        print(f"\nYou are wrong....Your final score is {user_score}\n")
        break
    elif choice1['follower_count'] < choice2['follower_count'] and user_choice == 'B':
        user_score += 1
        print(f"\nYou are correct...Your score is {user_score}\n")
        choice1 = choice2
        print(f"Compare A : {choice1['name']}, a {choice1['description']}, from {choice1['country']}")
        print(vs)
    elif choice1['follower_count'] < choice2['follower_count'] and user_choice == 'A':
        print(f"\nYou are wrong....Your final score is {user_score}\n")
        break
    else:
        print("Enter only 'A' or 'B'")
        break
        

