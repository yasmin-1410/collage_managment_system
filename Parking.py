class Parking ():
    __SlotId=0
    __ItemsList=[]
    __AvailableList=[]
    
    def ParkVehicle(self,SlotId,item):
        self.__SlotId=SlotId
        self.__ItemsList.append(item)
        
        while len(self.__ItemsList) < SlotId:
            self.__ItemsList.append(None)

        self.__SlotId = SlotId
        self.__ItemsList[SlotId-1] = item
        
        with open("Parking.txt","a") as file:
            try:
                file.write(f"{SlotId},{self.__ItemsList[SlotId-1]}\n")
                return "Stored Successfully"
            except IOError as e:
                return f"Erorr : {e}"

    
            
            
        
    