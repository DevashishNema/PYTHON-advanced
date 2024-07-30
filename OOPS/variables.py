# instance variable
# static/class variable
# local variable

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



class student:
        
    def display(self,name,age):
       self.n1 = name
       self.n2 = age
    def show(self):
        print(self.n1,self.n2)   
        
        
obj1=student()
obj1.display("Deva",23)
obj1.show()
print(obj1.n1,obj1.n2)
