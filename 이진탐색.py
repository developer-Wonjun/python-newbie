from random import *

def search(list, value):
    low = 0
    high = len(list) -1

    while low <= high:
        middle = (low+high) // 2
        if list[middle] > value:
            high = middle - 1
        elif list[middle] < value:
            low = middle + 1
        else:
            return middle +1
    return "값이 존재하지 않습니다."

a = int(input("리스트의 항목 갯수를 입력 하시오.(최대 100) :"))
b = int(input("찾고싶은 값을 입력 하시오 :"))

c = sample(range(1,101), a)
c.sort()


print(search(c, b))
