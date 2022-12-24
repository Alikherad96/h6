import pyfiglet
import random
import colorama
import time

title = pyfiglet.figlet_format("Tic Tac Toe",font="5lineoblique")
print(title)

start = time.time()
w=c=0
def show():
    for i in tic:
        for j in i:
            if j=="o":
                from colorama import Fore
                print(Fore.BLUE,j, end=" ")
            elif j=="x":
                from colorama import Fore
                print(Fore.RED,j, end=" ")
            else:
                from colorama import Fore
                print(Fore.BLACK,j, end=" ")
        print()

def player(a):
    while True:
        print("player", a , ":plz entr ur row and col position = ")
        i=int(input())
        j=int(input())
        if (-1< i <3) and (-1< j <3):
            if (tic[i][j] == "-"):
                if a == 1 :
                    tic[i][j] = "x"
                elif a == 2 :
                    tic[i][j] = "o"
                break
        else:
            print("plz plz choose btween 0,1,2")

def cpu(a):
    while True:
        if a == 1:
            print("player1 :plz entr ur row and col position = ")
            i=int(input())
            j=int(input())
            if (-1< i <3) and (-1< j <3) and (tic[i][j] == "-"):
                tic[i][j] = "x"
                break
            else:
                print("plz enter correct")
        elif a == 2 :
            ii=random.randint(0,2)
            jj=random.randint(0,2)
            if tic[ii][jj] == "-":
                tic[ii][jj] = "o"
                break

def win():
    global w
    for i in range(3):
        if tic[i][i] != "-":
            if (tic[i][0] == tic[i][1] == tic[i][2]) or (tic[0][i] == tic[1][i] == tic[2][i]):
                w=1
        if tic[1][1] != "-":
            if (tic[0][0] == tic[1][1] == tic[2][2]) or (tic[0][2] == tic[1][1] == tic[2][0]):
                w=1

def begin():
    global tic
    tic = [["-" ,"-" ,"-"],
           ["-" ,"-" ,"-"],
           ["-" ,"-" ,"-"]]

a=w=c=0
begin()
print("choose 2player(enter(2)) or player1 and cpu(entr 1)")
b=int(input())
while True:
    a +=1
    if a > 2:
        a=1
    if b==2:
        player(a)
    elif b==1:
        cpu(a)
    show()
    win()
    if w == 1 :
        print("player", a ," win")
        print("runtime in seconds = " ,time.time()-start)
        break
        
    q=0
    for i in tic:
        q=q+i.count("-")
    print("jahaye khali = " ,q)
    if q == 0:
        print("plz try again no bode win")
        begin()