import random

word_list = ['bottle','umbrella','phone']

print(word_list)
selected_word = random.choice(word_list)
display = []

lives = 1
print("You will have 7 lives")
for letter in selected_word:
    display += '_'
print(display)

continue_game = True

while continue_game:
    guess = input("Enter a letter : ").lower()
    lives += 1
    for pos in range(len(selected_word)):
        if selected_word[pos] == guess:
            display[pos] = guess
    print(display)

    if lives > 7 :
        continue_game = False
        print("End of lives ! You Lose")
    elif lives < 8 :
        if '_' not in display :
            continue_game = False
            print("Hurray...You win!!")
        else :
            continue_game = True
        
        

    

