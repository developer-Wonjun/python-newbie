from random import randint

a = int(input("주사위를 굴릴 횟수를 입력하시오 : "))

b = [0,0,0,0,0,0,0,0,0,0,0,0,0]

for c in range(a):
    d = randint(1, 6)
    e = randint(1, 6)
    b[d + e] += 1
for c in range(2, 13):
    print(c, b[c])