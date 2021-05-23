import random
print("Welcome to  hangman game.!")
print("There is a hidden word you need to guess the word letter by letter.")
print("if u guess wrong and ran out of six lives then a innocent person will be hanged to death.")
word=["apple","orange","reyna","pheonix","banana","coconut","mango","flabbergasted","hello","impressive","ascent","heaven"]
cword=word[random.randint(0,len(word)-1)]
blanks=[]
dummy =[]
lives = 6

for n in range(0, len(cword)):
    dummy.append(cword[n])
    blanks.append("_")
print(cword)


while dummy != blanks:
    user = input("\npick a letter : ").lower()
    for n in range(0, len(cword)):
        if (user == cword[n]):
            blanks[n] = user
    if user not in cword:
        lives = lives-1
        if(lives == 0):
            break
    print(f"Lives remining :{lives}\n")
    print(*blanks)

if(dummy == blanks):
    print("\nYou won\n You saved a man's life")
if(dummy != blanks):
    print("\nYou lose \n A man is dead that on you")




