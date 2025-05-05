

def zeroMove(fileName):
    '''
    Hoàn thiện phương thức zeroMove(fileName), phương thức này thực hiện việc đọc các số nguyên

    từ file fileName, các số nguyên được viết trên 1 dòng, mỗi số cách nhau bởi 1 dấu cách. Lưu các số này vào
    
    trong một danh sách theo đúng thứ tự trong fileName
    
    Thực hiện việc di chuyển các số 0 về phía bên phải của danh sách trong khi vẫn giữ nguyên thứ tự của các số khác.
    
    Hàm zeroMove trả lại danh sách sau khi thực hiện việc di chuyển số 0.
    
    
    
    > Ví dụ cho file data.txt có nội dung như sau:
    
    0 1 0 3 12
    
    > Kết quả trả về là
    
    [1, 3, 12, 0, 0]
    '''
    
    with open(fileName, 'r', encoding='utf-8') as f:
        # Đọc toàn bộ nội dung của file (giả sử số nằm trên 1 dòng)
        line = f.readline().strip()
        # Chuyển chuỗi thành danh sách số nguyên
        numbers = [int(num) for num in line.split()]
    
    # Tạo danh sách chứa các số khác 0 theo thứ tự ban đầu
    nonzeros = [num for num in numbers if num != 0]
    # Đếm số lượng số 0 trong danh sách ban đầu
    zeros_count = numbers.count(0)
    
    # Nối danh sách các số khác 0 với danh sách chứa số 0
    result = nonzeros + [0] * zeros_count
    return result	 	  	      	   	      	    	 	   	 	
