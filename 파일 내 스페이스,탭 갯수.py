def a(path):
    infile = open(path, "r")
    spaces = 0
    tabs = 0

    for line in infile:
        line = infile.readline()

        spaces += line.count(" ")
        tabs += line.count("\t")
    return spaces, tabs
    
    infile.close()

name = input("파일 이름을 입력하시오.")

spaces, tabs = a(name)

print("스페이스 수 : {0}, 탭 수 : {1}".format(spaces, tabs))

