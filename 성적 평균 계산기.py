lst = []
value = 0
studeonts = int(input("학생수를 입력하세요. :"))
for i in range(studeonts):
    num = int(input("성적을 입력하시오 :"))
    lst.append(num)

for j in lst:
    value = value + j



m = 0
for k in range(len(lst)):
    if lst[k] >= 80:
        m += 1

print("성적 평균은 {0}입니다.".format(value/studeonts))
print("80점을 넘기는 학생 수는 {0}명 입니다.".format(m))
