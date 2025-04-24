from Village import Village

def read_village_from_file(fileName):
    """
    Hàm đọc tệp dữ liệu về phường. Hàm này thực hiện đọc dữ liệu từ các phường
    từ tệp fileName sau đó tạo ra các đối tượng Village tương ứng và lưu vào 1 danh 
    sách, sau khi kết thúc việc đọc dữ liệu, hàm này trả lại danh sách các phường
    đã tạo được.
    
    dữ liệu trong tệp fileName được lưu dưới dạng csv,
    dòng đầu tiên là tên các thuộc tính của phường: vid,name,town
    các dòng tiếp theo, mỗi dòng chứa thông tin của 1 phường, mỗi thông tin cách nhau bởi 1 dấu phẩy ,
    Ví dụ:
    vid,name,town
    D-00001,Phúc Xá,Ba Đình
    B-00004,Trúc Bạch,Ba Đình
    D-00006,Vĩnh Phúc,Ba Đình
    """
    village_list = []
    with open(fileName, 'r') as f:
        next(f)  # Skip header
        for line in f:
            vid, name, town = line.strip().split(',')
            village = Village(name, vid, town)
            village_list.append(village)
    return village_list
    
def read_village_student_from_file(fileName, village_list):
    
    """
    Hàm thực hiện việc đọc file số lượng thí sinh thi vào cấp 3 của mỗi phường để bổ sung thêm thông tin
    vào thuộc tính student của mỗi Village trong village_list,
    Nhiệm vụ của hàm này là đọc dữ liệu số lượng thí sinh thi vào cấp 3 theo năm và ghi vào thuộc tính student
    của phường đó. Chú ý là việc thêm thông tin cần theo đúng mã phường (vid) của phường đó.
    
    fileName chứa thông tin về số lượng thí sinh thi vào cấp 3 theo từng năm
    được lưu dưới dạng csv.
    Dòng đầu tiên là tên các thuộc tính của dữ liệu: vid,2018,2019,2020,2021,2022,2023 (mã phường và các năm khảo sát)
    dữ liệu của mỗi phường được lưu trên 1 dòng bao gồm mã phường và số lượng thí sinh tương ứng với năm đó.
    
    Ví dụ về file:
    
    vid,2018,2019,2020,2021,2022,2023
    D-00001,7408,7554,7674,7775,7875,7969
    B-00004,6758,6883,6986,7074,7148,7277
    D-00006,7000,7114,7197,7331,7470,7566
    D-00007,7377,7492,7592,7710,7843,7942
    """
    vid_to_village = {village.vid: village for village in village_list}	 	  	      	   	      	    	 	   	 	
    with open(fileName, 'r') as f:
        header = f.readline().strip().split(',')
        years = [int(year) for year in header[1:]]
        for line in f:
            fields = line.strip().split(',')
            vid = fields[0]
            student_numbers = [int(num) for num in fields[1:]]
            if vid in vid_to_village:
                village = vid_to_village[vid]
                for year, num in zip(years, student_numbers):
                    village.student[year] = num
    
def get_Hanoi_student_change(village_list):
    """
    Hàm thực hiện trả về danh sách các năm (int)được sắp xếp tăng dần theo 
    số lượng thí sinh thi vào cấp 3 TĂNG THÊM mỗi năm trên toàn thành phố Hà Nội.
    output: [2019, 2020, 2021, 2022, 2023]
    """
    
    if not village_list:
        return []
    years = sorted(village_list[0].student.keys())
    total_students = {year: sum(v.student.get(year, 0) for v in village_list) for year in years}
    increases = [(years[i], total_students[years[i]] - total_students[years[i - 1]]) 
                 for i in range(1, len(years))]
    sorted_increases = sorted(increases, key=lambda x: x[1])
    return [year for year, _ in sorted_increases]
    
def get_top_village_by_year(village_list, rank, year):
    
    """
    Hàm trả về 1 danh sách tên phường với xếp hạng ( = rank) 
    và có số lượng thí sinh trong năm (year) 
    lớn hơn giá trị trung bình của tất cả số thí sinh của thành phố Hà Nội trong năm đó
    Danh sách được sắp sếp theo số lượng thí sinh.
    
    Ví dụ: rank = 2, year = 2018
    Tìm tất cả tên phường trong đó phường là phường loại 2 có số thí sinh thi vào cấp 3 
    năm 2018 lớn hơn trung bình số thí sinh thi vào cấp 3 năm 2018 trên toàn thành phố Hà Nội.
    output: ['Cống Vị',...,'Yên Hòa']
    """
    
    total_students = sum(v.student.get(year, 0) for v in village_list)
    num_villages = sum(1 for v in village_list if year in v.student)
    average = total_students / num_villages if num_villages > 0 else 0
    selected_villages = [v for v in village_list 
                         if v.get_rank() == rank and year in v.student and v.student[year] > average]
    sorted_villages = sorted(selected_villages, key=lambda v: v.student[year])
    return [v.name for v in sorted_villages]
    
def sorted_town_by_avg_student(village_list):
    
    """
    Hàm trả về một danh sách các quận (town) được xắp sếp tăng dần
    theo số lượng thí sinh thi cấp 3 trung bình của các phường trong quận đó.
    Giá trị trung bình được tính trên tất cả các năm cho tất cả các phường thuộc quận đó
    
    output: ['Ba Đình','Cầu Giấy','Hoàn Kiếm','Long Biên','Tây Hồ']
    """
    if not village_list:
        return []
    years = list(village_list[0].student.keys())
    town_to_villages = {}	 	  	      	   	      	    	 	   	 	
    for village in village_list:
        town = village.town
        if town not in town_to_villages:
            town_to_villages[town] = []
        town_to_villages[town].append(village)
    town_averages = []
    for town, villages in town_to_villages.items():
        if villages and years:
            total_students = sum(sum(v.student.get(year, 0) for year in years) for v in villages)
            num_villages = len(villages)
            num_years = len(years)
            average = total_students / (num_villages * num_years)
            town_averages.append((town, average))
    sorted_towns = sorted(town_averages, key=lambda x: x[1])
    return [town for town, _ in sorted_towns]
    