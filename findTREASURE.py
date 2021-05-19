import sys
import os

def function():
    print(" Hello welcome.!")
    print(
        "Assume you woke up in a misterious iland.\nThere is a map behind you, in the map \nthere is a way to find the treasure.\n\t now let's jump right into it")
    decsion = ""
    exit = input("are in or out.? (yes or no) : ")
    if exit == "no" or exit == "NO":
        sys.exit(0)
        os.system('cls')
    elif exit == "yes":
        os.system('cls')
        print(
            "okay so there is a stright way and another way from right, map shows that you can use both ways to reach treasure.")
        decsion = input("what do u wanna choose: (staright or right) : ")
        if decsion == "right":
            os.system('cls')
            print(
                "well.! it looks like we got to a river do u wanna swim or search for something that can float on water")
            decsion = input("what do u wanna choose: (swim or search) : ")
            if decsion == "swim":
                os.system('cls')
                print(
                    "cool lets go.. few seconds later...\n WTF is that a crocodile. \n\n do u wanna poke it with pen or swim back.")
                decsion = input("what do u wanna choose: (poke or swim) : ")
                if decsion == "poke":
                    print("well we are in water so cant use hand power to create good velocity.")
                    print("its really fast so cant poke on head\n")
                    print("\n\t\t LOL crocodile ate you while you are thinking.")
                    print("\n \t\t\t GAME OVER\nyou wanna restart or exit")
                    decsion = input("what do u wanna choose (restart or exit) : ")
                    if decsion == "restart":
                        os.system('cls')
                        function()
                    elif decsion == "exit":
                        exit()
                elif decsion == "swim":
                    os.system('cls')
                    print("This seems as a good idea lets go")
                    print("wait is that another shark")
                    print("\n \t\t\t GAME OVER\nyou wanna restart or exit")
                    decsion = input("what do u wanna choose (restart or exit) : ")
                    if decsion == "restart":
                        os.system('cls')
                        function()
                    elif decsion == "exit":
                        exit()
            elif decsion == "search":
                os.system('cls')
                print("well it's getting dark lets find something fast.")
                print("we gor banana tree leaves")
                print("wait what is that")
                print("OMG  a  rank 3 blood drinking demon ")
                print("demon slayer technique:\n\t 1 water breathing 10th form constant flux\n\t 2 Thunder breathing  1st form thunder clap and flash")
                decsion = input("what do u wanna choose (one or two) : ")
                if decsion == "one":
                    os.system('cls')
                    print("demon got you constant flux is slow")
                    print("\n \t\t\t GAME OVER\nyou wanna restart or exit")
                    decsion = input("what do u wanna choose (restart or exit) : ")
                    if decsion == "restart":
                        os.system('cls')
                        function()
                    elif decsion == "exit":
                        exit()
                elif decsion =="two":
                    print("it looks like using this thunder breathing 1st from we can go to treasure.")
                    print("wow we reached the treasure")
                    print("ab Hug do")
        elif decsion =="staright":
            os.system('cls')
            print("It looks like we reached a mountain and cave.\nShall we climb or just go inside cave.")
            dec = input("what do u wanna choose (mountin or cave) : ")
            if dec == "mountain":
                os.system('cls')
                print("well we are climbing since 15 min, gradully mountain is becoming hot")
                print("heck is this a valcano\n it just erupted.")
                print("\n \t\t\t GAME OVER\nyou wanna restart or exit")
                decsion = input("what do u wanna choose (restart or exit) : ")
                if decsion == "restart":
                    os.system('cls')
                    function()
                elif decsion == "exit":
                    exit()
            elif dec == "cave":
                os.system('cls')
                print("come on its too dark inside we dont have any torch.")
                print("wait something is glowing there.")
                print("lucky its gold.\n be quick lets get out of here.")
                print("\n\n\t finally you have finished the game.")
                decsion = input("what do u wanna choose (restart or exit) : ")
                if decsion == "restart":
                    os.system('cls')
                    function()
                elif decsion == "exit":
                    exit()

function()