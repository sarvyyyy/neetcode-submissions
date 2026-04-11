class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            tempe=[]
            for x in i:
                if x!= '.':
                    if x not in tempe:
                        tempe.append(x)
                    else:
                        return False
        
        for j in range(9):
            temp=[]
            for k in range(9):
                if board[k][j]!='.':
                    if board[k][j] not in temp:
                        temp.append(board[k][j])
                    else:
                        return False
        a=0
        b=3
        for l in range(3):
            c=0
            d=3
            for o in range(3):
                tempo=[]
                for m in range(a,b):
                    for n in range(c,d):
                        if board[m][n]!='.':
                            if board[m][n] not in tempo:
                                tempo.append(board[m][n])
                            else:
                                return False
                c+=3
                d+=3
            a+=3
            b+=3
        return True