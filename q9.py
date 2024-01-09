import re

string = input("enter string")
pattern = r'[^a-zA-Z0-9\s]'

updated = re.sub(pattern, '',string)
print(updated)