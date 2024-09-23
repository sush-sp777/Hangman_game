import random
from hangman_logo import logo
print(logo)
empty=6
#creating blank spaces
display=[]
#list of words
from hangman_logo import word_list
choosen_word=random.choice(word_list) 
#print(choosen_word) #randomly choosen word printed out
for _ in range(len(choosen_word)):
    display+="_" #it displays blank places equals to no of letters in choosen word
end_of_game=False

while not end_of_game:
    guess=input("guess the letter:") #user guess the letter
    guess.lower()
    print(guess)    
    if guess in display:
      print(f"You already guessed letter {guess}.Please try another letter")  

    for i in range(len(choosen_word)):
        letter=choosen_word[i] 
        if letter==guess:
            display[i]=letter #letter guess by the user appended to display list
    if guess not in choosen_word:
        print(f"You choose wrong letter.Please try another")
        empty-=1
        if empty==0:
            end_of_game=True
            print("you lose, Better luck next time")
    from hangman_logo import stages
    print(stages[empty]) #stages are printed according to users input
    print(display) #displaying the list of letters
    if "_" not in display:
        end_of_game=True
        print("Congradulations!You win") 
   