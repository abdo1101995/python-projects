from camproject import projectinfo
def login():
   em=input("email: ")
   passw =input("Password: ")
   f = open("user.txt", "r")

   for line in f.readlines():

       if (em in line) and (passw in line):

           print("Login successful!")
           projectinfo(1)
           return True

   print("Wrong username/password")
   return False