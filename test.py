class students:
    
    def __init__(self, age, college_name, hostel_name):
        self.age = age
        self.college_name = college_name
        self.hostel_name = hostel_name
        self.menu()
    
    def goodmorning(self, name):
        print(f"HEllo good morning {name}")
        
    
    def sum(self, a):
        count = 0
        for i in a:
            count = count+i
        print(count)
        return count
    
    
    def students_info(self):
        print(f"Students info: {self.age}, {self.college_name}, {self.hostel_name}.")
    
    def menu(self):
        print("Object created successfully!!..")
    
    
a = students(age=23, college_name='CITK', hostel_name='SJ')

a.students_info()



    

