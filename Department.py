from enum import Enum

class DepartmentEnum(Enum):
    CS = 1
    IT = 2
    IS = 3
    AI = 4

class Department:
    DepartmentId = 0
    DepartmentName = ""
    HODName = ""
    TotalStudents = 0
    TotalStaff = 0
    
    def DepartmentDetails(self):
        with open("Department.txt", "r") as file:
            lines = file.readlines()
        
        for line in lines:
            details = line.strip().split(",")
            if len(details) == 5:
                department_id = details[0]
                department_name_id = int(details[1])
                head_of_department = details[2]
                total_students = details[3]
                total_staff = details[4]
                
                department_name = DepartmentEnum(department_name_id).name
                
                print(f"Department Id : {department_id}")
                print(f"Department Name : {department_name}")
                print(f"Head of Department : {head_of_department}")
                print(f"Total Students : {total_students}")
                print(f"Total Staff : {total_staff}")
                print()
            else:
                print("Invalid Department.txt format.")
                break


        