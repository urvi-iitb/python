#simple calculator

class calculator:
    def __init__(self):
        print("calculating output")
        self.res = 0
    def add(self,x,y):
        self.res = x + y
        return self.res

    def sub(self,x,y):
        self.res = x- y
        return self.res

    def mul(self,x,y):
        self.res = x*y 
        return self.res

    def div(self,x,y):
        if y == 0 :
            print("divison by zero!") 
            return 
        self.res = x/y
        return self.res


my_calc= calculator()
a,b = eval(input("enter 2 numbers (a,b) :"))
op = input("enter operation (add/sub/mul/div): ")  
if op.lower() == "add":
    print(my_calc.add(a,b))

elif op.lower() == "sub":
    print(my_calc.sub(a,b))

elif op.lower() == "mul":
    print(my_calc.mul(a,b))

elif op.lower() =="div":
    print(my_calc.div(a,b))

else :
    print("invalid input")