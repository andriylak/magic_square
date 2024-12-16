def ReadSquareMatrix():
    matrix = []
    firstRow = list(map(int, input().split()))
    matrix.append(firstRow)
    for i in range(len(firstRow) - 1):
        matrix.append(list(map(int, input().split())))
    return matrix

def PrintMatrix(matrix):
    for row in matrix:
        print(*row)

def SearchZero(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column] == 0:
                return row, column

def ColumnSum(matrix, column):
    result = 0
    for i in range(len(matrix)):
        result += matrix[i][column]
    return result

def Diagonal(matrix):
    result = 0
    for i in range(len(matrix)):
        result += matrix[i][i]
    return result

def AntiDiagonal(matrix):
    row = len(matrix) - 1
    result = 0
    while row >= 0:
        result += matrix[row][len(matrix) - row - 1]
        row -= 1
    return result

def MagicSquare(matrix):
    #finding the sum of all rows and columns
    zero_row, zero_col = SearchZero(matrix)
    magicSum, magicSumOf0 = set(), set()
    N = len(matrix)
    for i in range(N):
        if i == zero_row:
            magicSumOf0.add(sum(matrix[i]))
        else:
            magicSum.add(sum(matrix[i]))
    for j in range(N):
        if j == zero_col:
            magicSumOf0.add(ColumnSum(matrix, j))
        else:    
            magicSum.add(ColumnSum(matrix, j))
    #checking if 0 is in diagonals, and calculating the sum of diagonals
    if zero_row != zero_col:
        magicSum.add(Diagonal(matrix))
    else:
        magicSumOf0.add(Diagonal(matrix))
    if zero_row + zero_col != N - 1:
        magicSum.add(AntiDiagonal(matrix))
    else:
        magicSumOf0.add(AntiDiagonal(matrix))
    #checking if the matrix can be magic square 
    if (len(magicSum) != 1) or (len(magicSumOf0) != 1):
        return False
    #calculating the missing number
    missing_value = magicSum.pop() - magicSumOf0.pop()
    matrix[zero_row][zero_col] = missing_value
    return matrix


result = MagicSquare(ReadSquareMatrix())
if result == False:
    print("Can't be magic")
else:
    PrintMatrix(result)
