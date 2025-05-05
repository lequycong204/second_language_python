def addNum(a, b):
    c = []
    int_a = 0
    int_b = 0

    # convert list to int
    for i in range(len(a)):
        int_a += a[i] * (10 ** (len(a) - i - 1))

    for i in range(len(b)):
        int_b += b[i] * (10 ** (len(b) - i - 1))

    int_c = int_a + int_b # tổng 2 số nguyên

    # convert int to list
    for i in str(int_c):
        c.append(int(i))   
    
    return c

def multiNum(a, b): #a, b là kiểu list
    c = []
    int_a = ""  # a viết dưới dạng số

    for i in a:
        int_a += str(i)

    for i in range(len(a)):
        rs = 0
    
    return c # c là 1 list

