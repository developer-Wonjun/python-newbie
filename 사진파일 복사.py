infilename = input("파일이름을 입력하시오.")
outfilename = input("파일이름을 입력하시오.")

infile = open(infilename, "rb")
outfile = open(outfilename, "wb")

while True:
    a = infile.read(1024)

    if not a:
        break

    outfile.write(a)


infile.close()
outfile.close()

print("사진이 {0}로 복사되었습니다.".format(outfilename))