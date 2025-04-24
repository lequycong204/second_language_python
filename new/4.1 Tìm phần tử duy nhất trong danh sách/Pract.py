
#Hoàn thiện hàm findUniq(a), tìm và trả lại giá trị xuất hiện duy nhất 1 lần trong danh sách a

def findUniq(a):
    unique_element = 0
    for num in a:
        unique_element ^= num  # Sử dụng phép XOR để tìm phần tử xuất hiện duy nhất
    return unique_element

