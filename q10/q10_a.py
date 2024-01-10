import re

file = "a.txt"
sorted_file = "sorted_passage.txt"
def func(file,sorted_file):
    with open (file,"r") as f:
        data = f.read()
        pattern = r'[^a-zA-Z\s]'
        words = (re.sub(pattern, '',data)).split()
        for i in range (len(words)):
            words[i] = words[i].lower()
            set_of_words = set(words)
            sorted_words = sorted(set_of_words)
        with open (sorted_file,"w") as f:
            for i in sorted_words:
                f.write(i)
                f.write("\n")