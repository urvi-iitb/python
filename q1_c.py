import tables

with open ("in.txt","r") as f:
    a = int(f.readline())
    b = int(f.readline())
res = tables.table(a,b)
for i in res:
    print(i)