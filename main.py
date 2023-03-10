logo = '''

  __  .__           __                    __                 
_/  |_|__| ____   _/  |______    ____   _/  |_  ____   ____  
\   __\  |/ ___\  \   __\__  \ _/ ___\  \   __\/  _ \_/ __ \ 
 |  | |  \  \___   |  |  / __ \\  \___   |  | (  <_> )  ___/ 
 |__| |__|\___  >  |__| (____  /\___  >  |__|  \____/ \___  >
              \/             \/     \/                    \/ 
'''
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
import random
def is_game_over(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True
    if ' ' not in [val for row in board for val in row]:
        return True
    return False
def play_game():
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

    for row in board:
        print(' | '.join(row))
        print('---------')

    while not is_game_over(board):
        print("Enter your 'X' position in matrix form (1,2).")
        while True:
            choice = input("Enter your position: ")
            if not choice:
                print("Invalid input. Please enter a position in the format '(1,2)'.")
                continue
            try:
                row, col = map(int, choice[1:-1].split(','))
                if row < 1 or row > 3 or col < 1 or col > 3:
                    print("Invalid input. Please enter a position in the range (1,1) to (3,3).")
                    continue
                if board[row - 1][col - 1] != ' ':
                    print("That position is already taken. Please choose a different one.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a position in the format '(1,2)'.")

        board[row - 1][col - 1] = 'X'

        if is_game_over(board):
            break
        print("Computer's turn:")
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if board[row][col] == ' ':
                break
        board[row][col] = 'O'

        for row in board:
            print(' | '.join(row))
            print('---------')

    if is_game_over(board):
        print("Game over!")
        for row in board:
            print(' | '.join(row))
            print('---------')
        if 'X' in [val for row in board for val in row]:
            print("You win!")
        elif 'O' in [val for row in board for val in row]:
            print("Computer wins!")
        else:
            print("It's a tie!")
def start_game():
    game = input("Press 'Yes' to start the game: ").lower()

    if game == 'yes':
        play_game()
    else:
        print('Invalid input. Please try again.')
        start_game()

    again_play = input("Do you want to play again? Press '1' for Play and '0' for exit: ")
    if again_play == '1':
        start_game()
    else:
        print("Goodbye!")
print("Welcome to TicTacToe!")
print(logo)
start_game()


