import numpy as np
def inputMatrix():
    m = []

    while True:
        line = input().strip()
        if line == "":
            break
        m.append(list(map(int, line.split())))
    return m


def isUpperTriangleMatrix(m):
    m = np.array(m)
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            if j < i:
                if m[i][j] != 0:
                    return False
    return True
    
    
m = inputMatrix()
print(isUpperTriangleMatrix(m))

