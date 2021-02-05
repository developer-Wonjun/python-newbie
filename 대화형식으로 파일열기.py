from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

readFile = askopenfilename()
if(readFile != None):
    infile = open(readFile,"r")

for line in infile.readlines():
    line = line.strip()
    print(line)

infile.close()