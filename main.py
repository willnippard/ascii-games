import math
import random

# Initialize the game board
board = [
  [' ', ' ', ' '],
  [' ', ' ', ' '],
  [' ', ' ', ' ']
]

# Initialize player turn
player = 'X'

# Function to print the game board
def print_board():
  print(board[0][0] + '|' + board[0][1] + '|' + board[0][2])
  print('-+-+-')
  print(board[1][0] + '|' + board[1][1] + '|' + board[1][2])
  print('-+-+-')
  print(board[2][0] + '|' + board[2][1] + '|' + board[2][2])
  print()

# Function to check if a player has won
def check_win(player, board):
  # Check rows
  for i in range(3):
    if board[i][0] == player and board[i][1] == player and board[i][2] == player:
      return True
  
  # Check columns
  for j in range(3):
    if board[0][j] == player and board[1][j] == player and board[2][j] == player:
      return True
  
  # Check diagonals
  if board[0][0] == player and board[1][1] == player and board[2][2] == player:
    return True
  
  if board[0][2] == player and board[1][1] == player and board[2][0] == player:
    return True
  
  return False

# Function to check if the game is a tie
def check_tie():
  for i in range(3):
    for j in range(3):
      if board[i][j] == ' ':
        return False
  
  return True

def playerTurn():
  # Get player input
  row = int(input("Enter row (0, 1, or 2) for " + player + ": "))
  col = int(input("Enter column (0, 1, or 2) for " + player + ": "))
  print()
  
  # Update the game board
  board[row][col] = player

def aiTurn():
  print("AI turn...")
  if all(elem == '' for elem in board):
    random_row = random.randint(0, 2)
    random_col = random.randint(0, 2)
    board[random_row][random_col] = player
  else:
    best_move = find_best_move(player, board)
    board[best_move[0]][best_move[1]] = player

def find_best_move(current_player, current_board):
    best_score = -math.inf
    best_move = None
    
    for i in range(3):
        for j in range(3):
            # Check if the spot is available
            if current_board[i][j] == ' ':
                current_board[i][j] = current_player
                score = minimax(current_player, current_board, 0, False)
                current_board[i][j] = ' '

                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move

def minimax(current_player, current_board, depth, is_maximizing):
    opposing_player = 'O' if current_player == 'X' else 'X'

    # Check if the game is over
    if check_win(opposing_player, current_board):
        return -1
    elif check_win(current_player, current_board):
        return 1
    elif check_tie():
        return 0

    # If it's the maximizing player's turn
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                # Check if the spot is available
                if current_board[i][j] == ' ':
                    current_board[i][j] = current_player
                    score = minimax(current_player, current_board, depth+1, False)
                    current_board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score

    # If it's the minimizing player's turn
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                # Check if the spot is available
                if current_board[i][j] == ' ':
                    current_board[i][j] = opposing_player
                    score = minimax(current_player, current_board, depth+1, True)
                    current_board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def checkWin():
  # Check for win or tie
  if check_win(player, board):
    print(player + " wins!")
    return True
  elif check_tie():
    print("Tie game!")
    return True

  return False


# Main game loop
while True:
  # Print the game board
  print_board()

  # Player turn
  playerTurn()
  
  # Print the game board
  print_board()

  # Check for win or tie
  if checkWin():
    break
  
  player = 'O' if player == 'X' else 'X'

  # AI turn
  aiTurn()

  # Check for win or tie
  if checkWin():
    break

  player = 'O' if player == 'X' else 'X'