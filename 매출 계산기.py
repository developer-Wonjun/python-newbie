infilename = input("파일 이름을 입력하시오.")
outfilename = input("파일 이름을 입력하시오.")

infile = open(infilename, "r")
outfile = open(outfilename, "w")

sum = 0
count = 0

for line in infile:
    dailysale = int(line)

    sum += dailysale
    count +=1

outfile.write("총매출 = {0}".format(str(sum)))
outfile.write("\n평균 일매출 = {0}".format(str(sum/count)))


infile.close()
outfile.close()