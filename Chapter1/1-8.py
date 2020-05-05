# Zero Matrix

# Solution1
def setZeros1(matrix):
    r = len(matrix)
    c = len(matrix[0])
    
    row = [False] * r
    col = [False] * c
    
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                row[i] = True
                col[j] = True
                
    for i in range(r):
        if row[i] == True:
            matrix[i] = [0] * c
        else:
            for j in range(c):
                if col[j] == True:
                    matrix[i][j] = 0
    
    return matrix

# Solution2
def setZeros2(matrix):
    rowHasZero = False
    colHasZero = False
    
    # Check if first row has a zero
    for j in range(len(matrix[0])):
        if matrix[0][j] == 0:
            rowHasZero = True
            break
            
    # Check if first column has a zero
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            colHasZero = True
            break
    
    # Check for zeros in the rest of the array
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
                
    # Nullify rows based on values in first column
    for i in range(1, len(matrix)):
        if matrix[i][0] == 0:
            nullifyRow(matrix, i)
            
    # Nullify columns based on values in first row
    for j in range(1, len(matrix[0])):
        if matrix[0][j] == 0:
            nullifyColumn(matrix, j)
            
    # Nullify first row
    if rowHasZero:
        nullifyRow(matrix, 0)
        
    # Nullify first column
    if colHasZero:
        nullifyColumn(matrix, 0)
        
    return matrix
        
def nullifyRow(matrix, row):
    for j in range(len(matrix[0])):
        matrix[row][j] = 0
        
def nullifyColumn(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0

def main():
    matrix = [[1, 2, 3, 4],
                     [5, 6, 7, 8],
                     [9, 0, 11, 12],
                     [13, 14, 15, 0]]
    print('matrix : ', matrix)
    print('# Solution1     setZeros : ', setZeros1(matrix))
    
    matrix = [[1, 2, 3, 4],
                     [5, 6, 7, 8],
                     [9, 0, 11, 12],
                     [13, 14, 15, 0]]
    print('# Solution2     setZeros : ', setZeros2(matrix))
    
if __name__ == "__main__":
    main()