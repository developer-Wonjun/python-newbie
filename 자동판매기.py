a = int(input("물건 값을 입력하시오. : "))

b = int(input("투입하실 1000원권의 갯수를 입력해 주세요 :"))
c = int(input("투입하실 500원권의 갯수를 입력해 주세요 :"))
d = int(input("투입하실 100원권의 갯수를 입력해 주세요 :"))

change = 1000 * b + 500 * c + 100 * d - a

e = change//500
change = change%500

f = change//100
change = change%100

g = change//10
change = change%10

print("반환 받으실 돈은 500원 {0}개, 100원 {1}개, 10원 {2}개 입니다.".format(e, f, g))
