class Cab:
    #Constructor with 1 attributes
    def __init__(self, km):
        
        self.km = km
    
    def calculateFare(self):
        pass  # abstract method, to be implemented by subclasses

#subClasses of Cab
class Sedan(Cab):
    def calculateFare(self):
        return 2.0 * self.km

class Hatchback(Cab):
    def calculateFare(self):
        return 1.5 * self.km