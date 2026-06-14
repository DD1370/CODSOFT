def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    if b==0:
        return "Zero Division Error"
    else:
        return a/b
print("~-~- CALCULATOR -~-~")
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
ch=input("Enter choice(+,-,*,/): ")
if ch=="+":
    print("Answer=",addition(num1,num2))
elif ch=="-":
    print("Answer=",subtraction(num1,num2))
elif ch=="*":
    print("Answer=",multiplication(num1,num2))
elif ch=="/":
    print("Answer=",division(num1,num2))
else:
    print("Invalid Choice")
