#function to find if number is a prime number 
def prime(num):
    flag = 0 
    for i in range (2,num//2 +1):
        if num%i ==0:
            flag =1
            break
    if (flag == 0):
        print("prime")
    else:
        print("not a prime")
a = int(input("enter number:"))
prime(a)