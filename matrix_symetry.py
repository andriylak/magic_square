def ReadSquareMatrix():
    matrix = []
    firstRow = list(map(int, input().split()))
    matrix.append(firstRow)
    for i in range(len(firstRow) - 1):
        matrix.append(list(map(int, input().split())))
    return matrix

def SymetryByTheDiagonal(matrix):
    N = len(matrix)
    for i in range(N):
        for j in range(N):
            if matrix[i][j] != matrix[j][i]:
                return 0
    return 1

def TurnOverTheMatrix(matrix):
    result = []
    for i in range(len(matrix) - 1, -1, -1):
        result.append(matrix[i])
    return result

def SymetryByTheAntiDiagonal(matrix):
    return SymetryByTheDiagonal(TurnOverTheMatrix(matrix))


def SymetryByTheCenter(matrix):
    N = len(matrix)
    for i in range(N):
        for j in range(N//2):
            if matrix[i][j] != matrix[i][N-j-1]:
                return 0
    return 1

m = ReadSquareMatrix()
print(SymetryByTheDiagonal(m), SymetryByTheAntiDiagonal(m), SymetryByTheCenter(m))
        
        