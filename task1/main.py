#task1
vowels=['a','i','e','o','u']
n1="ahmed"
n2="abdelrhman"
count = 0

for letter in n2:
    if letter in vowels:
        count += 1
print(count)

#task2
names=["yashin","bahaa","ali","sameh","ibrahim"]
names.sort()
print(names)

names.sort(reverse=True)
print(names)
#task3
coll="iti ahmed iti ali iti2"

print(coll.count("iti"))


vowels=['a','i','e','o','u']
n1="ahmed"
n2="abdelrhman"


for letter in n2:
    if letter.lower()  in vowels:
       n2=n2.replace(letter,'')


print(n2)

#task4
str1="iti"
str2="duration"
str3="king"

print(str3.find('i'))
#task5
listofnum=[]
for i in range(3):
    listofnum.insert(i, [((i+1)*(j+1)) for j in range(i+1)])
print(listofnum)

#task6

n=4
k=n*2-2
for i in range(n):
    for j in range(0, k):
        print(end=" ")


    k = k-2
    for j in range(i+1):
        print("* ", end="")
    print("\n")
n=input("enter number")
for i in range(int(n)):

    for j in range(i+1):

        print("*",end="")

    print("\n")
n = input("enter number")

for i in range(int(n)):
    for k  in range(k-i):
        print(" ")
    for j in range(i+1):

        print("*",end="")

    print("\n")

list=[]



for i in range(3):
    list.insert(i,[2*(j+1) for j in range(i+1)] )

print(list)


