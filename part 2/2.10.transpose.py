import numpy as np

def inputMatrix():
    m = []
    while True:
        line = input().strip()
        if line == "":
            break
        m.append(list(map(int, line.split())))
    return m

def transpose(m):
    m = np.array(m)
    return m.T
    
def printMatrix(t):
    for i in t:
        print(f"{i} ")


m = inputMatrix()
t = transpose(m)
printMatrix(t)
    