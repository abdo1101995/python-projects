# dics={"cs1":"python","cs2":"java","cs3":"Linear algebra","cs4":"math"}
# print(dics["cs1"])
# print(dics.keys())
# print(dics.values())
# print(dics.items())
# for key ,value in dics.items():
#     print(f"{key}:{value}")
# print("hiii")
# dics.clear()
# print(dics)
# del dics
# for i in range(1,10):
#     print(i)
#
# count=0
# while count<4:
#     print("hiii")
#     count+=1
#
# for i in range(10):
#     if(i==4):
#        break
#
#
# else:
#
#     print("loop ended")
#
#
# def function(x,y):
#     return x+y
#
# print(function(1,5))
#
# def myfunction(x,y):
#
#     print(f"my favorite language: {x}\nmy favorite color :{y}")
#
# myfunction("python","red")
#
# def func(x=10,y=0):
#
#     print(f"my favorite language: {x}\nmy favorite color :{y}")
# func()
# func(1,2)
# func(2)
#


def func2(**args):

    print(args)
    print("______________________________________")

func2(x="ahmed",y="ali")


def myFun(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}== {value}")


# Driver code
myFun(first='Geeks', mid='for', last='Geeks')

print(round(5.2342,3))