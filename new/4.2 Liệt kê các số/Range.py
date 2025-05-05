#Viết chương trình tìm tất cả các số chia hết cho 11 nhưng không phải bội số của 3, nằm trong đoạn a và b (tính cả a và b). 
#Với a, b là các số nguyên được nhập từ bàn phím.
#Các số thu được sẽ được in thành chuỗi trên một dòng, cách nhau bằng dấu chấm phẩy và dấu cách “; ”.

def findNumbers(a, b):
    result = [x for x in range(min(a, b), max(a, b) + 1) if x % 11 == 0 and x % 3 != 0]
    print("; ".join(map(str, result)))

# Nhập giá trị a, b
a = int(input())
b = int(input())
findNumbers(a, b)