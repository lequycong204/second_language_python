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
    try:
        with open(fileName, 'r', encoding='utf-8') as file:
            # Skip header line
            next(file)
            for line in file:
                data = line.strip().split(',')
                if len(data) >= 3:
                    vid, name, town = data[0], data[1], data[2]
                    village = Village(name, vid, town)
                    village_list.append(village)
    except Exception as e:
        print(f"Error reading file {fileName}: {e}")
    
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
    # Create a dictionary for quick lookup of villages by vid
    village_dict = {village.vid: village for village in village_list}
    
    try:
        with open(fileName, 'r', encoding='utf-8') as file:
            # Read header to get years
            header = next(file).strip().split(',')
            years = [int(year) for year in header[1:] if year.isdigit()]
            
            for line in file:
                data = line.strip().split(',')
                if len(data) >= len(header):
                    vid = data[0]
                    if vid in village_dict:
                        village = village_dict[vid]
                        for i, year in enumerate(years):
                            try:
                                student_count = int(data[i+1])
                                village.student[year] = student_count
                            except (ValueError, IndexError):
                                pass
    except Exception as e:
        print(f"Error reading student data from {fileName}: {e}")
    
    
def get_Hanoi_student_change(village_list):
    """
    Hàm thực hiện trả về danh sách các năm (int)được sắp xếp tăng dần theo 
    số lượng thí sinh thi vào cấp 3 TĂNG THÊM mỗi năm trên toàn thành phố Hà Nội.
    output: [2019, 2020, 2021, 2022, 2023]
    """
    
    all_years = set()
    for village in village_list:
        all_years.update(village.student.keys())
    
    years_list = sorted(all_years)
    if len(years_list) < 2:
        return []
    
    # Calculate total students for each year
    total_by_year = {}
    for year in years_list:
        total = sum(village.student.get(year, 0) for village in village_list)
        total_by_year[year] = total
    
    # Calculate changes between consecutive years
    year_changes = {}
    for i in range(1, len(years_list)):
        current_year = years_list[i]
        prev_year = years_list[i-1]
        change = total_by_year[current_year] - total_by_year[prev_year]
        year_changes[current_year] = change
    
    # Sort years by change (ascending)
    sorted_years = sorted(year_changes.keys(), key=lambda y: year_changes[y])
    
    return sorted_years
    
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
    
    filtered_villages = [v for v in village_list if v.get_rank() == rank and year in v.student]
    
    if not filtered_villages:
        return []
    
    # Calculate average student count for the year across all villages
    total_students = sum(v.student.get(year, 0) for v in village_list if year in v.student)
    total_villages_with_data = sum(1 for v in village_list if year in v.student)
    
    if total_villages_with_data == 0:
        return []
    
    avg_students = total_students / total_villages_with_data
    
    # Filter villages with student count greater than average
    above_avg_villages = [v for v in filtered_villages if v.student[year] > avg_students]
    
    # Sort by student count and extract names
    sorted_villages = sorted(above_avg_villages, key=lambda v: v.student[year])
    village_names = [v.name for v in sorted_villages]
    
    return village_names
    
def sorted_town_by_avg_student(village_list):
    
    """
    Hàm trả về một danh sách các quận (town) được xắp sếp tăng dần
    theo số lượng thí sinh thi cấp 3 trung bình của các phường trong quận đó.
    Giá trị trung bình được tính trên tất cả các năm cho tất cả các phường thuộc quận đó
    
    output: ['Ba Đình','Cầu Giấy','Hoàn Kiếm','Long Biên','Tây Hồ']
    """
    # Group villages by town
    towns = {}
    for village in village_list:
        if village.town not in towns:
            towns[village.town] = []
        towns[village.town].append(village)
    
    # Calculate average student count for each town
    town_avg = {}
    for town, town_villages in towns.items():
        total_students = 0
        total_data_points = 0
        
        for village in town_villages:
            for year, count in village.student.items():
                total_students += count
                total_data_points += 1
        
        if total_data_points > 0:
            town_avg[town] = total_students / total_data_points
        else:
            town_avg[town] = 0
    
    # Sort towns by average student count
    sorted_towns = sorted(town_avg.keys(), key=lambda t: town_avg[t])
    
    return sorted_towns
    