import re
from abc import ABC, abstractmethod
class Hostel(ABC):
    __StudentId=0
    __BlockNumber=0
    __RoomNumber=0
    
    @abstractmethod
    def HostelDetails(slef,StudentId):
        pass
    
    @abstractmethod
    def CheckIn(self,StudentId):
        pass
    
    @abstractmethod
    def CheckIn(self,StudentId):
        pass
    
    
    