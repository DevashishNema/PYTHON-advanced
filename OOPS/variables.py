# instance variable
# static/class variable 
# local variable





# -----------------------------------------------------------------------------------------------------------------------------

# INSTANCE VARIALE

# class student:
   
    
#     def __init__(self,name,age):
#         self.n1 = name
#         self.n2 = age
        
#     def display(self):
#         print("Name = ",self.n1)
#         print("Age = ",self.n2)
        
        
# obj1=student("Deva",21)
# obj1.display()
# obj2=student("Ashish",22)
# obj2.display()


# class student:
   
    
#     def __init__(self,name,age):
#         self.n1 = name
#         self.n2 = age
        
#     def display(self):
#         print("Name = ",self.n1)
#         print("Age = ",self.n2)
        
        
# obj1=student("Deva",21)
# obj1.display()
# print(obj1.n1)
# print(obj1.n2)




# class student:
        
#     def display(self):
#         print("Name = ",self.n1)
#         print("Age = ",self.n2)
        
        
# obj1=student()
# obj1.n1="Deva"
# obj1.n2=23
# obj1.display()



# class student:
        
#     def display(self,name,age):
#        self.n1 = name
#        self.n2 = age
#     def show(self):
#         print(self.n1,self.n2)   
        
        
# obj1=student()
# obj1.display("Deva",23)
# obj1.show()
# print(obj1.n1,obj1.n2)

# ----------------------------------------------------------------------------------------------------------------------------------------------



# STATIC/CLASS VARIABLE

class Student:
    
    # School = "SJCS"
    
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
        
        # Student.center_code = 101
        
    def display(self):
        
        Student.grade = "10th"
        
        print("name = ",self.name)
        print("roll_no = ",self.roll_no)
        # print("School = ",Student.School)
        # print("center = ",Student.center_code)
        print("grade = ",Student.grade)
        
obj=Student("Deva",62)
obj.display()
# print("School",Student.School)        



# -------------------------------------------------------------------------------------------------------


        