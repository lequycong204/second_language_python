def check_binary_div5(binary_str):
    '''
    Kiểm tra các số nhị phân 4 chữ số, tách bởi dấu phẩy,
    xem số nào chia hết cho 5 và in ra kết quả.
    '''
    
    # Tách chuỗi đầu vào thành danh sách các số nhị phân
    binary_numbers = binary_str.split(',')
    
    # Lọc ra các số chia hết cho 5
    divisible_by_5 = [num for num in binary_numbers if int(num, 2) % 5 == 0]
    
    # In kết quả, các số được phân tách bằng dấu phẩy
    print(','.join(divisible_by_5))

# Ví dụ chạy chương trình
binary_input = input()
check_binary_div5(binary_input)