import os

def searchInFiles(x, path):
    results = []
    # Lấy danh sách các tệp/thư mục trong đường dẫn path
    entries = os.listdir(path)
    # Sắp xếp danh sách theo tên tệp
    entries.sort()
    
    for entry in entries:
        full_path = os.path.join(path, entry)
        # Kiểm tra xem entry có phải là một file không (loại bỏ thư mục)
        if os.path.isfile(full_path):
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    # Đọc file theo từng dòng
                    for line in f:
                        # Nếu tìm thấy từ khóa x trong dòng hiện tại
                        if x in line:
                            # Thêm tuple (tên tệp, dòng chứa từ khóa) vào danh sách kết quả
                            results.append((full_path, line.strip()+"\n"))
                            # Chuyển sang file tiếp theo sau khi tìm thấy dòng đầu tiên chứa x
                            break
            except Exception as e:
                # Nếu có lỗi khi mở/đọc file, có thể bỏ qua file đó hoặc xử lý theo yêu cầu
                pass
    return results
	 	  	      	   	      	    	 	   	 	
