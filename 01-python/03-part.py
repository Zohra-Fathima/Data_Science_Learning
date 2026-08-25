# class student:
#     def __init__(self):#default constructor
#         print("obj is being constructed...")

#     def __init__(self,name,cgpa): #parameterized constructor
#         self.name=name
#         self.cgpa=cgpa

#     def get_cgpa(self):
#         return self.cgpa


# stu1=student("zohra",9)
# stu2=student("gori",8)
# stu3=student("kali",9)

# print(f"{stu1.name} has cgpa ={stu1.get_cgpa()}")
# print(f"{stu2.name} has cgpa ={stu2.get_cgpa()}")

#ATTRIBUTE
# class student:
#     college_name="ABC college" #class attributes
#     PI=3.1

#     def __init__(self,name,gpa):
#         self.name=name #instance attributes
#         self.gpa=gpa
#         self.PI=3.14

# stu1=student("rahul",9.0)
# print(stu1.PI)#whenever we have two attributes with same name ,instance attribute have higher preference

#METHODS
# class laptop:
#     storage_type="ssd"

#     def __init__(self,RAM,storage):
#         self.RAM=RAM
#         self.storage=storage

#     @classmethod #hover for more info
#     def get_storage_type(cls):#example of what an class method looks like
#         print(f"storage type = {cls.storage_type}")

#     def get_info(self):#example of what an instance method looks like
#         print(f"laptop has {self.RAM} RAM and {self.storage} {self.storage_type}")

#     @staticmethod
#     def cal_discount(price,discount):
#         final_price=price-(discount * price/100)
#         print(f"discounted price={final_price}")

# l1=laptop("16gb","512")
# l2=laptop("8gb","256")

# # l1.get_info()#printing instance method

# # laptop.get_storage_type()#printing class method(can also use obj)

# l1.cal_discount(40_000,10)

# #PROBLEM:-
# class product:
#     count=0

#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#         product.count += 1

#     def get_info(self): #instance method
#         print(f"the price of {self.name} is Rs.{self.price}")

#     @classmethod
#     def total_product(cls):
#         print(f"the total number of products in store is {product.count}")

#     @staticmethod #create a static method to calculate discount on each product bassed on a % parameter
#     def discount(price,discount):
#         final_price=price-(discount * price/100)
#         print(f"the final price after discount is ={final_price}")


# p1=product("laptop",90_000)
# p2=product("mobile",40_000)
# p3=product("notepad",20_000)

# # p1.get_info()#design and create an online store for products(name,price)
# # p2.get_info()
# # p3.get_info()

# # product.total_product()#track total products being created

# p1.discount(90_000,12)

#OOP PILLARS
#DATA HIDING
# class bankaccount:
#     def __init__(self,account_name,balance):
#         self.account_name=account_name
#         self.__balance=balance #private 

#     def get_balance(self): #getter
#         return self.__balance

#     def set_balance(self,new): #setter
#         self.__balance= new
  

# acc1=bankaccount("zohra",80_000)

# acc1.set_balance(200_000)
# print(f"the user {acc1.account_name} has the balance {acc1.get_balance()}")

#INHERITANCE
# class Employee:
#     start="10AM"
#     end="4PM"

#     def change_time(self,end_time):
#         self.end=end_time

# class Teacher(Employee):
#     def __init__(self,subject):
#         self.subject=subject

# class Admin(Teacher):
#     def __init__(self,role):
#         self.role=role


# staff1=Admin("manager")
# print(staff1.role,staff1.start,staff1.end)

# T1=Teacher("english")
# T1.change_time("5pm")

# print(T1.subject,T1.start,T1.end )

# #MULTI LEVEL INHERITANCE
# class Employee:
#     start="10AM"
#     end="4PM"

# class Admin(Employee):
#     def __init__(self,role):
#         self.role=role

# class Accountant(Admin):
#     def __init__(self,salary,role):
#          super().__init__(role)
#          self.salary=salary

# acc1=Accountant(25_000,"CA")
# print(acc1.role,acc1.salary,acc1.start,acc1.end)


#MULTIPLE LEVEL INHERITANCE
# class Teacher:
#     def __init__(self,salary):
#         self.salary=salary


# class Student:
#     def __init__(self,gpa):
#         self.gpa=gpa

# class TA(Teacher,Student):
#     def __init__(self,gpa,salary,name):
#         super().__init__(salary)
#         Student.__init__(self,gpa)
#         self.name=name



# TA1=TA(9.0,90_000,"zohra")
# print(f"{TA1.name}'s salary is {TA1.salary} and has the gpa {TA1.gpa}")


#ABSTRACTION
# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass #pass represents null value

# class Lion(Animal):
#     def make_sound(self):
#         print("roar")


# l1=Lion()
# l1.make_sound()


#POLYMORPHISM
#function overriding:-
# class Employee:
#     def designation(self):
#         print("employee")

# class Teacher(Employee):
#      def designation(self):
#             print("teacher")

# t1=Teacher()
# t1.designation()

#duck typing
# class Teacher():
#     def get_designation(self):
#         print("teacher")

# class Accountant():
#     def get_designation(self):
#         print("Accountant")

# t1=Teacher()
# a1=Accountant()

# t1.get_designation()
# a1.get_designation()



# class Book():
#     def __init__(self,title,author,list_of_reviews):
#         self.title=title
#         self.author=author
#         self.list_of_reviews=list_of_reviews

#     def add_review(self,new):
#         self.list_of_reviews.append(new)

#     def count(self):
#         return len(self.list_of_reviews)

#     def display(self):
#         return self.list_of_reviews

# b=Book("money heist","sargo",["lockdown movie"])
# b.add_review("one of the best series")
# print(b.display())

# class Student():
#     def __init__(self,__name,__rollno,__marks):
#         self.__name=__name
#         self.__rollno=__rollno
#         self.__marks=__marks

#     def get(self):
#         return self.__name
#         return self.__rollno
#         return self._marks

#     def set(self):
#         self.__rollno=__rollno
#         self.__name=__name
#         self.__marks=__marks


# s=Student("zohra",10,90)

# s.get()
# print(s.get())