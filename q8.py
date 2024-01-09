import re #for pattern matching using regex

difficult_words = []
with open ("q8_passage.txt", "r") as f:
    data = f.read()
    
pat = r'\*(.*?)\*'
difficult_words = re.findall(pat, data)
print(difficult_words)
