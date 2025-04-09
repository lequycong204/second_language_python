


def find_minimum_sum(nums):
    """
    Tìm đỉnh núi có tổng nhỏ nhất.
    Cho một danh sách số nguyên dương nums
    Bộ 3 chỉ số i, j, k được gọi là đỉnh núi nếu thỏa mãn:
    i < j < k và nums[i] < nums[j] và nums[j] > nums[k]
    Ví dụ 1: input [8,6,1,5,3]
    với i = 2, j = 3 k = 4 tương ứng tạo thành một đỉnh núi với tổng bằng 9 (1 + 5 + 3)
    output: 9
    Ví dụ 2: input [5,4,8,7,10,2]
    i = 0, j = 2, k = 5 tạo thành một đỉnh núi với tổng bằng 15.
    i = 1, j = 4, k = 5 tạo thành một đỉnh núi với tổng bằng 16.
    output : 13
    Nếu không tồn tại đỉnh núi nào trong danh sách
    output : -1
    """
    
    ans = nums[0] + nums[1] + nums[2]
    
    countTriplets = 0
    
    for i in range (0, len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if (nums[i] < nums[j] and nums[j] > nums[k]):
                    countTriplets += 1
                    ans = min(ans, nums[i] + nums[j] + nums[k])
    
    if (countTriplets > 0):
        return ans
    return -1

def cosin_distance(v1, v2):
    """
    Tính khoảng cách cosin của 2 vector,
    input: v1, v2 là danh sách có cùng kích thước
    Cosin distance được tính theo công thức:
    cho trong đề bài.
    """
    return -1
    
def get_hightest_gdp(country_list):
    """
    Tìm ra và trả về một danh sách 3 mã quốc gia
    có chỉ số gdp cao nhất được sắp xếp giảm dần theo chỉ số gdp.
    """

    results = []  # Lưu (country_id, gdp)

    # Bước 1: Lấy country_id và gdp đưa vào list mới
    for country in country_list:
        name = country[0]      # Lấy mã quốc gia
        gdp = country[2]       # Lấy GDP
        results.append((name, gdp))  # Thêm tuple vào list

    # Bước 2: Sắp xếp giảm dần theo gdp
    def take_gdp(country):
        return country[1]  # lấy gdp

    results.sort(key=take_gdp, reverse=True)

    # Bước 3: Lấy top 3 country_id có gdp cao nhất
    ans = []
    countCountries = 0

    for country in results:
        if countCountries < 3:   # chỉ lấy đúng 3 nước
            ans.append(country[0])
            countCountries += 1

    return ans