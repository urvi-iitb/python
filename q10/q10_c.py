import os
import datetime

files = os.listdir()
all_words = []
for file in files:
    if file.startswith("sorted_") and file.endswith(".txt"):
        with open (file,"r") as f:
            content = f.read()
            words = content.split("\n")
            all_words.extend(words)
unique_words = set(all_words)
sorted = sorted(unique_words)

date = datetime.datetime.now().strftime("%Y%m%d")
with open ("sorted_"+date+".txt","w") as f:
    for i in sorted:
        f.write(i)
        f.write("\n")
