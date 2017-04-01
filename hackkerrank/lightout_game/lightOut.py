def nextMove(player,board):
    print(board[0][1])
    colNo=0
    rowNo=0
    for i in range(0,len(board)):
        for j in range(0,len(board[i])):
            if board[i][j]==1:
                print("here")
                colNo=j
                rowNo=i
                break
    print rowNo, colNo
#If player is 1, I'm the first player.
#If player is 2, I'm the second player.
player = raw_input()

#Read the board now. The board is a 8x8 array filled with 1 or 0.
board = []
for i in xrange(0, 8):
    board.append(raw_input())

nextMove(player,board)