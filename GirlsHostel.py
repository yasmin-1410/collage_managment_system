from Hostel import Hostel
import re
class GirlsHostel(Hostel):
    def __init__(self):
        self.present_students = set()
        
    def Set_StudentId(self,StudentId):
        self.__StudentId=StudentId
        
    def Set_BlockNumber(self,BlockNumber):
        self.__BlockNumber=BlockNumber
        
    def Set_RoomNumber(self,RoomNumber):
        self.__RoomNumber=RoomNumber
    
    def HostelDetails(self, StudentId):
        
        with open("Student.txt", "r") as file:
            lines = file.readlines()
        
        student_found = False
        
        for line in lines:
            details = line.strip().split(",")
            if len(details) == 5:
                id = details[0]
                StudentName = details[1]
                Gender = details[2]
            
                if id == str(StudentId) and Gender.lower() == "female":
                    print(f"Student Name : {StudentName}")
                    student_found = True
                    break
        
        if not student_found:
            print("Not Found")

    def CheckIn(self,StudentId):
        
        with open("GirlsHostel.txt", "r") as file:
            lines = file.readlines()
        
        student_found = False
        
        for line in lines:
            details = line.strip().split(",")
            if len(details) == 7:
                id = details[0]
                StudentName = details[1]
                Gender = details[2]
                year = details[3]
                ClassId = details[4]
                BlockNum = details[5]
                RoomNum = details[6]
                if id == str(StudentId) and Gender.lower() == "female":
                    if id == str(StudentId) and Gender.lower() == "female":
                        self.present_students.add(str(StudentId))
                        print(f"Student with ID {StudentId} has been checked in.")
                        student_found = True
                        break
            
            if not student_found:
                print("Student not found or not eligible for the girls' hostel.")

    def CheckOut(self, StudentId):
        student_found = False
    
        with open("GirlsHostel.txt", "r") as file:
            lines = file.readlines()
    
        with open("GirlsHostel.txt", "w") as file:
            for line in lines:
                details = line.strip().split(",")
                if len(details) == 7:
                    id = details[0]
                    if id == str(StudentId):
                        student_found = True
                    else:
                        file.write(line)
    
        if student_found:
            print(f"Student with ID {StudentId} has been checked out and removed from the file.")
        else:
            print(f"Student with ID {StudentId} is already checked out or not found in the file.")
