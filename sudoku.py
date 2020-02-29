board = [
            
            [5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]
        
        ]

def printBoard(b):
    for x in range(9):    
        if x%3 == 0 and x!=0:
            print("---------------------")
        for y in range(9):
            if y%3 == 0 and y!=0:
                print('| ', end= "")
            print(board[x][y], end=" ")
        print()
        
    return

def possible(x,y,n):
    #check row
    if board[x].count(n) > 1:
        return False
    #check column
    for m in range(9):
        if board[m][y] == n and m != x:
            return False
    
    #check block
    blockX = x % 3
    blockY = y % 3
    if board[blockX][blockY] == n:
        return False
    if board[blockX + 2][blockY + 2] == n:
        return False
    if board[blockX][blockY + 2] == n:
        return False
    if board[blockX + 2][blockY] == n:
        return False
    
    return True

