from random import *

lst = ["head", "tail"]


while (True):
    b = input("동전 던지기를 계속 하시겠습니까? (yes, no)")
    a = choice(lst)
    if b == "yes":
        print(a)
    else:
        break
    