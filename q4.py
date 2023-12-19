#prisoners with cell number which has odd number of divisors will be lucky
#ONLY PERFECT SQUARES HAVE ODD NUMBER OF DIVISORS

import math
import datetime

n = 100 #no. of cells
lucky =[]
i=1
while i*i <= n:
    lucky.append(str(i*i))
    i+=1
with open ("Letter1","w") as f:
    f.write(str(datetime.date.today()))
    f.write("\n")
    for line in lucky:
        f.write(f'{line}\n')
with open ("Letter2", "w") as f:
    for i in range (1,100):
        if str(i) not in lucky:
            f.write(f'{str(i)}\n')