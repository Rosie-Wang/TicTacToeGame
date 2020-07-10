def genBoard():
    return [0,0,0,0,0,0,0,0,0]

def printBoard(T): #0 is empty board space, 1 is X-occupied, 2 is O-occupied
    if len(T)==9: #error checking (number of elements in the board must be 9)
        Tdisplay = T[:]
        for i in range(0,9):
            if T[i]==0:
                Tdisplay[i]=i #show position of board if the position is unoccupied
            elif T[i]==1:
                Tdisplay[i]="X" #show X if position is occupied by X
            elif T[i]==2:
                Tdisplay[i]="O" #print O if position is occupied by O
            else:
                return False #if the data in the board is not valid
        print(Tdisplay[0],'|',Tdisplay[1],'|',Tdisplay[2])
        print('--|---|--')
        print(Tdisplay[3],'|',Tdisplay[4],'|',Tdisplay[5])
        print('--|---|--')
        print(Tdisplay[6],'|',Tdisplay[7],'|',Tdisplay[8])
        return True
    else:
        return False #if length of board is not valid (doesn't equal 9)


def analyzeBoard (T): #returns: 0=board is in play, 1=X won, 2=O won, 3=draw
    if len(T) == 9: #error checking (number of elements in the board must be 9)
        # -------- 1st: CHECK FOR WINS ------------
        #Top ROW
        if T[0] == T[1] == T[2] == 1:
            state = 1 #X won
        elif T[0] == T[1] == T[2] == 2:
            state = 2 #O won
        #Middle ROW
        elif T[3] == T[4] == T[5] ==1:
            state = 1  # X won
        elif T[3] == T[4] == T[5] == 2:
            state = 2 #O won
        #Bottom ROW
        elif T[6] == T[7] == T[8] ==1:
            state = 1  # X won
        elif T[6] == T[7] == T[8] == 2:
            state = 2 #O won

        #Left COLUMN
        elif T[0] == T[3] == T[6] == 1:
            state = 1 #X won
        elif T[0] == T[3] == T[6] == 2:
            state = 2 #O won
        #Middle COLUMN
        elif T[1] == T[4] == T[7] == 1:
            state = 1 #X won
        elif T[1] == T[4] == T[7] == 2:
            state = 2  # O won
        #Right COLUMN
        elif T[2] == T[5] == T[8]==1:
            state = 1 #X won
        elif T[2] == T[5] == T[8]==2:
            state = 2 #O won

        #Top left-bottom right DIAGONAL
        elif T[0] == T[4] == T[8] == 1:
            state = 1 #X won
        elif T[0] == T[4] == T[8] == 2:
            state = 2 #O won
        #Top right-bottom left DIAGONAL
        elif T[2] == T[4] == T[6] == 1:
            state = 1 #X won
        elif T[2] == T[4] == T[6] == 2:
            state = 2 #O won

        # ----- NO WINS, CHECK IF DRAW OR STILL PLAYING ---------
        else: #if no one won
            # Check if board is in play
            for i in T:
                if T[i] == 0:
                    state = 0
                    break  # as long as one empty spot exists, the board is still in play
                else:
                    state = 3 #if board is completely occupied or it is analyzed that there's no way one player can win, it's a draw
        return state

    else:
        return -1



