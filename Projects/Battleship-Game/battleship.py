from random import randint
from copy import deepcopy

board = []
user_hit = 0
comp_hit = 0
def create_board(board):
    for x in range(5):
        board.append(["O"] * 5)
    user_board = deepcopy(board)
    computer_board = deepcopy(board)
    return user_board,computer_board

def print_usrboard(user_board):
    print "\nUSER BOARD\n"
    for row in user_board:
        print " ".join(row)

def print_compboard(computer_board):
    print "\nCOMPUTER BOARD\n"
    for row in computer_board:
        print " ".join(row)

def placeUserShips(user_board):

    print "Please place your 5 ships!\n"
    count =0
    for ship in range (5):
        print "SHIP ",count+1
        row,column = getCoordinates();
        user_board[row][column] = 'S'
        count = count+1

def placeComputerShips(computer_board):

    print "\nPlacing computer ships!\n"

    for ship in range (5):
        row,column=getRandomCoordinates()
        computer_board[row][column] = 'S'


def getCoordinates():

    valid = False

    while valid is False:

        row = int(raw_input("Enter Row Number:"))
        column = int(raw_input("Enter Column Number:"))
        valid = validateUserCoordinates(row,column)
    return row,column

def validateUserCoordinates(row,column):
    if (row < 0 or row > 4) or (column <0 or column > 4):
        print "The entered coordinates are not valid\n"
        return False
    elif user_board[row][column]=='S':
        print "you have already placed a ship there, Please select different coordinates\n"
        return False
    else:
        return True

def getRandomCoordinates():
    valid = False

    while valid is False:

        row = randint(0, len(computer_board) - 1)
        column = randint(0, len(computer_board) - 1)
        if user_board[row][column]=='S':
            print "Already selected coordinates,IGNORE!\n"
        else:
            valid = True
    return row,column

def random_row(computer_board):
    return randint(0, len(computer_board) - 1)

def random_col(computer_board):
    return randint(0, len(computer_board) - 1)

def user_turn(computer_board,user_hit):
    print "\nUSER\n"
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    if computer_board[guess_row][guess_col] == "S":
        print "Congratulations! You sunk my battleship!"
        computer_board[guess_row][guess_col]="-1"
        user_hit += 1

    else:

        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(computer_board[guess_row][guess_col] == "X" or computer_board[guess_row][guess_col]=="-1"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            computer_board[guess_row][guess_col] = "X"
    return user_hit

def computer_turn(user_board,computer_hit):
    print "\nCOMPUTER\n"

    guess_row = random_row(user_board)
    guess_col = random_col(user_board)

    print "********"
    print guess_row
    print guess_col
    print "********"

    if user_board[guess_row][guess_col] == "S":
        print "Congratulations! You sunk my battleship!"
        user_board[guess_row][guess_col]="-1"
        computer_hit += 1

    else:

        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(user_board[guess_row][guess_col] == "X" or user_board[guess_row][guess_col] == "-1"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            user_board[guess_row][guess_col] = "X"
    return computer_hit

print "Let's play Battleship!\n"

user_board,computer_board = create_board(board)

print_usrboard(user_board)
print_compboard(computer_board)

placeUserShips(user_board)
print_usrboard(user_board)

placeComputerShips(computer_board)
print_compboard(computer_board)

for turn in range(5):

    print "Turn",turn+1

    user_hit = user_turn(computer_board,user_hit)
    print_compboard(computer_board)
    comp_hit = computer_turn(user_board,comp_hit)
    print_usrboard(user_board)

if user_hit>comp_hit:
    print "Congratulations User ! You won the game"
elif user_hit<comp_hit:
    print "Sorry ! Better luck next time"
else:
    print "Its a Tie!"


print "Hit Score \n User : %d\tComputer : %d"%(user_hit,comp_hit)
