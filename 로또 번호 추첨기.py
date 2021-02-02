import random

num = range(1, 46)

E = sorted(num)
num_list = random.sample(num, 6)

D = sorted(num_list)

A = random.sample(num_list, 5)

C = list(set(num_list).difference(A))

B = sorted(A)


print("제 948회 로또 행운의 번호는 {0}이고, 보너스 번호는 {1}입니다 부자되세요 ~!.".format(B, C))






