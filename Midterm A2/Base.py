import math
def projection_motion(v0, theta):
    """
    v0 và theta là hai giá trị đầu vào kiểu số thực cho bài toán ném xiên
    
    Thực hiện theo các yêu cầu CÂU 1 của đề bài
    """
    
    if v0 <= 0 or theta < 0 or theta > 90:
        return "ERROR"  
     
    g = 9.81 

    # Độ cao cực đại
    H = ((v0 ** 2) * math.sin(math.radians(theta)) * math.sin(math.radians(theta))) / (2*g)
    H = round(H, 5)

    # Tầm ném xa
    R = (v0 ** 2) * math.sin(2 * math.radians(theta)) / g
    R = round(R, 5)

    # Thời gian di chuyển trên không trung
    T = 2 * v0 * math.sin(math.radians(theta)) / g
    T = round(T, 5)
    return H, R, T


def caculate_time(t1, t2):
    """
    t1, t2 là hai tham số đầu vào có dạng chuỗi. hh:mm
    
    Tính toán trả về khoảng thời gian theo yêu cầu CÂU 2 của đề bài.
    """
    t1 = str(t1)
    t2 = str(t2)

    if len(t1) != 5 or len(t2) != 5:
        return "ERROR"

    # Convert time to int
    time1 = [int(t1[:2]), int(t1[3:])]
    time2 = [int(t2[:2]), int(t2[3:])]

    if time1[0] < 0 or time1[0] > 23:
        return "ERROR"
    
    if time2[0] < 0 or time2[0] > 23:
        return "ERROR"
    
    if time1[1] < 0 or time1[1] > 59 or time2[1] < 0 or time2[1] > 59:
        return "ERROR"
    
    # Convert to minute
    time1_minute = time1[0] * 60 + time1[1]
    time2_minute = time2[0] * 60 + time2[1]

    # Tính khoảng thời gian
    minus = time2_minute - time1_minute
    if minus < 0:
        minus = time2_minute - time1_minute + 24 * 60
    
    minus_hour = minus // 60
    minus_min = minus % 60 
    # Convert to hh:mm
    
    if minus_min < 10:
        minus_min = f"0{minus_min}"
    
    if minus_hour < 10:
        minus_hour = f"0{minus_hour}"
    return f"{minus_hour}:{minus_min}"


print(caculate_time("04:20", "24:22"))