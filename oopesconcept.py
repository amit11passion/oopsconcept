#Base class one
class Dad:
    def __init__(self):
        print("Dad class")
    def dad_method(self):
        print("inside the Dad method")
#parent class method
    def careers(self):
        print("I want my child to be a doctor")


#Base class two
class Mom:
    def __init__(self):
        print("mom class")
    def Mom_method(self):
        print("inside the mom method")
#child class merhods
    def careers(self):
            print("I want my child to be a engineers")


#Child class that inherit the parent Dad and Mom
#so concept of inheritance and multiple inheritance
class Child(Mom,Dad):
    def __init__(self):
        print("child class")
    def Child_method(self):
        print("inside the child method")
#overridden method in the child class from the parent
    def careers(self):
        print("i want to be a filmmaker")

d=Dad();
d.careers()
#Dad class
#I want my child to be a doctor
m=Mom()
m.careers()
#mom class
#I want my child to be a engineers
c=Child()
c.careers()
#child class
#i want to be a filmmaker
