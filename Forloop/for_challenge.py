sh = input("input a list of student heights : ").split()
count =0
sum=0
for n in range (0,len(sh)):
    sh[n] = int(sh[n])
    count =count+1
    sum = sum+sh[n]

avg = round(sum/count)
print(f"\nThe average height of all {count} students is :{avg}")
