import random
word_list =["ardvark","baboon","camel"]

lives = 6
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
display = []

for _ in range(len(chosen_word)):
    display+='_'
   

while end_of_game:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print("You've already guessed {guess} letter")
        
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current Position:{position}\n Current letter: {letter}\n Guessed letter:{guess}")
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives-=1
        if lives == 0:
            end_of_game = True
            print("You lose")
            
print(f"{''.join(display)}")

if "_" not in display:
    end_of_game = True
    print("You Won.")  
