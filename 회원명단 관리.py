def menu():
    print("1. 회원 리스트 출력")
    print("2. 회원 추가")
    print("3. 회원 삭제")
    print("4. 이름 변경")
    print("9. 종료")
    
lst = []

a = 0

while a != 9:
    
    menu()

    a = int(input("메뉴를 선택 하시오 : "))

    if a == 1:
        print(lst)
    elif a == 2:
        name = input("추가할 이름을 입력하시오 :")
        lst.append(name)
        
    elif a == 3:
        dename = input("삭제할 이름을 입력하시오 :")
        if dename in lst:
            lst.remove(dename)
        else:
            print("존재하지 않는 이름입니다.")
    
    elif a == 4:
        oldname = input("변경하고싶은 이름을 입력하시오 : ")
        if oldname in lst:
            newname = input("새로운 이름을 입력하시오 : ")
            index = lst.index(oldname)
            lst[index] = newname
        else:
            print("존재하지 않는 이름입니다.")


            
print("프로그램을 종료합니다.")
