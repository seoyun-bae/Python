class Person:
    def __init__ (self, name, mobile="", office="", email=""):
        self.name = name
        self.mobile = mobile
        self.office = office
        self.email = email

    def __str__(self):
        return f"{self.name}, {self.mobile}, {self.office}, {self.email}"
    
    def setEmail(self, email):
        self.email = email

p1 = Person("Kim", office="1234567", email="kim@company.com")
p2 = Person("Park", office="12345678")
p2.setEmail("park@company.com")
print(p1)
print(p2)