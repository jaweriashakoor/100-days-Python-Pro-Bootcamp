stages=['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''']


import random
logo='''888                                                           
888                                                           
888                                                           
88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
888  888.d888888888  888888  888888  888  888.d888888888  888 
888  888888  888888  888Y88b 888888  888  888888  888888  888 
888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                             888                              
                        Y8b d88P                              
                         "Y88P"   '''
print(logo)
life=6
word_list=["camel","Cow","Goat","Buffalo"]
chosen_word=random.choice(word_list)
print(chosen_word)
placeholder=""
word_length=len(chosen_word)
for position in range(word_length):
    placeholder+="_"
print(placeholder)

game_over = False 
correct_letter=[]

while not game_over:
    guess=input("Guess the letter:").lower()
    display=""
    for letter in chosen_word:
        if letter == guess:
            display+=letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display+=letter
        else:
            display+="_"

    
    print(display)
    if guess not in chosen_word:
        life-=1
        if life==0:
            game_over=True
            print("You Lose")
    
    
    if "_" not in display:
        game_over=True
        print("You Win")
    print(stages[life])