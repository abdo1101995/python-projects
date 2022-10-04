from datetime import datetime as dt
import string
def projectinfo(ownerid):
    title=input("enter the title")
    details=input("enter details")
    target=input("enter target")
    start=validdate(input("enter start_date:"))
    end=validdate(input("enter end_date:"))
    idofowner = str(ownerid)
    info = ':'.join([idofowner, title, details, target, start, end])
    writeprojectsinfile(info)

def validdate(date):
    while True:
        try:
            dt.strptime(date,"%Y-%m-%d")
        except ValueError:
            date = input("date should be like this '2022-01-15' : ")
        else:
            return date

def writeprojectsinfile(info):
    write = open('projects.txt', 'a', encoding='UTF-8')
    info = info + '\n'
    write.write(info)
    write.close()

def displayall():
    try:
        read = open('projects.txt', 'r')
        result = read.readlines()
        try:
            for i in result:
                value = i.split(':')
                print(value[1], value[2], value[3], value[5])
        except IndexError:
            print("file empty")
            if result:
                print("file empty")
                return 0
    except FileNotFoundError:
        return 0
    else:
        read.close()
    return 0

def editproject(idowner):
    try:
        read = open('projects.txt', 'r')
        result = read.readlines()
        for i in range(len(result)):
            index = result[i].split(':')
            if index[0] == idowner:
                print("what are you want to change?")
                sectionch = input("if wont change title press (t), details pres (d), total target (tt),"
                             "start date (s) or end date (e) ")
                result[i] = changeonproject(sectionch, index)
                break
        read = open('projects.txt', 'w')
        read.writelines(str(result))
    except FileNotFoundError:
        print("the file isn't exist")
    else:
        read.close()

def changeonproject(scch, project):
    while True:
        if scch == 't':
            project[1] = input("what are you change title for? : ")
            return project
        elif scch == 'd':
            project[2] = input("You change details for what? : ")
            return project
        elif scch == 'tt':
            project[3] = input("You change details for what? : ")
            return project
        elif scch == 's':
            project[4] = validdate(input("You change details for what? : "))
            return project
        elif scch == 'e':
            project[5] = validdate(input("You change details for what? : "))
            return project
        else:
            scch = input("you can chose form [t,d,tt,s,e] nothing else : ")


def deleteproject(idowner):
    try:
        read = open('projects.txt', 'r')
        result = read.readlines()
        index = []
        for i in result:
            if i.split(':')[0] == idowner:
                index = i
                break
        read = open('projects.txt', 'w')
        try:
            result.remove(index)
        except ValueError:
            print("not found")

        read.writelines(result)
    except FileNotFoundError:
        print("the file isn't exist")
    else:
        read.close()

def searchofprojects():
    date = validdate(input("please, write the date you search for."))
    try:
        read = open('projects.txt', 'r')
        result = read.readlines()
        try:
            for i in result:
                value = i.split(':')
                if value[5] == date:
                    print(value[1], value[2], value[3], value[5])
        except IndexError:
            print("file empty")
            if result:
                print("file empty")
                return 0
    except FileNotFoundError:
        return 0
    else:
        read.close()
    return 0
