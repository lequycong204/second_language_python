# Nhập số nguyên dương n từ bàn phím
n = int(input())

# Tạo dictionary chứa (i, và đảo ngược của i*i)
result = {}
for i in range(1, n+1):
    squared = i * i
    reversed_squared = int(str(squared)[::-1])  # Đảo ngược số bình phương
    result[i] = reversed_squared

# In ra dictionary
print(result)
