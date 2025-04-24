def findCouple(filename):
    """
    Đọc file văn bản chứa các xâu (mỗi xâu cách nhau bởi dấu cách, có thể có nhiều dòng).
    Tìm và trả về một tuple gồm 2 phần tử tương ứng với cặp đôi hoàn hảo.
    Một cặp đôi (a, b) được gọi là hoàn hảo nếu:
      - a khác b,
      - a là đảo ngược của b (nghĩa là chuỗi ab tạo thành xâu đối xứng)
      - a và b không phải là xâu đối xứng (vì khi đó a = b).
    
    Kết quả trả về được sắp theo thứ tự tăng dần (theo thứ tự từ điển).
    Giả sử file chỉ chứa duy nhất 1 cặp đôi hoàn hảo.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        # Đọc toàn bộ file và tách các xâu theo khoảng trắng
        words = []
        for line in file:
            words.extend(line.split())
    
    # Duyệt qua các xâu trong danh sách
    for word in words:
        # Lấy xâu đảo ngược của word
        rev = word[::-1]
        # Kiểm tra điều kiện:
        # - word khác rev (để tránh trường hợp xâu đối xứng)
        # - rev cũng có trong danh sách
        if word != rev and rev in words:
            # Sắp xếp theo thứ tự tăng dần và trả về tuple
            return tuple(sorted([word, rev]))
    
    # Nếu không tìm thấy cặp đôi hoàn hảo nào
    return None
	 	  	      	   	      	    	 	   	 	
