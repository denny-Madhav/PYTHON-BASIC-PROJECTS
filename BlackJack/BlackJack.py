import random
from os import system

ucard=[]
ccard=[]



def compare(us, cs):
    if us == cs:
        return "Game is draw"
    elif cs == 0:
        return "You lose, Opponent has blackjack"
    elif us == 0:
        return "Win with a black jack"
    elif us > 21:
        return "You went over the limit"
    elif cs > 21:
        return "Opponent went over the limit you won"
    elif us > cs:
        return "You win"
    else:
        return "Computer win"

def score(cards):
    """ Checks the sum of the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

us=score(ucard)
cs=score(ccard)

def deal_cards():
    """"Takes a card out of these cards and assign to the assigned variable"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
for loop in range(2):
    ucard.append(deal_cards())
    ccard.append(deal_cards())

def play():
    gameover = False
    while not gameover:
        us = score(ucard)
        cs = score(ccard)
        print(f"your cards {ucard} and score {us}\nCoumpeter first card[{ccard[0]}]")
        if us == 0 or cs == 0 or us > 21:
            gameover = True
        else:
            ip = input("Type 'y' to get another card and 'n' to pass : ")
            if ip == "y":
                ucard.append(deal_cards())
            else:
                gameover = True

    while cs != 0 and cs < 17:
        ccard.append(deal_cards())
        cs = score(ccard)
    print(f"\nyour cards {ucard} and score {us}\nCoumpter cards {ccard} and score {cs}")
    print(compare(us, cs))


while input("\nDo you wanna play a black jack type 'y' or 'n' : ")=="y":
    play()
    system('cls')