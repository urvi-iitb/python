with open("inConvert.txt","r") as fi, open("outConvert.txt","w") as fo:
    for line in fi:
        sp = line.split(" ")
        l1 = str(1)+" "+sp[1]+" = "+str(float(sp[3])/float(sp[0]))+" "+sp[4].rstrip() +"\n"
        fo.write(l1)
        l2 = str(1)+" "+sp[4].rstrip()+" = "+str(float(sp[0])/float(sp[3]))+" "+sp[1] +"\n"
        fo.write(l2)