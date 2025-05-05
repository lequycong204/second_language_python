class Student:
    
    """
    Lớp mô tả 1 sinh viên bao gồm các thông tin sau:
    name :(str) tên sinh viên
    sid:(int) mã số sinh viên có định dạng 2000xxxx trong đó 2 mã số đầu
    đại diện cho năm nhập học của sinh viên.
    Sinh viên năm nhất hiện có mssv bắt đầu bằng 2200xxxx
    department:(str) khoa sinh viên đang theo học.
    grade:(dict) một từ điển chứa mã môn học và điểm số tương ứng với môn học đó.
    điểm được chấm theo thang 100.
    """
    
    def __init__(self, name, sid, department):
        self.name = name
        self.sid = sid
        self.department = department
        self.grade = dict()
    
    def __str__(self):
        """
        Hàm in thông tin student sinh viên không cần làm gì hàm này.
        """
        return  '{name:%s, sid:%s, department:%s}'%(self.name, self.sid, self.department)
        
    def get_year(self):
        """
        Hàm trả về sinh viên đang theo học năm thứ mấy.
        sid bắt đầu bằng 2200 : sinh viên năm 1
        sid bắt đầu bằng 2100 : sinh viên năm 2
        ...
        sid bắt đầu bằng 1800: sinh viên năm 5
        """
        year_code = int(str(self.sid)[:2])
        return 23 - year_code
        
    def get_avg_grade(self):
        """
        Hàm trả về điểm trung bình của sinh viên
        """
        if not self.grade:
            return 0.0
        return sum(self.grade.values()) / len(self.grade)	 	  	      	   	      	    	 	   	 	
