#Employee Class example

class Employee:
    'Common base class for all employees'
    empCount=0
    
    def __init__(self,name,salary):
        self.name=name
        self.salary =salary
        Employee.empCount +=1
    
    def displayCount(self):
        print("Total Employee %d"% Employee.empCount)
        
    def displayEmployee(self):
        print("Name : ",self.name,",Salary: ",self.salary)

#Creating Instances Objects

emp1 =Employee("Saurav",2000)
emp2 = Employee("Pussy",1200)

emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)
#can create atrributes of classes and objects at any time
emp1.age=7
emp1.age=8

print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)
