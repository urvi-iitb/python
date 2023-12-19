with open ("in.txt","r") as f:
    a = (f.readline()).split(",")
start = int(a[0])
end = int(a[1])
with open ("out.txt","w") as f:
    for i in range (start, end+1):
        for j in range (1,11):
            string = str(i) + "*" + str(j) + "=" + str(i*j) + "\n"
            f.write(string)
        f.write("\n")