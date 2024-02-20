

class Person:

    def __init__(self,fname,lname,email) :
        self.fname=fname
        self.lname = lname
        self.email = email
    
    def show(self):
        print("Fname : ",self.fname)
        print("Lname : ",self.lname)
        print("Email : ",self.email)
    

p = Person("Chintan","Chovatiya","chintan@gmail.com")
p.show()
