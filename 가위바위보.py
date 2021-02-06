import random

lst = ["가위", "바위", "보"]
lst.sort()

a = random.sample(lst, 1)

user = input("가위 / 바위/ 보 ! :")
userlst = []
userlst.append(user)

print( "컴퓨터 : {0}".format(a))
print("사용자 : {0}".format(userlst))

if userlst == ["바위"]:
    if a == ["보"]:
        print("컴퓨터 승리!")
    elif a == ["가위"]:
        print("사용자 승리!")
    elif a == ["바위"]:
        print("비겼네 ~")

elif userlst == ["가위"]:
    if a == ["바위"]:
        print("컴퓨터 승리!")
    elif a == ["가위"]:
        print("비겼네~")
    elif a== ["보"]:
        print("사용자 승리!")

elif userlst == ["보"]:
    if a == ["가위"]:
        print("컴퓨터 승리!")
    elif a == ["바위"]:
        print("사용자 승리!")
    elif a == ["보"]:
        print("비겼네~")