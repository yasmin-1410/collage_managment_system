class Bus():
    
    __BusId=0
    __BusNumber=0
    __DriverName=""
    __TotalSeats=0
    
    def Set_BusId(self,BusId):
        BusId=self.__BusId

    def Set_BusNumber(self,BusNumber):
        BusNumber=self.__BusNumber

    def Set_DriverName(self,DriverName):
        DriverName=self.__DriverName

    def Set_TotalSeats(self,TotalSeats):
        TotalSeats=self.__TotalSeats
        
    def BusDitails(self,BusId):
        with open("Bus.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                details = line.strip().split(",")
                if len(details) == 4:
                    self.__BusId = details[0]
                    self.__BusNumber = details[1]
                    self.__DriverName = details[2]
                    self.__TotalSeats = details[3]
                if self.__BusId == str(BusId):
                    print(f"Bus id : {self.__BusId}")
                    print(f"Bus Number : {self.__BusNumber}")
                    print(f"Driver Name : {self.__DriverName}")
                    print(f"Total Seats : {self.__TotalSeats}")
    
    def SeatsAvailability(self,BusId):
        with open("Bus.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                details = line.strip().split(",")
                if len(details) == 4:
                    self.__BusId = details[0]
                    self.__BusNumber = details[1]
                    self.__DriverName = details[2]
                    self.__TotalSeats = details[3]
            if self.__BusId == str(BusId):
                print(f"Bus id : {self.__BusId}")
                print(f"Total Seats : {self.__TotalSeats}")
            else:
                print("Not Available")           
                    