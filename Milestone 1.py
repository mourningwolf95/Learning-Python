#Imports here

import random

#Globals

slot = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
Players = {"1":" ",
           "2":" "}

#Methods and functions

def Board(board):
    print(" ")
    print(" " + slot[7] + " | " + slot[8] + " | " + slot[9])
    print("--- --- ---")
    print(" " + slot[4] + " | " + slot[5] + " | " + slot[6])
    print("--- --- ---")
    print(" " + slot[1] + " | " + slot[2] + " | " + slot[3])
    ImGreat = " "
    return ImGreat

def PlayerXO():
    Loop = True
    while Loop == True:
        You = input("Let's play Tic-Tac-Toe! Do you want to be X or O? ").upper()
        if You == "X" or You == "O":
            print("Okay. You will be " + You + ".")
            Players["1"] = You
            Loop = False
            return You
        else:
            print("""
Let's try that again, shall we?""")
            return Loop

def Player2():
    if Players["1"] == "X":
        Players["2"] = "O"
    else:
        Players["2"] = "X"

#def PlaceMarker(board, marker, position):
 #   global slot
  #  slot.insert(position, marker)
   # print(Board(slot))
    
def WinCheck(board, M):
    if((board[7] == M and board[8] == M and board[9]) == M or
    (board[4] == M and board[5] == M and board[6] == M) or
    (board[1] == M and board[2] == M and board[3] == M) or
    (board[7] == M and board[4] == M and board[1] == M) or
    (board[8] == M and board[5] == M and board[2] == M) or
    (board[9] == M and board[6] == M and board[3] == M) or
    (board[7] == M and board[5] == M and board[3] == M) or
    (board[1] == M and board[5] == M and board[9] == M)):
        return True
    else:
        return False

def RandFirst():
    X = str(random.randint(1,2))
    print("Player " + X + " will go first!")
    return X

def SpotCheck(Slot, Pos):
    if slot[Pos] != " ":
        print("That spot's taken! You can't move there!")
        return False
    else:
        return True

def IsFull(Slot):
    if " " in slot:
        return False
    else:
        return True

def MoveHere(Slot, XO):
    global slot
    Loc = int(input("Please enter a number that corresponds with there you would like to move. "))
    Free = SpotCheck(slot, Loc)
    if Free == False:
        Loc = int(input("Please enter a number that corresponds with where you would like to move. "))
    else:
        slot[Loc] = XO
    return Free

def Replay():
    Again = input("Do you want to play again? ").lower()
    if Again == "yes":
        print("Hooray!")
        return True
    elif Again == "no":
        print("That's too bad.")
        return False
    else:
        print("I'm sorry, I didn't quite catch that.")
        return "I'm a dumb piece of shit program that won't fucking work for some stupid reason."



def Main():
    PlayerXO()
    Player2()
    X = RandFirst()
    if X == "1":
        Y = "2"
    else:
        Y = "1"
    GameOver = "No"
    while GameOver == "No":
        while GameOver == "No":
            GameOver = Move(X)
            break
        print(" ")
        while GameOver == "No":
            GameOver = Move(Y)
            break

    
def Move(Pl):
    print("It's you're turn, Player" + Pl + ".")
    MoveHere(slot, Players[Pl])
    print(Board(slot))
    Win = WinCheck(slot, Players[Pl])
    F = IsFull(slot)
    if Win == True:
        print("Congratulations! Player" + Pl + " wins!")
        return "Yes"
    else:
        if F == True:
            print("Alas, there are no more moves available.")
            return "Yes"
        else:
            return "No"
    
        
    
    
#Main method

Main()