#finding palindromes 
def palindrome(filename):
    with open (filename,"r") as f:
        data = f.read()
        words = data.split(" ")
        palindromes = []
        for word in words:
            flag = True
            for i in range (len(word)//2):
                if word[i]!=word[len(word)-1-i]:
                    flag = False
                    break
            if flag == True:
                palindromes.append(word)
        palindromes= set(palindromes)
        for i in palindromes:
            print(i)

palindrome("palindrome.txt")