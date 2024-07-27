from CollegeManagement import CollageManagment
from Department import Department
from Student import Student
from staff import Staff
from NonTeachingStaff import NonTeachingStaff
from TeachingStaff import TeachingStaff
from PGStudent import PGStudent
from UGStudent import UGStudent
from GirlsHostel import GirlsHostel
from BoysHostel import BoysHostel
from Classroom import Classroom
from Canteen import Canteen
from Library import Library
from Bus import Bus
from Hostel import Hostel
from Parking import Parking
from Auditorium import Auditorium

def main_menu():
    while True:
        print("""
        ########################################
        # Welcome to College Management System #
        ########################################
        Please Choose:
        1. College Management
        2. Department
        3. Student
        4. Staff
        5. Classroom
        6. Library
        7. Bus
        8. Hostel
        9. Auditorium
        10. Exit
        """)
        
        x = int(input("Enter Number: "))
        
        if x == 1:
            collage_management_menu()
        elif x == 2:
            department_menu()
        elif x == 3:
            student_menu()
        elif x == 4:
            staff_menu()
        elif x == 5:
            classroom_menu()
        elif x == 6:
            library_menu()
        elif x == 7:
            bus_menu()
        elif x == 8:
            hostel_menu()
        elif x == 9:
            auditorium_menu()
        elif x == 10:
            break
        else:
            print("Invalid choice, please select a valid option.")

def collage_management_menu():
    collage = CollageManagment()
    while True:
        print("""
        #################################
        # Welcome to College Management #
        ################################# 
        Please Choose:
        1. Open -> Check if the college is open
        2. College Details
        3. Exit
        """)
        y = int(input("Enter Number: "))
        
        if y == 1:
            while True:
                name = input("Enter the Name of college: ")
                time = int(input("Enter time from [0 -> 23]: "))
                collage.Open(name, time)
                
                again = input("Do you want to check another college? (Y/N): ").strip().upper()
                if again != 'Y':
                    break
        
        elif y == 2:
            while True:
                name = input("Enter the Name of college: ")
                collage.CollegeDetails(name)
                
                again = input("Do you want to check another college? (Y/N): ").strip().upper()
                if again != 'Y':
                    break
        
        elif y == 3:
            break
        
        else:
            print("Invalid choice, please select 1, 2, or 3.")

def department_menu():
    dep = Department()
    while True:
        print("""
        #################################
        # Welcome to College Department #
        #################################
        Please Choose:
        1. Department Details
        2. Exit
        """)
        y = int(input("Enter Number: "))
        
        if y == 1:
            dep.DepartmentDetails()
        
        elif y == 2:
            break
        
        else:
            print("Invalid choice, please select 1 or 2.")

def student_menu():
    while True:
        print("""
        #################################
        # Welcome to College's Students #
        ################################# 
        Please Choose:
        1. UG Students
        2. PG Students
        3. Exit
        """)
        y = int(input("Enter Number: "))
        
        if y == 1:
            ug_student_menu()
        
        elif y == 2:
            pg_student_menu()
        
        elif y == 3:
            break
        
        else:
            print("Invalid choice, please select 1, 2, or 3.")

def ug_student_menu():
    while True:
        print("""
        ####################################
        # Welcome to College's UG Students #
        #################################### 
        Please Choose:
        1. Student Details
        2. Pay Fees
        3. Check Attendance
        4. Exit
        """)
        z = int(input("Enter Number: "))
        stu = UGStudent()
        
        if z == 1:
            while True:
                id = int(input("Enter ID: "))
                stu.studentDetails(id)
                
                again = input("Do you want to check another student? (Y/N): ").strip().upper()
                if again != 'Y':
                    break
        
        elif z == 2:
            while True:
                fees = int(input("Enter fees: "))
                id = int(input("Enter ID: "))
                stu.PayFees(fees, id)
                
                again = input("Do you want to pay for another student? (Y/N): ").strip().upper()
                if again != 'Y':
                    break
        
        elif z == 3:
            while True:
                id = int(input("Enter ID: "))
                stu.IsPresent(id)
                
                again = input("Do you want to check attendance for another student? (Y/N): ").strip().upper()
                if again != 'Y':
                    break
        
        elif z == 4:
            break
        
        else:
            print("Invalid choice, please select 1, 2, 3, or 4.")

def pg_student_menu():
    while True:
        print("""
        ####################################
        # Welcome to College's PG Students #
        #################################### 
        Please Choose:
        1. Student Details
        2. Pay Fees
        3. Check Attendance
        4. Exit
        """)
        z = int(input("Enter Number: "))
        stu = PGStudent()
        
        if z == 1:
            while True:
                id = int(input("Enter ID: "))
                stu.studentDetails(id)
                
                again = input("Do you want to check another student? (Y/N): ").strip().upper()
                if again != 'Y':
                    break
        
        elif z == 2:
            while True:
                fees = int(input("Enter fees: "))
                id = int(input("Enter ID: "))
                stu.PayFees(fees, id)
                
                again = input("Do you want to pay for another student? (Y/N): ").strip().upper()
                if again != 'Y':
                    break
        
        elif z == 3:
            while True:
                id = int(input("Enter ID: "))
                stu.IsPresent(id)
                
                again = input("Do you want to check attendance for another student? (Y/N): ").strip().upper()
                if again != 'Y':
                    break
        
        elif z == 4:
            break
        
        else:
            print("Invalid choice, please select 1, 2, 3, or 4.")

def staff_menu():
    while True:
        print("""
        ##############################
        # Welcome to College's Staff #
        ############################## 
        Please Choose:
        1. Teaching
        2. Non-Teaching
        3. Exit
        """)
        y = int(input("Enter Number: "))
        
        if y == 1:
            teaching_staff_menu()
        
        elif y == 2:
            non_teaching_staff_menu()
        
        elif y == 3:
            break
        
        else:
            print("Invalid choice, please select 1, 2, or 3.")

def teaching_staff_menu():
    while True:
        print("""
        #######################################
        # Welcome to College's Teaching Staff #
        ####################################### 
        Please Choose:
        1. Staff Details
        2. Exit
        """)
        z = int(input("Enter Number: "))
        staff = TeachingStaff()
        
        if z == 1:
            id = int(input("Enter ID: "))
            staff.StaffDetails(id)
            
            again = input("Do you want to check another staff? (Y/N): ").strip().upper()
            if again != 'Y':
                break
        
        elif z == 2:
            break
        
        else:
            print("Invalid choice, please select 1 or 2.")

def non_teaching_staff_menu():
    while True:
        print("""
        ###########################################
        # Welcome to College's Non-Teaching Staff #
        ###########################################
        Please Choose:
        1. Staff Details
        2. Exit
        """)
        z = int(input("Enter Number: "))
        staff = NonTeachingStaff()
        
        if z == 1:
            id = int(input("Enter ID: "))
            staff.StaffDetails(id)
            
            again = input("Do you want to check another staff? (Y/N): ").strip().upper()
            if again != 'Y':
                break
        
        elif z == 2:
            break
        
        else:
            print("Invalid choice, please select 1 or 2.")

def classroom_menu():
    while True:
        print("""
        ###################################
        # Welcome to College's Class Room #
        ################################### 
        Please Choose:
        1. Classroom Details
        2. Check if Occupied
        3. Exit
        """)
        z = int(input("Enter Number: "))
        room = Classroom()
        
        if z == 1:
            id = int(input("Enter ID: "))
            room.ClassRoomDetails(id)
            
            again = input("Do you want to check another classroom? (Y/N): ").strip().upper()
            if again != 'Y':
                break
        
        elif z == 2:
            id = int(input("Enter ID: "))
            room.IsOccupied(id)
            
            again = input("Do you want to check another classroom? (Y/N): ").strip().upper()
            if again != 'Y':
                break
        
        elif z == 3:
            break
        
        else:
            print("Invalid choice, please select 1, 2, or 3.")

def library_menu():
    while True:
        print("""
        ################################
        # Welcome to College's Library #
        ################################ 
        Please Choose:
        1. Library Details
        2. Exit
        """)
        y = int(input("Enter Number: "))
        lib = Library()
        
        if y == 1:
            lib.LibraryDetails()
        
        elif y == 2:
            break
        
        else:
            print("Invalid choice, please select 1 or 2.")

def bus_menu():
    while True:
        print("""
        ############################
        # Welcome to College's Bus #
        ############################ 
        Please Choose:
        1. Bus Details
        2. Exit
        """)
        y = int(input("Enter Number: "))
        bus = Bus()
        
        if y == 1:
            bus.BusDetails()
        
        elif y == 2:
            break
        
        else:
            print("Invalid choice, please select 1 or 2.")

def hostel_menu():
    while True:
        print("""
        ###############################
        # Welcome to College's Hostel #
        ###############################
        Please Choose:
        1. Boys Hostel
        2. Girls Hostel
        3. Exit
        """)
        y = int(input("Enter Number: "))
        
        if y == 1:
            boys_hostel_menu()
        
        elif y == 2:
            girls_hostel_menu()
        
        elif y == 3:
            break
        
        else:
            print("Invalid choice, please select 1, 2, or 3.")

def boys_hostel_menu():
    while True:
        print("""
        ##########################
        # Welcome to Boys Hostel #
        ########################## 
        Please Choose:
        1. Hostel Details
        2. Exit
        """)
        z = int(input("Enter Number: "))
        hostel = BoysHostel()
        
        if z == 1:
            id = int(input("Enter ID: "))
            hostel.HostelDetails(id)
            
            again = input("Do you want to check another hostel? (Y/N): ").strip().upper()
            if again != 'Y':
                break
        
        elif z == 2:
            break
        
        else:
            print("Invalid choice, please select 1 or 2.")

def girls_hostel_menu():
    while True:
        print("""
        ###########################
        # Welcome to Girls Hostel #
        ########################### 
        Please Choose:
        1. Hostel Details
        2. Exit
        """)
        z = int(input("Enter Number: "))
        hostel = GirlsHostel()
        
        if z == 1:
            id = int(input("Enter ID: "))
            hostel.HostelDetails(id)
            
            again = input("Do you want to check another hostel? (Y/N): ").strip().upper()
            if again != 'Y':
                break
        
        elif z == 2:
            break
        
        else:
            print("Invalid choice, please select 1 or 2.")

def auditorium_menu():
    while True:
        print("""
        ###################################
        # Welcome to College's Auditorium #
        ################################### 
        Please Choose:
        1. Auditorium Details
        2. Exit
        """)
        y = int(input("Enter Number: "))
        aud = Auditorium()
        
        if y == 1:
            aud.AuditoriumDetails()
        
        elif y == 2:
            break
        
        else:
            print("Invalid choice, please select 1 or 2.")

if __name__ == "__main__":
    main_menu()
