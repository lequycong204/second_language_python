def customSort(a):
    '''
    Hàm thực hiện sắp xếp các phần tử trong a, theo thứ tự:
    - Chẵn bên trái, lẻ bên phải
    - Chẵn tăng dần, lẻ giảm dần
    ví dụ a  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    kết quả là [2, 4, 6, 8, 10, 9, 7, 5, 3, 1]
    '''
    if not a:
        raise ValueError("Danh sách không được rỗng")

    even = []
    odd = []

    for element in a:
        if element % 2 == 0:
            even.append(element)
        else:
            odd.append(element)

    even.sort()
    odd.sort(reverse=True)

    return even + odd

# Test
a  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(customSort(a))
