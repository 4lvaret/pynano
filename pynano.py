# pynano - written by 4lvaret
import os
import time
import sys

opened = 0
listest = []
commands = [":quit", ":save", ":change"]

def edit():
    global listest, opened
    os.system('cls' if os.name == 'nt' else 'clear')
    print("pynano\nwrite :save to save, write :change to change a line and write :quit to exit without saving\n")
    if opened == 1:
        for i in listest:
            print(f"> {i}")
    while True:
        temp = input("> ")

        if temp in commands:
            if temp == ":quit":
                print("exiting without saving, have a great day :3")
                sys.exit()
            if temp == ":save":
                test = input("what do you want to save it as? ") 
                with open(test, "w") as f:
                    for i in listest:
                        f.write(i + "\n")
                print("Done! Exiting now.")
                sys.exit()
            if temp == ":change":
                x = 0
                for i in listest:
                    x += 1
                    print(f"{x}: {i}")

                test = input("what line do you want to edit? ")
                print("change line to your content")
                temp = input("> ")
                listest[int(test) - 1] = temp
                print("\ndone! going back to regular editing")
        else:    
            listest.append(temp)

def menu():
    print("select alternative:\n1: open file and edit\n2: make new file and edit")
    choice = input("> ")

    if choice == "1":
        openfile()
    elif choice == "2":
        edit()
    else:
        print("not a valid option! exiting")

def openfile():
    global listest, opened
    filename = input("enter file to open: ")
    with open(filename, "r") as f:
        listest = [line.rstrip("\n") for line in f]
    opened = 1
    edit()


print("pynano - by 4lvaret")
time.sleep(2)
menu()