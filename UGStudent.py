import re
class UGStudent():
    __StudentId=0
    __StudentName=""
    __Gender=""
    __Year=""
    __CLassId=""
    def Get_StudentId(self):
        return self.__StudentId
    
    def studentDetails(self, StudentId):
        with open("Student.txt", "r") as file:
            lines = file.readlines()
        
                
        staff_found = False
        
        for line in lines:
            details = line.strip().split(',')
            if len(details) == 6:
                id = details[0]
                name = details[1]
                Gender = details[2]
                Year = details[3]
                Class_id = details[4]
                student_type=details[5].strip().upper()
                
                if id == str(StudentId):
                    if student_type == "UG":
                        staff_found = True
                        print(f"id : {id}")
                        print(f"name : {name}")
                        print(f"Gender : {Gender}")
                        print(f"Year : {Year}")
                        print(f"Class id : {Class_id}")
                        print(f"Type : {student_type}")
                        break
        
        if not staff_found:
            print("Not Found")

    def PayFees(self, fees, StudentId):
        total = 2000
        student_found = False

        with open("Student.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            details = line.strip().split(",")
            if len(details) == 6:
                id = details[0]
                name = details[1]
                Gender = details[2]
                Year = details[3]
                Class_id = details[4]
                student_type=details[5].strip().upper()
                if id == str(StudentId):
                    if student_type == "UG":
                        student_found = True
                        print(f"Name => {name}")
                        break
            else:
                print("Try again")
                return

        if not student_found:
            print(f"Student with ID {StudentId} not found")
            return

        total -= fees
        if total <= 0:
            with open("PayFees.txt", "a") as file:
                file.write(f"{StudentId},Yes\n")
            print("Fees paid in full")
        else:
            with open("PayFees.txt", "a") as file:
                file.write(f"{StudentId},No({total})\n")
            print(f"You should pay ${total}")
         
    def IsPresent(self, StudentId):
        with open("Student.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            details = line.strip().split(",")
            if len(details) == 6:
                id = details[0]
                name = details[1]
                Gender = details[2]
                Year = details[3]
                Class_id = details[4]
                student_type=details[5].strip().upper()
                if id == str(StudentId):
                    if student_type == "UG":
                        print("Present")
                        return

        print("Absent") 
        
x = UGStudent()
x.PayFees(900,4)

                