import math

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
    n = len(nums)
    if n < 3:
        return -1
    
    # Compute min_left: minimum value to the left of each index
    min_left = [0] * n
    current_min = nums[0]
    for j in range(1, n):
        min_left[j] = current_min
        if nums[j] < current_min:
            current_min = nums[j]
    
    # Compute min_right: minimum value to the right of each index
    min_right = [0] * n
    current_min = nums[n-1]
    for j in range(n-2, -1, -1):
        min_right[j] = current_min
        if j > 0 and nums[j] < current_min:
            current_min = nums[j]
    
    # Find all valid mountain sums
    sums = []
    for j in range(1, n-1):
        if min_left[j] < nums[j] and min_right[j] < nums[j]:
            sums.append(min_left[j] + nums[j] + min_right[j])
    
    # Return the minimum sum or -1 if no mountains exist
    return min(sums) if sums else -1

def cosin_distance(v1, v2):
    """
    Tính khoảng cách cosin của 2 vector,
    input: v1, v2 là danh sách có cùng kích thước
    Cosin distance được tính theo công thức:
    cho trong đề bài.
    """
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same length")
    
    # Compute dot product
    dot = sum(a*b for a, b in zip(v1, v2))
    # Compute L2 norms
    norm1 = math.sqrt(sum(a ** 2 for a in v1))
    norm2 = math.sqrt(sum(b ** 2 for b in v2))
    
    # If either vector is zero, cosine similarity is undefined; return 1
    if math.isclose(norm1, 0.0) or math.isclose(norm2, 0.0):
        return 1.0
    
    # Compute cosine similarity and distance
    cos_sim = dot / (norm1 * norm2)
    return round((cos_sim), 3)
    
def get_hightest_gdp(country_list):
    """
    country_list là một danh sách trong đó mỗi phần tử là một tuple có cấu trúc như sau:
    (country_id, region, gdp, area)
    country_id: mã quốc gia
    region: khu vực (Asia, EU, USA...)
    gdp: tổng thu nhập quốc dân
    area: diện tích tương ứng với quốc gia đó
    tìm ra và trả về một danh sách 3 mã quốc gia
    có chỉ số gdp cao nhất được sắp xếp giảm dần theo chỉ số gdp, nếu cùng chỉ số gdp thì sắp giảm dần theo mã quốc gia country_id
    """
    
    # Sort by GDP descending, then country_id descending
    sorted_countries = sorted(country_list, key=lambda x: (x[2], x[0]), reverse=True)
    # Take top 3 (or fewer if list is shorter)
    top_3 = sorted_countries[:3]
    # Return list of country_ids
    return [country[0] for country in top_3]	 	  	      	   	      	    	 	   	 	
