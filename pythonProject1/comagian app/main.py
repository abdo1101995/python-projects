import re
import string
import random
import os.path
from register import mregister
from loginn import login
from camproject import editproject
from camproject import displayall
from camproject import searchofprojects
from camproject import deleteproject

def mainmenu():

    while True:
        option=input("enter 1 for register\n2 for login\n3 for editprojects \n4 for display projects \n5 for search projects\n6 for delete\n7 Exit")

        if option=='1':
             mregister()
        elif option=='2':
            login()
        elif option=='3':
            editproject('1')
            break
        elif option=='4':
             displayall()
        elif option=='5':
            searchofprojects()
        elif option=='6':
            deleteproject('1')
        elif option=='7':
            break;



mainmenu()

