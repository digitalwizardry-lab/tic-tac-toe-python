from os import system, name

# Special unicode characters
HORIZONTAL_LINE = '\u2501'
VERTICAL_LINE = '\u2503'

LEFT_TOP_CORNER = '\u250f'
RIGHT_TOP_CORNER = '\u2513'
LEFT_BOTTOM_CORNER = '\u2517'
RIGHT_BOTTOM_CORNER = '\u251b'

LEFT_T_INTERSECTION = '\u2523'
RIGHT_T_INTERSECTION = '\u252b'
TOP_T_INTERSECTION = '\u2533'
BOTTOM_T_INTERSECTION = '\u253b'

CROSS_INTERSECTION = '\u254b'

def initialize_board(size=3):
    return [[str(size * i + j + 1) for j in range(size)] for i in range(size)]

def clear_screen():
    system('cls' if name == 'nt' else 'clear')

def display_board(board, player, turn):
    size = len(board)
    vspacer = ' ' + VERTICAL_LINE + ' '
    hspacer = HORIZONTAL_LINE * 3

    # Clear the screen before displaying the board
    clear_screen()
    
    # Print turn and player
    print(f"Turn {turn}, Player {player}")
    
    # Print the top border
    print(LEFT_TOP_CORNER + hspacer + (TOP_T_INTERSECTION + hspacer) * (size - 1) + RIGHT_TOP_CORNER)
    
    for i in range(size * 2 - 1):
        if i % 2:
            # Print the horizontal separators
            print(LEFT_T_INTERSECTION + hspacer + (CROSS_INTERSECTION + hspacer) * (size - 1) + RIGHT_T_INTERSECTION)
        else:
            # Print the board cells
            line = board[i // 2]
            print(VERTICAL_LINE + ' ' + vspacer.join(line) + ' ' + VERTICAL_LINE)
    
    # Print the bottom border
    print(LEFT_BOTTOM_CORNER + hspacer + (BOTTOM_T_INTERSECTION + hspacer) * (size - 1) + RIGHT_BOTTOM_CORNER)

def get_valid_move(board):
    size = len(board)
    while True:
        move = input(f"Enter your move (1-{size * size}): ")
        if move.isdigit():
            move = int(move)
            if 1 <= move <= size * size:
                pos = move - 1
                row = pos // size
                col = pos % size
                if board[row][col] not in ['X', 'O']:
                    return move
                else:
                    print("This position is already taken. Try another move.")
            else:
                print(f"Invalid input. Please enter a number between 1 and {size * size}.")
        else:
            print("Invalid input. Please enter a valid number.")

def make_move(board, position, player):
    size = len(board)
    pos = int(position) - 1
    row = pos // size
    col = pos % size
    
    if board[row][col] not in ['X', 'O']:
        board[row][col] = player
        return True
    else:
        print("Invalid move, try again.")   # redundant checking
        return False

def check_winner(board):
    size = len(board)
    lines = []

    # Rows and Columns
    for i in range(size):
        lines.append(board[i])                              # horizontal
        lines.append([board[j][i] for j in range(size)])    # vertical

    # Diagonals
    lines.append([board[i][i] for i in range(size)])
    lines.append([board[i][size - i - 1] for i in range(size)])
    
    for line in lines:
        if len(set(line)) == 1:
            return line[0] 
        
    return None

def is_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def main_game():
    # Initialize the game
    board = initialize_board()
    turn = 1
    player = 'X'

    # Main game loop
    while True:
        display_board(board, player, turn)
        move = get_valid_move(board)
        
        if make_move(board, move, player):
            winner = check_winner(board)
            if winner:
                display_board(board, player, turn)
                print(f"Player {winner} wins!")
                break
            elif is_draw(board):
                display_board(board, player, turn)
                print("It's a draw!")
                break
            
            turn += 1
            player = 'O' if player == 'X' else 'X'

if __name__ == '__main__':
    main_game()

