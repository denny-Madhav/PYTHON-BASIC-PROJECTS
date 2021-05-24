
alphabets="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
bits=alphabets.split(",")
sc= True
def cypher(text , key , type):
    cypher =""
    if type == "decode":
        key *= -1
    for char in text:
        if char in bits:
            pos = bits.index(char)
            npos = pos + key
            cypher = cypher + bits[npos]
        else:
            cypher += char
    print(f"Here is the {type}d  information: {cypher}")
while sc:
    konsa = input("Here we go do you wanna encode or decode : ").lower()
    message = input("Type a message to process : ").lower()
    keydigit = int(input("Enter Key digit : "))

    keydigit = keydigit % 26

    cypher(text=message, key=keydigit, type=konsa)

    result = input("Type 'yes' if u want to go again. or else type 'no'\n")
    if result == "no":
        sc = False
        print("Bye.!")


