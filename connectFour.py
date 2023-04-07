import numpy as np

# Define constants for the number of rows and columns
ROWS = 6
COLS = 7

# Initialize the game board with empty cells
board = np.full((ROWS, COLS), " ")

# Define the function to print the game board
def print_board():
    print("\n " + "|".join([" " + str(i+1) + " " for i in range(COLS)]) + "\n" + "-"*29)
    for row in board:
        print("|" + "|".join([" " + cell + " " for cell in row]) + "|")
        print("-"*29)

# Define the function to check if a column is full
def is_column_full(col):
    return board[0][col] != " "

# Define the function to drop a piece into a column
def drop_piece(col, piece):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == " ":
            board[row][col] = piece
            return

# Define the function to check if the game is over
def is_game_over():
    # Check for horizontal wins
    for row in range(ROWS):
        for col in range(COLS - 3):
            if board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3] != " ":
                print(f"Player {board[row][col]} wins!")
                return True

    # Check for vertical wins
    for row in range(ROWS - 3):
        for col in range(COLS):
            if board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col] != " ":
                print(f"Player {board[row][col]} wins!")
                return True

    # Check for diagonal wins (top-left to bottom-right)
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] != " ":
                print(f"Player {board[row][col]} wins!")
                return True

    # Check for diagonal wins (bottom-left to top-right)
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if board[row][col] == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3] != " ":
                print(f"Player {board[row][col]} wins!")
                return True

    # Check if the board is full
    if " " not in board:
        print_board()
        print("It's a tie!")
        return True

    return False

import math

# Constants
EMPTY = ' '
PLAYER1 = 'X'
PLAYER2 = 'O'

def smartest_ai_move():
    move, _ = minimax(board, depth=6, alpha=-math.inf, beta=math.inf, maximizingPlayer=True)
    return move

def smart_ai_move():
    move, _ = minimax(board, depth=4, alpha=-math.inf, beta=math.inf, maximizingPlayer=True)
    print('best move', move)
    return move

def minimax(board, depth, alpha, beta, maximizingPlayer):
    # Base case: depth = 0 or game is over
    if depth == 0 or is_game_over():
        return None, evaluate_board(board)

    valid_moves = get_valid_moves(board)
    best_move = None

    if maximizingPlayer:
        best_score = -math.inf
        for move in valid_moves:
            temp_board = make_move(board, move, PLAYER2)
            _, score = minimax(temp_board, depth-1, alpha, beta, False)
            if score > best_score:
                best_score = score
                best_move = move
            alpha = max(alpha, best_score)
            if alpha >= beta:
                break
        return best_move, best_score

    else:
        best_score = math.inf
        for move in valid_moves:
            temp_board = make_move(board, move, PLAYER1)
            _, score = minimax(temp_board, depth-1, alpha, beta, True)
            if score < best_score:
                best_score = score
                best_move = move
            beta = min(beta, best_score)
            if alpha >= beta:
                break
        return best_move, best_score

def evaluate_board(board):
    # Evaluate the board for the current player
    # Return a score between -100 and 100
    # The higher the score, the better the position for the current player
    score = 0

    # Check horizontal
    for i in range(len(board)):
        for j in range(len(board[0]) - 3):
            window = board[i][j:j+4]
            score += evaluate_window(window)

    # Check vertical
    for i in range(len(board) - 3):
        for j in range(len(board[0])):
            window = [board[i+k][j] for k in range(4)]
            score += evaluate_window(window)

    # Check diagonal (top-left to bottom-right)
    for i in range(len(board) - 3):
        for j in range(len(board[0]) - 3):
            window = [board[i+k][j+k] for k in range(4)]
            score += evaluate_window(window)

    # Check diagonal (bottom-left to top-right)
    for i in range(3, len(board)):
        for j in range(len(board[0]) - 3):
            window = [board[i-k][j+k] for k in range(4)]
            score += evaluate_window(window)

    return score

def evaluate_window(window):
    # Evaluate a window of 4 cells
    # Return a score between -5 and 5
    # The higher the score, the better the window for the current player
    player_count = np.count_nonzero(window == PLAYER2)
    opponent_count = np.count_nonzero(window == PLAYER1)
    empty_count = np.count_nonzero(window == EMPTY)
    if player_count == 4:
        return 100
    elif player_count == 3 and empty_count == 1:
        return 5
    elif player_count == 2 and empty_count == 2:
        return 2
    elif opponent_count == 3 and empty_count == 1:
        return -4
    else:
        return 0

def get_valid_moves(board):
    # Return a list of valid moves for the current player
    valid_moves = []
    for j in range(len(board[0])):
        if board[0][col] == EMPTY:
            valid_moves.append(j)
    
    return valid_moves

def make_move(board, col, player):
  # Make a move and return the resulting board
  temp_board = board.copy()
  for i in range(len(temp_board)-1, -1, -1):
    if temp_board[i][col] == EMPTY:
      temp_board[i][col] = player
      break

  return temp_board














def make_smart_ai_move():
    ai_col = smart_ai_move()
    drop_piece(ai_col, "O")

def make_random_ai_move():
    # Generate a random move for the AI player
    ai_col = np.random.randint(COLS)
    while is_column_full(ai_col):
        ai_col = np.random.randint(COLS)
    drop_piece(ai_col, "O")

# Modify the main game loop to include user input
while not is_game_over():
    print_board()

    # Ask the user to choose a column
    col = int(input("\nChoose a column (1-{}): ".format(COLS))) - 1

    # Check if the chosen column is full
    while is_column_full(col):
        col = int(input("Column is full, choose another column (1-{}): ".format(COLS))) - 1

    # Drop the piece into the chosen column
    drop_piece(col, "X")

    # Check if the game is over
    if is_game_over():
        break

    print_board()

    make_smart_ai_move()

    # Check if the game is over
    if is_game_over():
        break

print_board()