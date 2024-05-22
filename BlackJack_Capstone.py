import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

computer_cards = []
user_cards = []

for key in range(0,2):
    random_choice = random.choice(cards)
    computer_cards.append(random_choice)

for key in range(0,2):
    random_choice = random.choice(cards)
    user_cards.append(random_choice)
    
print(f"The computer's cards are [{computer_cards[0]},*]")
print(f"Your cards are {user_cards}")

computer_card_sum = 0
for key in computer_cards:
    computer_card_sum += key
    
user_card_sum = 0
for key in user_cards:
    user_card_sum += key

draw_next_card = True
while draw_next_card :
    choice = input("Enter 'Hit' if you want to draw next card or 'Stand' if you want to end")
    
    if choice == "Hit":
        user_cards.append(random.choice(cards))
        

# if computer_card_sum == 21 & user_card_sum == 21:
#     print("Draw")
# elif user_card_sum == 21:
#     print("BlackJack!!! You win")
# elif computer_card_sum == 21:
#     print("Computer has the blackjack!!! You lose")










