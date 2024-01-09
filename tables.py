#calculating tables from a to b

def table (a,b):
    res = []
    for i in range (a,b+1):
        str1= ""
        for j in range (1,11):
            string = str(i)+"*"+str(j)+"="+str(i*j) +"\n"
            str1 = str1+string
        res.append(str1)
    return res