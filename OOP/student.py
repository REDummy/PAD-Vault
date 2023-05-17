class Student:
    def __init__(self, nama="", uts=0, uas=0):
        self._name = nama
        self._midterm = uts
        self._final = uas
        
    def setName(self, nama):
        self._name = nama
    
    def setMidterm(self, uts):
        self._midterm = uts
    
    def setFinal(self, uas):
         self._final = uas 
    
    def getName(self):
         return self._name
        
    def __str__(self):
        return self._name + "\t" + self.calcSemGrade()


class LGstudent(Student):
    
    def calcSemGrade(self):
        average = (self._midterm + self._final) / 2
        average = round(average)
        if average >= 80:
            return "A"
        elif average >= 70:
             return "B"
        elif average >= 56:
             return "C"
        elif average >= 50:
             return "D"
        else:
             return "E"

class PFstudent(Student):
    
    def calcSemGrade(self):
        average = round((self._midterm + self._final) / 2)
        if average >= 56:
            return "Lulus"
        else:
            return "Gagal"
        