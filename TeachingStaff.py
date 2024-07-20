from staff import Staff
import re
from enum import Enum

class Department(Enum):
    CS=1
    IT=2
    IS=3
    AI=4
    
class TeachingStaff(Staff):
    
    def Set_StaffId(self,StaffId):
        self.__StaffId=StaffId
         
    def Set_StaffName(self,StaffName):
        self.__StaffName=StaffName
        
    def Set_DepartmentId(self,DepartmentId):
        self.__DepartmentId=DepartmentId
        
    def Set_Salary(self,Salary):
        self.__Salary=Salary
    
    def StaffDetails(self,StaffId):
        with open("Staff.txt", "r") as file:
            lines = file.readlines()
        
                
        staff_found = False
        
        for line in lines:
            details = line.strip().split(',')
            if len(details) == 5:
                id = details[0]
                name = details[1]
                dep_id = details[2]
                salary = details[3]
                staff_type = details[4].strip().lower()  # Convert to lower case to standardize
                
                department_name = Department(int(dep_id)).name
                
                if id == str(StaffId):
                    if staff_type == "teaching":
                        staff_found = True
                        print(f"id : {id}")
                        print(f"name : {name}")
                        print(f"department : {department_name}")
                        print(f"salary : {salary}")
                        print(f"staff type : {staff_type}")
                        break
        
        if not staff_found:
            print("Not Found")
x = TeachingStaff()
x.StaffDetails(2)