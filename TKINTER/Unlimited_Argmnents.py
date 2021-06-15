"""a=5
b=6
c=7
d=8
e=9
f=0

def fun(*args):#(*args) Unlimited arguments.
    f=a+b
    print(f)
    print(f-c)
    print(d*e)
fun(a,b,c,d,e,f)"""

"""def add(*args):
    sum = 0
    for i in args:
        print(i)
        sum += i
    return sum

print(add(3,5,7,9,11,13,15,17,19))"""
"""a=5
b=10
c=15
d=20
e=25
f=0
def calculate(n, **kwargs): #(**kwargs) is unlimited keyword arguments
    #f=a+b-c*d%e
    #print(f)
    #for (key, value) in kwargs.items():
       # print(key,value)
    n += kwargs["add"]
    n *= kwargs["mul"]

    print(n)


calculate(5,add=5,mul=10)
"""
class car:

    def __init__(self,**DK):
        self.make = DK.get("make")
        self.model =DK.get("model")
        self.color = DK.get("Color")

hmm = car(make="NISSAN")
print(hmm.model)

