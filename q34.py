#num to binary 

def dec_to_bin(num):
    if num < 0:
        print("negative number!")
    elif num == 0:
        print("0")
    else:
        bin = ""
        while num > 0:
            bin= str(num % 2) + bin
            num //= 2
        print(bin)

num = int(input("enter number: "))
dec_to_bin(num)