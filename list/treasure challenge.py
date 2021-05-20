one =["🐕","🐕","🐕"]
two =["🦮","🦮","🦮"]
the =["🐈","🐈","🐈"]

all = [one,two,the]

print(f"{one}\n{two}\n{the}\n")

postion=input("This is the map where do u wanna place the treasure : ")

h=int(postion[0])
v=int(postion[1])
all[h-1][v-1] ="🦝"
print(*all, sep ="\n")