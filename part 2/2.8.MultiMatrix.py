import numpy as np

def inputMatrix():
    m = []
    length = []
    line = input().strip()
    if line != "":
        length = [int(i) for i in line.split()]
    
    for i in range(length[0]):
        line = input().strip()
        if line == "":
            break
        m.append(list(map(int, line.split())))

        # Check dimension condition
        if len(m[i]) != length[1]:
            raise ValueError("Each row must have the same number of columns")
    return m
        
	
def multiMatrix(m1, m2):
    m1 = np.array(m1)
    m2 = np.array(m2)
    if m1.shape[1] != m2.shape[0]:
        raise ValueError("Cannot multiply matrices with incompatible dimensions")
    r = np.dot(m1, m2)
    return r

def printMatrix(m):
    for i in m:
        print(f"{i} ")

m1 = inputMatrix()
m2 = inputMatrix()

mm = multiMatrix(m1, m2)
printMatrix(mm)