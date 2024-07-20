import re
from abc import ABC, abstractmethod
class Staff(ABC):
    __StaffId=0
    __StaffName=""
    __DepartmentId=0
    __Salary=0.0
    
    @abstractmethod
    def Set_StaffId(self,StaffId):
        pass
    
    @abstractmethod     
    def Set_StaffName(self,StaffName):
        pass
    
    @abstractmethod    
    def Set_DepartmentId(self,DepartmentId):
        pass
    
    @abstractmethod   
    def Set_Salary(self,Salary):
        pass
    
    @abstractmethod
    def StaffDetails(self,StaffId):
        pass
        
        
        
        
    