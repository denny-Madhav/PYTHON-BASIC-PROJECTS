sh = input("input a list of student marks: ").split()
count =0
high=0
for n in range(0,len(sh)):
    sh[n] = int(sh[n])
    count =count+1

for score in sh:
    if score > high:
        high=score
print(f"Highest marks among all {count} students is : {high}")



