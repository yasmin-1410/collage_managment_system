import re
class Student():
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
        for line in lines:
            if re.match(f"{StudentId},", line):
                return line.strip()

    def PayFees(self, fees, StudentId):
        total = 1000
        student_found = False

        with open("Student.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            details = line.strip().split(",")
            if len(details) == 5:
                self.__StudentId = details[0]
                self.__StudentName = details[1]
                if self.__StudentId == str(StudentId):
                    student_found = True
                    print(f"Name => {self.__StudentName}")
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
            if len(details) == 5:
                self.__StudentId = details[0]
                if self.__StudentId == str(StudentId):
                    print("Present")
                    return

        print("Absent") 
        
x = Student()
x.IsPresent(2)

                