import random

word_list = ["ardvark", "baboon", "camel"]
the_word = random.choice(word_list)

#loop throw the word to print "_" instead of each letter
display = []
for _ in range(len(the_word)):
    display += "_"

print(display)

game_over = True
live_score = 6

while game_over:
    guess = input("Provide a letter as your guess: ").lower()

    if guess in the_word:

        for index, elem in enumerate(the_word):
            if guess == elem and display[index] != "_":
                live_score -= 1
                print(live_score)
            elif guess == elem and display[index] == "_":
                display[index] = guess
                break
    else:
        live_score -= 1
        print(live_score)
    
    print(display)
    if "_" not in display:
        game_over = False
        print("you Won!")
    if live_score == 0:
        game_over = False
        print("You lose!")