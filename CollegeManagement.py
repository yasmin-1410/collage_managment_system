class CollageManagment ():
    __CollageName =""
    __City =""
    __ContactNumber =""
    # def __init__ (self,CollageName,City,ContactNumber):
    #     self.__CollageName=CollageName
    #     self.__City=City
    #     self.__ContactNumber=ContactNumber
    
    def Open(self, CollegeName, Time):
        with open("OpenCollage.txt", "r") as file:
            lines = file.readlines()
        
        college_found = False
        
        for line in lines:
            details = line.strip().split(",")
            if len(details) == 5:
                id = details[0]
                name = details[1]
                contact = details[2]
                start = int(details[3])
                end = int(details[4])
                
                if name == CollegeName:
                    if start <= Time <= end:
                        print(f"{name} is opened")
                        college_found = True
                        break
        
        if not college_found:
            print(f"{CollegeName} is closed")
    
    def CollegeDetails(self,CollegeName):
        with open("CollageMangment.txt", "r") as file:
            lines = file.readlines()
        
        college_found = False
        
        for line in lines:
            details = line.strip().split(",")
            if len(details) == 3:
                id = details[0]
                name = details[1]
                contact = details[2]
                if name == CollegeName:
                    print(f"id : {id}")
                    print(f"name : {name}")
                    print(f"contact : {contact}")
                    college_found=True
                    break
        if not college_found:
            print("Not Found")

x = CollageManagment()
x.CollegeDetails("Cairo University")



         
