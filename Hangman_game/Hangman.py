#Hangman game
from random import *

situation=['''
     ____________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / ]
     |
 jgs_|___
''',
'''
     ____________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
 jgs_|___
'''
,
'''
     ____________
     |/      |
     |      (_)
     |      \|/
     |       |
     |    
     |
 jgs_|___
'''
,
'''
     ____________
     |/      |
     |      (_)
     |      \|
     |       |
     |     
     |
 jgs_|___
'''
,
'''
     ____________
     |/      |
     |      (_)
     |       |
     |       |
     |      
     |
 jgs_|___
'''
,
'''
     ____________
     |/      |
     |      (_)
     |      
     |       
     |      
     |
 jgs_|___
'''
,
'''
     ____________
     |/      |
     |     
     |      
     |       
     |      
     |
 jgs_|___
'''
           ]

from Hangman_word import word_list
word=choice(word_list)

print('''
888                                                           
888                                                           
888                                                           
88888b.     8888b.  88888b.    .d88bbb  88888b.d88b.     8888b.  88888b.  
888 "88b      "88b  888 "88b  d88P"88b  888 "888 "88b      "88b  888 "88b 
888  888  .d888888  888  888  888  888  888  888  888  .d888888  888  888 
888  888  888  888  888  888  Y88b 888  888  888  888  888  888  888  888 
888  888  "Y888888  888  888   "Y88888  888  888  888  "Y888888  888  888 
                                   888                              
                              Y8b d88P                              
                               "Y88P"                               
''')   #logo

# print(f"the word was chosen is {word}")

word_display=[]
word_len=len(word)

for i in range(word_len):
    word_display+="_"
print(word_display)

count_=1
lives=6

while count_!=0 and lives!=0:

    guess = input("Guess one character: ").lower()
    count_=0

    if (guess not in word) or (guess in word_display):
        lives-=1
        print("Your character is wrong or duplicated.")
    else:
        print("Your character is correct.")

    for i in range(word_len):
        if guess == word[i]:
            word_display[i] = word[i]

    if '_' in word_display:
        count_+=1


    print(situation[lives])
    print(f"Your current lives: {lives}")
    print(word_display)

    if count_ == 0:
        print(f"YOU WIN!\nThe word correct ís \"{word}\"")
    if lives==0:
        print("YOU LOSE! :(")
