# Khởi tạo số dư tài khoản
balance = 0

print()

while True:
    transaction = input().strip()  # Nhập từng dòng và loại bỏ khoảng trắng thừa
    if not transaction:  # Dừng khi gặp dòng trống
        break
    
    parts = transaction.split()  # Tách dữ liệu nhập vào thành danh sách
    if len(parts) != 2:  # Kiểm tra định dạng hợp lệ
        
        continue
    
    action, amount = parts[0], parts[1]

    if not amount.isdigit():  # Kiểm tra số tiền có phải là số không
        
        continue

    amount = int(amount)

    if action == "D":  # Gửi tiền
        balance += amount
    elif action == "W":  # Rút tiền
        balance -= amount
    else:
        continue

# In số dư cuối cùng
print(balance)
	 	  	      	   	      	    	 	   	 	
