import re
import string
import random
import os.path
def lfname():
    # firstname and last name
    fname = input("enter first name:")
    lname = input("enter last name:")
    info = '_'.join([fname, lname])
def email():
    # email

    while True:
        fe = open('user.txt', 'a')
        email = input("enter email")
        fe.write(email)
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if (re.fullmatch(regex, email)):
            print("Valid Email")
            break
        else:
            print("Invalid Email")
            break

def password():
    fp = open('user.txt', 'a')
    password = input("enter passwd")
    fp.write(password)

    flag = 0
    while True:
        if (len(password) < 8):
            flag = -1
            break
        elif not re.search("[a-z]", password):
            flag = -1
            break
        elif not re.search("[A-Z]", password):
            flag = -1
            break
        elif not re.search("[0-9]", password):
            flag = -1
            break
        elif not re.search("[_@$]", password):
            flag = -1
            break
        elif re.search("\s", password):
            flag = -1
            break
        else:
            flag = 0
            print("Valid Password")
            break

    if flag == -1:
           print("Not a Valid Password")

def mobile_number():
    moblie_phone = input("enter phone_number")
    ph = ['011', '012', '015', '010']
    flag = 0
    while True:
        if (len(moblie_phone) < 11):
            flag = -1
            break
        if moblie_phone[:3] not in ph:
            flag = -1
            break
        elif not re.search("[0_9]", moblie_phone):
            flag = -1
            break

        else:
            flag = 0
            print("Valid mobile_phone")
            break

    if flag == -1:
        print("Not Valid a mobile_phone")
def mregister():
    lfname()
    email()
    password()
    mobile_number()