a = int(input("start"))
b = int(input("end"))

for i in range (a,b+1):
    filename = str(i) + ".txt"
    with open (filename,"w") as f:
        for j in range (1,11):
            string = str(i)+"*"+str(j)+"="+str(i*j)+"\n"
            f.write(string)