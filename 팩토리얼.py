def factorial(n):

    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


num = int(input("수를 입력하세요."))
print(factorial(num))