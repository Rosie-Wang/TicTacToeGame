from tttlib import *

T = genBoard()
print("------------------------------------------------------------------------------------------------------------------------------")
print("Welcome to the world of Tic-Tac-Toe!")
print("------------------------------------------------------------------------------------------------------------------------------")
print("Before we start, let's establish some basic knowledge:")
print("   A board will be displayed on your screen.")
print("   This board is labeled with numbers corresponding to the position shown.")
print("   If a position if occupied, it will display the player occupying that position (X or O)")
print(" ")
print("To make the game more challenging, here is something to watch out for:")
print("   PAY ATTENTION TO THE DISPLAYED BOARD!")
print("   If you choose a position that is unoccupied or invalid, you lose this turn and your opponent will immediately take your turn!")
print("   This is a test of your attention, so make sure you stay alert and don't let your opponent distract you.")
print("--------------------------------------------------------------------------------------------------------------------------------")
print("Are you ready?....GO!")

while True:
   printBoard(T)
   moveX = int(input("X player, choose your move:"))
   if ((moveX==0) or (moveX==1) or (moveX==2) or (moveX==3) or (moveX==4) or (moveX==5) or (moveX==6) or (moveX==7) or (moveX==8)):
   # check moveX for valid input
   #check if the position is unoccupied
      if T[moveX]==0:
         T[moveX] = 1 # yes, valid and unoccupied, set that position to be 1 (represents X)
         state = analyzeBoard(T)
         if state == 0:
            print("...board is in play...")
         elif state == 1:
            print("CONGRATULATIONS X PLAYER! YOU WON!")
            break
         elif state == 3:
            printBoard(T)
            print("IT'S A DRAW!")
            break
         else:
            print("Error in analyzing")
      else:
         print("Sorry! That position is occupied. You lose your turn :(")

   else:
      print("Oh no! Looks like your move was invalid.")

   printBoard(T)
   moveO = int(input("O player, choose your move:"))
   if ((moveO==0) or (moveO==1) or (moveO==2) or (moveO==3) or (moveO==4) or (moveO==5) or (moveO==6) or (moveO==7) or (moveO==8)):
      # check moveO for valid input
      # check if the position is unoccupied
      if T[moveO]==0:
         T[moveO] = 2 # yes, valid and unoccupied, then set that position to be 2 (represents O)

         state = analyzeBoard(T)
         if state == 0:
            print("...board is in play...")
         elif state == 2:
            print("CONGRATULATIONS O PLAYER! YOU WON!")
            break
         elif state == 3:
            printBoard(T)
            print("IT'S A DRAW!")
            break
         else:
            print("Error in analyzing")
      else:
         print("Sorry! That position is occupied. You lose your turn :(")
   else:
      print("Oh no! Looks like your move was invalid.")
