def addNum(a, b):
    '''
    Cho 2 số nguyên a, b được biểu diễn bởi 2 danh sách
    thực hiện phép cộng 2 số a, b trên 2 danh sách theo quy tắc cộng thông thường. kết quả trả về là 1 danh sách biểu diễn tổng a+b
    ví dụ 
    a = [1,2,4,5]
    b =   [7,8,9]
   
    c = [2,0,3,4]
    '''
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

print(addNum([1,2,4,5], [7,8,9])) # [2,0,3,4])