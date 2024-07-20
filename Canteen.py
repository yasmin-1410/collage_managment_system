from Student import Student
student = Student()
class Canteen ():
    __InChargeId=0
    __ItemsList=[]
    __AvailableList=[]
    
    def Set_InChargeId(self ,InChargeId):
        self.__InChargeId = InChargeId
        
    def Set_ItemsList(self, ItemsList):
        while len(self.__ItemsList) < self.__InChargeId:
            self.__ItemsList.append("")
        self.__ItemsList[self.__InChargeId - 1] = ItemsList

    def Set_AvailableList(self, AvailableList):
        while len(self.__AvailableList) < self.__InChargeId:
            self.__AvailableList.append("")
        self.__AvailableList[self.__InChargeId - 1] = AvailableList
    def ShowItems():
        with open("Canteen.txt","r") as file:
            lines = file.readlines()
        for line in lines:
            return line.strip() 
         
    def SaveToFile(self):
        with open("Canteen.txt", "a") as file:
            file.write(f"{self.__InChargeId},{self.__ItemsList[self.__InChargeId - 1]},{self.__AvailableList[self.__InChargeId - 1]}\n")
        print("Stored Successfully") 

    def Buy(self, StudentId, item, quantity):
        student_found = False
        with open("Student.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                details = line.strip().split(",")
                if len(details) == 5:
                    student_id = details[0]
                    if student_id == str(StudentId):
                        student_found = True
                        break
            if not student_found:
                print("Invalid Student ID")
                return
        item_found = False
        with open("Canteen.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                details = line.strip().split(",")
                if len(details) == 3:
                    in_charge_id = details[0]
                    item_name = details[1]
                    available = details[2]
                    if item_name == item and available.lower() == "yes":
                        item_found = True
                        with open("Payments.txt","a") as file:
                            file.write(f"{StudentId},{in_charge_id},{item_name},{quantity} \n")
                        break
            if not item_found:
                print("Not found")
                return

        print(f"Student {StudentId} bought {quantity} {item}")
y = Canteen()
y.Buy(1,"banana",2)
             
        
    