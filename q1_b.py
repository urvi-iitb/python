Start = int(input("start:"))
End = int(input("end:"))
for i in range (Start, End+1):
    for j in range (1,11):
        print(i, "*", j,"=",i*j, end="\n")
    print("\n")