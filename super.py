


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
class student(person):
    def __init__(self,name,age,rollno,marks):
        super().__init__(name,age)
        self.rollno=rollno
        self.marks=marks
    def display1(self):    
        super().display()
        print("Roll no:",self.rollno)
        print("Marks:",self.marks)
class teacher(person):
    def __init__(self,name,age,salary,subject):
        super().__init__(name,age)
        self.salary=salary
        self.subject=subject
    def display2(self):   
        for i in range(10): 
            print("*",end="")
        print()
        super().display()
        print("Salary:",self.salary)
        print("Subject:",self.subject)  
    
        

s=student("sunny",26,2526,65)
t=teacher("bunny",28,15000,"Telugu")
s.display1()
t.display2()

