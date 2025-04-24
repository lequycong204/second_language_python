from Student import Student
import csv

def read_student_from_file(studentFile):
    """
    Hàm đọc tệp dữ liệu sinh viên. Hàm này thực hiện đọc dữ liệu của các sinh viên từ 
    tệp studentFile, và tạo ra các đối tượng sinh viên tương ứng và lưu vào 1 danh sách,
    sau khi kết thúc việc đọc dữ liệu, hàm này trả lại danh sách sinh viên đã tạo được.
    
    dữ liệu trong tệp studentFile được lưu dưới dạng csv,
    dòng đầu tiên là tên các thuộc tính của sinh viên: name,sid,department
    các dòng tiếp theo, mỗi dòng chứa thông tin của 1 sinh viên, mỗi thông tin cách nhau bởi 1 dấu phẩy ,
    Ví dụ:
    name,sid,department
    Nguyễn Minh Đức,20001153,Physics
    Lê Minh Đức,19003301,Chemistry
    Phạm Minh Đức,18006360,Chemistry
    """
    students = []
    with open(studentFile, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            students.append(Student(row['name'], int(row['sid']), row['department']))
    return students
    
def read_grade_from_file(gradeFile, student_list):
    
    """
    Hàm thực hiện việc đọc file điểm thi của mỗi sinh viên để bổ sung thêm thông tin vào thuộc tính
    grade của mỗi Student trong student_list,
    Nhiệm vụ của hàm này là đọc dữ liệu điểm của sinh viên, thêm điểm vào từ điển điểm grade của sinh viên đó
    Chú ý là việc thêm điểm grade vào theo đúng mã sinh viên sid của sinh viên đó
    
    gradeFile chứa thông tin về điểm của các sinh viên được lưu dưới dạng csv.
    dòng đầu tiên là tên các thuộc tính của dữ liệu: sid,CS,CV,DSA,MAT,ML (mã sinh viên và mã các môn học)
    dữ liệu điểm của mỗi sinh viên lưu trên 1 dòng gồm mã sinh viên và điểm của sinh viên đó với từng môn học.
    
    Ví dụ về file gradeFile
    
    sid,CS,CV,DSA,MAT,ML
    18000144,81,29,85,91,96
    18006360,71,64,38,32,32
    19003301,88,33,70,41,87
    19003563,64,46,79,85,52
    
    
    """
    sid_map = {s.sid: s for s in student_list}	 	  	      	   	      	    	 	   	 	
    with open(gradeFile, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            sid = int(row['sid'])
            if sid in sid_map:
                for subject in row:
                    if subject != 'sid':
                        sid_map[sid].grade[subject] = int(row[subject])
    
    
def get_best_student_avg_grade(student_list):
    """
    Hàm thực hiện trả về tên 2 sinh viên có điểm trung bình thấp nhất và cao nhất.
    Ouput: (Nguyễn Văn A, Nguyễn Văn B)
    """
    if not student_list:
        return None
    sorted_students = sorted(student_list, key=lambda s: s.get_avg_grade())
    return (sorted_students[0].name, sorted_students[-1].name)

    
def get_best_student_by_year(student_list, year, class_id):
    """
    year: cho biết cần tìm những sinh viên đang học năm thứ mấy.
    Hàm trả về sinh viên có điểm môn class_id cao nhất trong số sinh viên cùng khóa
    Ví dụ 
    input: year = 3, class_id = 'CS' 
    => tìm ra sinh viên có điểm môn 'CS' cao nhất trong số các sinh viên năm 3.
    output: {name:Trần Hải Anh, mssv:20000848, department:Biology}
    """
    filtered = [s for s in student_list if s.get_year() == year and class_id in s.grade]
    if not filtered:
        return None
    best = max(filtered, key=lambda s: s.grade[class_id])
    
    
    
    return f'{{name:{best.name}, sid:{best.sid}, department:{best.department}}}'

    
def sorted_department_by_avg_student_grade(student_list):
    
    """
    Hàm trả về một danh sách các khoa được sắp xếp theo thứ tự tăng dần điểm thi trung bình
    của các sinh viên thuộc khoa đó.
    """
    dep_grades = {}	 	  	      	   	      	    	 	   	 	
    for s in student_list:
        if s.department not in dep_grades:
            dep_grades[s.department] = []
        dep_grades[s.department].append(s.get_avg_grade())
    avg_by_dep = [(dep, sum(grades)/len(grades)) for dep, grades in dep_grades.items()]
    return [dep for dep, _ in sorted(avg_by_dep, key=lambda x: x[1])]

    