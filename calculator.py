num1=float(input("Enter first number : "))
op=input("choose an operation '+','-','*','/' : ")
num2=float(input("Enter first number : "))
answer=0

def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

operations={"+":add(num1,num2),
            "-":sub(num1,num2),
            "*":mul(num1,num2),
            "/":div(num1,num2)
            }

for n in operations:
    if n==op:
        answer=operations[n]

print(f"{num1} {op} {num2} = {answer}")




