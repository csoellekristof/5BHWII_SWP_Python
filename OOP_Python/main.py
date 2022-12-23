from enum import Enum


class Gender(Enum):
    MALE = 1
    FEMALE = 2

class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Mitarbeiter(Person):
    def __init__(self, name, gender):
        super.__init__(self, name, gender)


class Gruppenleiter(Mitarbeiter):
    def __init__(self,name,gender):
        super.__init__(self, name, gender)


class Firma:
    def __init__(self,name):
        self.name = name
        self.abteilungen = []

    def getBiggestDepartment(self):
        anzMitarbeiter = 0
        abteilung = None
        for a in self.abteilungen:
            nonlocal anzMitarbeiter
            nonlocal abteilung
            if a.getAnzMitarbeiter > anzMitarbeiter:
                anzMitarbeiter = a.getAnzMitarbeiter
                abteilung = a
        return a.name

    def getMaleFemaleRatio(self):
        ratio = {"Male": 0, "Female": 0}
        all = 0
        males = 0
        females = 0

        for a in self.abteilungen:
            nonlocal all
            nonlocal males
            nonlocal females
            for m in a.mitarbeiter:
                if m.gender == Gender.MALE:








class Abteilung:
    def __init__(self, name, gruppenleiter):
        self.name = name
        self.gruppenleiter = [gruppenleiter]
        self.mitarbeiter = []

    def getAnzMitarbeiter(self):
        return len(self.mitarbeiter)





p1 = Person("Wolfgang", Gender.MALE,Abteilung.PRODUKTION)

