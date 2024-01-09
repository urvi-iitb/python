#prisoners with cell number which has odd number of divisors will be lucky
#ONLY PERFECT SQUARES HAVE ODD NUMBER OF DIVISORS

import math
import datetime

n = 100 #no. of cells
lucky =[]
cells =[]
for i in range (0,100):
    cells.append("C")
#print(cells)
for j in range (1,100):  #j+1 is cell number
    for i in range (j,100,j):
        if cells[i]=="C":
            cells[i]="O"
        elif cells[i]=="O":
            cells[i]="C"
for i in range (100):
    if cells[i]=="O":
        lucky.append(i)
with open ("Letter1","w") as f:
    f.write(str(datetime.date.today()))
    f.write("\n")
    for line in lucky:
        f.write(f'{line}\n')
with open ("Letter2", "w") as f:
    for i in range (1,100):
        if i not in lucky:
            f.write(f'{str(i)}\n')