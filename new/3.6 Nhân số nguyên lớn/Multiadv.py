#Hoàn thiện hàm multiNum(a, b) theo yêu cầu trong đề bài


def addNum(a, b):
    # Chuyển danh sách thành số nguyên
    num_a = int("".join(map(str, a)))
    num_b = int("".join(map(str, b)))
    
    # Cộng hai số nguyên
    sum_ab = num_a + num_b
    
    # Chuyển kết quả thành danh sách các chữ số
    return list(map(int, str(sum_ab)))

def multiNum(a, b):
    # Danh sách lưu các kết quả trung gian
    partial_results = []
    
    # Nhân từng chữ số của b với số a
    for i, digit_b in enumerate(reversed(b)):
        carry = 0
        temp_result = [0] * i  # Dịch phải theo vị trí
        
        for digit_a in reversed(a):
            product = digit_a * digit_b + carry
            temp_result.insert(0, product % 10)
            carry = product // 10
        
        if carry:
            temp_result.insert(0, carry)
        
        partial_results.append(temp_result)
    
    # Cộng tất cả các kết quả trung gian lại
    result = [0]
    for partial in partial_results:
        result = addNum(result, partial)
    
    return result	 	  	      	   	      	    	 	   	 	
