board = ["  " for space in range (1,10)] #prints out the spaces for the tic tac toe board 
print (board)

def print_board ():
    #creating the 3 x 3 grid format of tictactoe    
    row1 ="|{}| |{}| |{}|".format (board[0], board[1], board[2])
    row2 ="|{}| |{}| |{}|".format (board[3], board[4], board[5])
    row3 ="|{}| |{}| |{}|".format (board[6], board[7], board[8])
   #printing the rows 
    print () 
    print (row1)
    print (row2) 
    print (row3) 
    print () 

#funct for icon of the players as well as their moves
def player_move(icon):
    if icon == "X":
        number = 1 
    elif icon == "O":
        number = 2 
    print ("Your turn player {} ".format(number))
    
    #user intput for board
    choice = int(input("Enter a number between (1 - 9) to make your move: ").strip())
   #if there is room on the position the user selected 
    if board[choice-1] == "  ":
        board[choice -1]= icon
    else:
        print()
        print ("That space is taken try again")

        #8 different possible outcomes of winning the game 
def win_game(icon):
    if (board[0] == icon and board[1]== icon and board[2]== icon) or\
       (board[3] == icon and board[4]== icon and board[5]== icon) or\
       (board[6] == icon and board[7]== icon and board[8]== icon) or\
       (board[1] == icon and board[4]== icon and board[7]== icon) or\
       (board[0] == icon and board[3]== icon and board[6]== icon) or\
       (board[2] == icon and board[5]== icon and board[8]== icon) or\
       (board[0] == icon and board[4]== icon and board[8]== icon) or\
       (board[2] == icon and board[4]== icon and board[6]== icon):
       return True
    else:
        return False
    #function for the outcome of a draw 
def is_draw():
#if there is no space on the board then return true for game being a draw
    if " " not in board:
        return True
    else:
        return False
 
while True:
#prints the board and moves of both users
    print_board()
    player_move("X")
    print_board()
#checks if player 1 wins the game 
    if win_game("X"):
        print ("X wins!")
        break
#checking for draw 
    elif is_draw():
        print ("It's a draw!")
    player_move("O")
#checks if player 2 wins the game 
    if win_game("O"):
        print_board
        print ("O wins!")
        break
#checking for draw  
    elif is_draw():
        print ("It's a draw!")
        




    
    
