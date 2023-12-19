import datetime as dt
import os

a = int(input("start:"))
b = int(input("end:"))

now = dt.datetime.now()
formatted_time = now.strftime("%Y%m%d_%H%M%S")
filepath = f"../TABLES/{str(a)}_{formatted_time}.txt"
dir_path = "../TABLES"
os.makedirs(dir_path, exist_ok=True)
with open (filepath,"w") as f:
    for i in range (a,b+1):
        for j in range (1,11):
            string = str(i)+"*"+str(j)+"="+ str(i*j)+"\n"
            f.write(string)
        f.write("\n")