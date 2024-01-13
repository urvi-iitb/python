#leap years between 2000 and 2400 
leap_year= []

for year in range (2000,2401):
    if (year%4 ==0) and (year%100!=0):
        leap_year.append(year)
    elif (year%400==0):
        leap_year.append(year)

print(leap_year)