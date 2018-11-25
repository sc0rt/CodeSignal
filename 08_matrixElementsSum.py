def matrixElementsSum(matrix):
    sum = 0
    for i in range(0,len(matrix)-1):
        for j in range(0,len(matrix[i])):
            if matrix[i][j] == 0:
                matrix[i+1][j] = 0
    for row in matrix:
        for element in row:
            sum = sum + element
    return sum
