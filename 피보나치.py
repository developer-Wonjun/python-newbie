fiboList = {0:0, 1:1}

def fibm(n):
    if not n in fiboList:
        fiboList[n] = fibm(n-1) + fibm(n-2)
    return fiboList[n]

n = int(input("정수를 입력하시오:"))
print(n, "번째 피보나치 수는", fibm(n))