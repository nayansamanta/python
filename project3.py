# hangman game 
import random

word_list=["apple" ,"orange" , "patato", "rice"]
word_chossen =random.choice(word_list)
# print(word_chossen)
lives=len(word_chossen)
display=[]
for letter in word_chossen:
    display +='_'
print(display)    

game_over=False
while not game_over:
    guess_letter=input("Guess a letter : ")
    for position in range(len(word_chossen)):
        letter=word_chossen[position]
        if letter==guess_letter:
            display[position]=guess_letter
        
    print(display)

    if guess_letter not in word_chossen:
        lives -=1
        if lives==0:
            game_over=True
            print("you lose!")
    if '_' not in display:
        game_over=True
        print("you win")