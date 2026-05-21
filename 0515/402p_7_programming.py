class Person():
    def __init__(self, name,
                 mobile=None, office=None, email=None):
        self.name = name
        self.mobile = mobile
        self.office = office
        self.email = email

    def setMobile(self, number):
        self.mobile = number

    def setOffice(self, number):
        self.office = number

    def setEmail(self, address):
        self.email = address
    def __str__(self):
        s = ''
        s += self.name + '\n'
        s += "office phone:"+self.office + '\n'
        s += "email address:"+self.email + '\n'
        return s

class PhoneBook():
    def __init__(self):        
        self.contacts = {}

    def add(self, name, mobile=None, office=None,
            email=None):
        p = Person(name, mobile, office, email)
        self.contacts[name] = p
    def __str__(self):
        s = ''
        for p in sorted(self.contacts):
            s += str(self.contacts[p]) + '\n'
        return s

obj = PhoneBook()
obj.add("Kim", office="1234567", email="kim@company.com")
obj.add("Park", office="2345678", email="park@company.com")
print(obj)