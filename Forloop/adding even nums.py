print("Adding even number sfrom 1  to 100")

n = 0
o=0
for num in range(1,101):
    if num%2==0:
        n=n+num
    else:
      o=o+num
print(f"sum of even : {n}")

print(f"sum of odd :{o}")
print("total is")
print(n+o)