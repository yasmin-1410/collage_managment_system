from enum import Enum

class Department(Enum):
    CS=1
    IT=2
    IS=3
    AI=4
    
class Classroom():
    __ClassId=0
    __Section=""
    __DepartmentId=0
    
    def ClassroomDetails(self,ClassId):
        with open("ClassRoom.txt","r") as file :
            lines = file.readlines()
        found = False
        for line in lines:
            details = line.strip().split(",")
            if len(details) == 3:
                id = details[0]
                Section = details[1]
                DepartmentId = details[2]
                if id == str(ClassId):
                    department_name = Department(int(DepartmentId)).name
                    print(f"id : {id}")
                    print(f"Section : {Section}")
                    print(f"Department : {department_name}")
                    found = True
                    break
        if not found:
            print("Not Found")
            
    def IsOccupied(self,ClassId):
        with open("ClassRoom.txt","r") as file :
            lines = file.readlines()
        found = False
        for line in lines:
            details = line.strip().split(",")
            if len(details) == 3:
                id = details[0]
                Section = details[1]
                DepartmentId = details[2]
                if id == str(ClassId):
                    print("this class room is occupied")
                    found = True
                    break
        if not found:
            print("this class room is not occupied")
