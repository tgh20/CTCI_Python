# Rotate Matrix

def rotate(matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return None
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        last = n -1 - layer
        for i in range(first, last):
            offset = i -first
            top = matrix[first][i] # save top
            
            # left -> top
            matrix[first][i] = matrix[last-offset][first]
            
            # bottom -> left
            matrix[last-offset][first] = matrix[last][last-offset]
            
            # right -> bottom
            matrix[last][last-offset] = matrix[i][last]
            
            # top -> right
            matrix[i][last] = top # right <- saved top
            
    return matrix

def main():
    matrix = [[1, 2, 3, 4],
                     [5, 6, 7, 8],
                     [9, 10, 11, 12],
                     [13, 14, 15, 16]]
    print('matrix : ', matrix)
    print('rotate : ', rotate(matrix))
    
if __name__ == "__main__":
    main()