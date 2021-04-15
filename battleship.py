from random import randint

board = []

# For loop that fills the board with "O"s
for x in range(0, 5):
  board.append(["O"] * 5)

#creates board
def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)

#creates random coordanents
def random_row(board):
  return randint(0, len(board) - 1)
def random_col(board):
  return randint(0, len(board[0]) - 1)
#assigns the random coordanents to the ship
ship_row = random_row(board)+ 1
ship_col = random_col(board)+ 1

#just to test our game (delete before final code) 
print (ship_row)
print (ship_col)

#loops through 4 turns
for turn in range(4):
  print ("Turn" , turn + 1)
  
  #asks user for their guesses
  guess_row = int(input("Guess Row: "))-1
  guess_col = int(input("Guess Col: "))-1
  
  # impliments you win and game over
  if guess_row == (ship_row) - 1 and guess_col == (ship_col) - 1:
    print ("Congratulations! You sank my battleship!")
    break
  else:
    if guess_row not in range(5) or guess_col not in range(5):
      print ("Oops, thats not even in the ocean.")
    elif(board[guess_row][guess_col]=="X"):
      print("You guessed that one already.")
    else:
      print ("You missed my battleship!")
      board[guess_row][guess_col] = "X"
      
    if(turn==3):
      print("game over")
      
    print_board(board)



