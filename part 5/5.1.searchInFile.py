import os

def searchInFiles(x, path):
    result = []

    # Lặp qua tất cả các tệp trong thư mục
    for filename in os.listdir(path):
        filepath = os.path.join(path, filename)

        # Kiểm tra nếu là file (bỏ qua thư mục con)
        if os.path.isfile(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    for line in f:
                        if x in line:
                            # Thêm bộ (tên tệp, dòng chứa từ khóa) vào danh sách kết quả
                            result.append((filename, line.strip()))
                            break  # Chỉ lấy dòng đầu tiên chứa từ khóa
            except Exception as e:
                break

    # Sắp xếp kết quả theo tên tệp
    result.sort(key=lambda tup: tup[0])
    return result
