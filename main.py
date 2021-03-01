board = [' ' for x in range(10)]


def insertLetter(letter, pos):
    board[pos] = letter


def spaceCheck(pos):
    return board[pos] == ' '


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def printBoard(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ')
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')
    print('   |   |   ')


def checkWinner(board, letter):
    return ((board[1] == letter and board[2] == letter and board[3] == letter) or \
            (board[4] == letter and board[5] == letter and board[6] == letter) or \
            (board[7] == letter and board[8] == letter and board[9] == letter) or \
            (board[1] == letter and board[4] == letter and board[7] == letter) or \
            (board[2] == letter and board[5] == letter and board[8] == letter) or \
            (board[3] == letter and board[6] == letter and board[9] == letter) or \
            (board[1] == letter and board[5] == letter and board[9] == letter) or \
            (board[3] == letter and board[5] == letter and board[7] == letter))


def playerMove():
    run = True
    while run:
        move = input("Please select a position to enter the X between 1 to 9: ")
        try:
            move = int(move)
            if 0 < move < 10:
                if spaceCheck(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print("Sorry, this space is occupied")
            else:
                print("Please type a number between 1 and 9")

        except:
            print("Please type a number")


def computerMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if checkWinner(boardcopy, let):
                move = i
                return move

    cornersOpen = []

    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    if 5 in possibleMoves:
        move = 5
        return move
    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def main():
    print("Welcome to the game!")
    printBoard(board)
    while not (isBoardFull(board)):
        if not (checkWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print("You loose!")
            break
        if not (checkWinner(board, 'X')):
            move = computerMove()
            if move == 0:
                print("")
            else:
                if not(isBoardFull(board)):
                    insertLetter('O', move)
                    print('Computer placed O on position: ', move, ' : ')
                    printBoard(board)
        else:
            print("You win!")
            break

    if isBoardFull(board):
        print("Tie game")


while True:
    x = input("Do you want to play? (y/n): ")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('------------')
        main()
    else:
        break
