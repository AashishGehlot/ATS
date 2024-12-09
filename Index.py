class Candidate:
    def __init__(self, FirstName, MiddleName, LastName, Location, PhoneNo, EmailID, PositionType, Budget, VisaStatus):
        self.FirstName= FirstName
        self.MiddleName= MiddleName
        self.LastName= LastName 
        self.Location = Location
        self.PhoneNo= PhoneNo
        self.EmailID= EmailID
        self.PositionType= PositionType
        self.Budget= Budget
        self.VisaStatus= VisaStatus
        
    def getFName():
        return FirstName
    
    def setFname(FirstName):
        self.FirstName = FirstName
        
        
        
resource1 = Candidate("Aashish", "Gehlot", "NoMiddle", "Bengaluru", "8287625111", "Aashish.g@techvistainc.com", "Full Time", 100, "EAD")

print(resource1)
    
        
        
        
        