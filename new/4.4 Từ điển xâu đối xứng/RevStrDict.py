# Nhập danh sách các chuỗi từ một dòng từ bàn phím
words = input().split()

# Tạo từ điển với khóa là chuỗi s, và giá trị là xâu đối xứng tạo từ s và đảo ngược của s
palindrome_dict = {s: s + s[::-1] for s in words}

# In ra từ điển
print(palindrome_dict)
