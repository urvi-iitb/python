import datetime as dt
import os
import tables

a = int(input("start:"))
b = int(input("end:"))

now = dt.datetime.now()
formatted_time = now.strftime("%Y%m%d_%H%M%S")
filepath = f"../TABLES/{str(a)}_{formatted_time}.txt"
dir_path = "../TABLES"
os.makedirs(dir_path, exist_ok=True)
with open (filepath,"w") as f:
    res = tables.table(a,b)
    for i in res:
        f.write(i)
        f.write("\n")