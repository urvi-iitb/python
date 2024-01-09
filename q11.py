
import re


with open ("template.txt","r") as f:
    template = f.read()
with open ("list1.txt","r") as f:
    data = f.readlines()

pat = r'\$\d+\w+ '
text = re.split(pat,template)
text[-1]=text[-1].rstrip()
text_temp=''
for i in range (len(text)-1):
    text_temp = text_temp.rstrip(" ")+text[i].lstrip(" ")+"{}"
#print(text_temp)

with open ("message.txt", "w")as f:    
    for line in data:
        person = line.split(",")
        msg = text_temp.format(*person)
        if person[0]=="F":
            msg = re.sub("F","Ms.",msg)
        else:
            msg = re.sub("M","Mr.",msg)
        f.write(msg)