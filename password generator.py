import random
import module


print("Welcome to the python automatic password generator.!\n")
lets = input("How many letters would u want in password : ")
nums = input("How many numbers would u want in password : ")
sps = input("How many special characters would u want in password : ")
size =int(lets)
ran =""
pystr =""
pynum =""
pychar=""
password=[]

for n in range(0,size):
    ran=random.randint(0,51)
    pystr=pystr+module.letters[ran]
    password.append(pystr[n])
#print(pystr)


nsize=int(nums)
for n in range(0,nsize):
    ran=random.randint(0,9)
    pynum=pynum+module.numbers[ran]
    password.append(pynum[n])
#print(pynum)



csize = int(sps)
for n in range(0,csize):
    ran=random.randint(0,13)
    pychar=pychar+module.sp[ran]
    password.append(pychar[n])
#print(pychar)


random.shuffle(password)
final_password=""
for char in password:
    final_password +=char
print(f"Generated password is : {final_password}")

#print(f"Generated password is :{pystr+pynum+pychar}")






