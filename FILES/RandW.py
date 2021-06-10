"""file = open("file.txt")
contents = file.read()
print(contents)
file.close()"""

with open("file.txt", mode = "w") as hello:
    #hmm = hello.read()
    keka = hello.write("babi")
    hello.write("hello babai")
    print(keka)

with open("esko.txt", mode="w") as sare:
    sare.write("sarsarle")

