infile = open("practice.txt")
outfile = open("practice1.txt", "w")

i = 1

for line in infile:
    outfile.write(str(i)+ ":" + line)
    i += 1

infile.close()
outfile.close()