import random
print("1부터 10000사이의 숫자를 맞추시오")

a = random.randint(1, 10000)
n = 0
b = 0

while a != b:
    b = int(input("숫자를 입력하시오 :"))

    if a > b:
        print("높음!")
    elif a < b:
        print("낮음!")
    else:
        print("정답")
    
    n = n + 1

print("축하합니다. 시도횟수 : {0}".format(n))