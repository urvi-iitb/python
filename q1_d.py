import tables

with open ("in.txt","r") as f:
    a = (f.readline()).split(",")
start = int(a[0])
end = int(a[1])
with open ("out.txt","w") as f:
    res = tables.table(start,end)
    for string in res:
        f.write(string)
        f.write("\n")