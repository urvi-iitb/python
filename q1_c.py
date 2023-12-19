with open ("in.txt","r") as f:
    a = int(f.readline())
    b = int(f.readline())
for i in range (a, b+1):
    for j in range (1,11):
        print(i, "*", j,"=",i*j, end="\n")
    print("\n")