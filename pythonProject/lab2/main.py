# import re
# import random
# #task1
# def mkarray(length,step):
#     mlist=list(range(0,length,step))
#     print(mlist)
#
# mkarray(10,1)
#
# #task2
# def dividible(number):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number%3==0:
#         print("Fizz")
#     elif number%5==0:
#         print("buzz")
#
#
# dividible(5)
# dividible(6)
# dividible(15)
#
# #task3
# def sreverse(str):
#     str=str[::-1]
#     return str
#
#
# print(sreverse("ahmed"))
#
#
# #task4
# regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# def checkne(name,email):
#         if len(name) == 0:
#             print("null")
#         else:
#             print(" " + name)
#
#
#         if not re.fullmatch(regex, email):
#                 print("Invalid email")
#
#         else:
#          print("valid email")
#
# checkne("ahmed","abomhade@gmail.com")
#
# #task5
#
# def subname(s):
#     longest = s[0]
#     current = s[0]
#     for c in s[1:]:
#         if c >= current[-1]:
#             current += c
#             if len(current) > len(longest):
#                 longest = current
#         else:
#             current = c
#
#     print("Longest substring in alphabetical order is:", longest)
#
#
# print(subname('abdulrhman'))
#
#
#
# #task6
# count=0
# sum=0
#
# while True:
#     number = input("enter number")
#     if number=='done':
#         break
#     try:
#         nm=int(number)
#         count=count+1
#         sum=sum+nm
#
#     except:
#
#       print('Enter a valid number')
#
# print("count:",count,"total:",sum,"average:",sum/count)
#
# #task7
#
# words=["java","python","computer vision","math","machine learning","deep learning","software"]
#
#
# word = random.choice (words)
#
# print ("Guess the characters")
#
# guesses = ''
#
# # any number of turns can be used here
# turns = 7
#
# while turns > 0:
#     failed = 0
#     for char in word:
#
#         if char in guesses:
#             print (char)
#
#         else:
#             print ("_")
#             failed += 1
#
#     if failed == 0:
#
#         print ("You Win")
#
#         print ("The word is: ", word)
#         break
#
#     guess = input ("guess a character:")
#
#     guesses += guess
#
#     if guess not in word:
#
#         turns -= 1
#         print ("Wrong")
#
#         print ("You have", + turns, 'more guesses')
#
#         if turns == 0:
#             print ("You Loose")


import re
def mklist(length,start):

    mklist=list(range(start,length,1))

    print(mklist)

mklist(10,1)


def divisiblen(number):

    if number%5==0 and number%3==0:
        print("FizzBuzz")
    elif number%3==0:
        print("Fizz")
    elif number%5==0:
        print("buzz")

divisiblen(15)
divisiblen(10)
divisiblen(30)

def reverse(name):
    name=name[::-1]
    print(name)

reverse("salah")

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

name=input("enter your name")
email = input("enter your email")

try:
    if str(name)=="":
            print("NULL")
    else:
        print(name)

    if not re.fullmatch(regex,email):
            print("invalid email",email)

    else:
        print("valid email",email)
except:
        print("invalid enter again")

def sublong(name=""):
     sorted_name=sorted(name)
     sort_size=len(sorted_name)
     if sort_size>4:
         return sorted_name[1:5]
     else:
         return sorted_name

print(sublong("abdulrhman"))
count=0
sum=0
while True:
    number=input("enter number")
    if number=="done":
        break
    try:
        nm=int(number)
        count=count+1
        sum=sum+nm
    except:
        print("try correct number")
print(f"count :{count}\n total:{sum}\n average:{sum/count}")

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
        print("You have", + turn, 'more guesses')
    if turn == 0:
         print ("You Loose")
