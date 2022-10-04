import random
words=["ahmed","mohamed","adel","boody","ibrahim"]

word=random.choice(words)
turn=7
guessess=""
while turn>0:

    failed=0
    for char in word:
        if char in guessess:
            print(char)

        else:
         print("_")
         failed+=1

    if failed==0:
        print("you win")
        print("the word",word)
        break
    guess=input("guess the character")
    guessess+=guess
    if guess not in word:
        turn-=1
        print("Wrong")
        print("You have",  turn, ' guesses')
    if turn == 0:
         print ("You Loose")
