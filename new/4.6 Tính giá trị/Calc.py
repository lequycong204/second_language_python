# Nhập số a từ bàn phím
a = input()

# Tính giá trị của biểu thức a + aa + aaa + aaaa
term1 = int(a)        # a
term2 = int(a * 2)    # aa
term3 = int(a * 3)    # aaa
term4 = int(a * 4)    # aaaa

# Tổng các giá trị
result = term1 + term2 + term3 + term4

# In kết quả
print(result)
