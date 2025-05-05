import math

def is_prime(n):
    """Kiểm tra n có phải là số nguyên tố hay không."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def findLuckyNumber(filename):
    """
    Đọc file văn bản chứa các xâu, mỗi xâu cách nhau bởi dấu cách, có thể nhiều dòng.
    Tìm số may mắn (số nguyên tố có tổng các chữ số chia hết cho 5) trong file.
    Giả sử file chỉ chứa duy nhất 1 số may mắn.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        # Đọc từng dòng trong file
        for line in f:
            # Tách các xâu theo khoảng trắng
            tokens = line.split()
            for token in tokens:
                # Kiểm tra xem xâu có phải là số hay không
                if token.isdigit():
                    num = int(token)
                    # Kiểm tra số nguyên tố và tổng các chữ số chia hết cho 5
                    if is_prime(num) and sum(int(d) for d in token) % 5 == 0:
                        return num
    # Nếu không tìm thấy số may mắn nào
    return None
	 	  	      	   	      	    	 	   	 	
