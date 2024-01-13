# done it separately for this part as part a is iteratively doing the conversion so it will do for 
#any number of inputs while here we are taking one input from the user

a = input("first")
b = input("second")
c = a.split(" ")
d = b.split(" ")

l1 = str(1)+" "+c[1]+" = "+str(round((float(d[0])/float(c[0])),2))+" "+d[1]+"\n"
l2 = str(1)+" "+d[1]+" = "+str(round(float(c[0])/float(d[0]),2))+" "+c[1] +"\n"
print(l1)
print(l2)