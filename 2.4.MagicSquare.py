import numpy as np

def inputMatrix():
    m = []
    while True:
        try:
            line = input().strip()
            if line == "":
                break 
            row = list(map(int, line.split())) 
            m.append(row)
        except EOFError:
            break
    return m

def isMagicSquare(m):
    if len(m) != len(m[0]): 
        return False

    array = np.array(m)
    
    # Calculate the sum of each row and column
    sum_row = np.sum(array, axis=1)
    sum_col = np.sum(array, axis=0)

    if not np.all(sum_row == sum_row[0]):
        return False
    
    if not np.all(sum_col == sum_col[0]):
        return False
    
    # Calculate the sum of the main diagonal and sub-diagonal
    sum_main_diag = np.trace(array)
    sum_sub_diag = np.trace(np.fliplr(array))

    return sum_main_diag == sum_sub_diag == sum_row[0]


m = inputMatrix()
print(isMagicSquare(m))