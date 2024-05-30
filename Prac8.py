################## CLASS AND OBJECT ####################
# class Student:  #class creation
#     name = "karan kumar"
# s1 = Student()  #object creation
# print(s1.name)

######### CONSTRUCTOR (__init__ function) ###########
# class Cars:
#     def __init__(self, brand):  #self is always the 1st parameter
#         self.car = brand 
#         print("adding to database....")

# c1 = Cars("BMW")
# print(c1.car)
# 'self' parameter is the reference to the current instance of the class and is used to access variables belonging to that class

# class Student:
#     # default constructor(one parameter)
#     def __init__(self):
#         pass

#     # parameterized constructor
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("Adding new student to the database....")
        
# s1 = Student("Rishi", 98)
# print(s1.name, s1.marks)

# s2 = Student("Dimple", 86)
# print(s2.name, s2.marks)

############### CLASS AND OBJECT ATTRIBUTES ###############
# Class attributes are common for every object
# Instance attributes are different for every object
# obj attribute > class attribute

# class Student:
#     cname = "GITAM UNIVERSITY"
#     name = "Anirudh"  #class attribute

#     def __init__(self, name, marks):
#         self.name = name  #obj attribute
#         self.marks = marks
#         print("adding to the database")

# s1 = Student("Karan", 98)
# print(s1.name, s1.marks)
 
################ METHODS (functions that belong to objects) #################
# class Student:
#     cname = "GITAM UNIVERSITY"

#     def __init__(self, name, marks):
#         self.name = name  
#         self.marks = marks

#     def hello(self):
#         print("welcome student", self.name)

#     def get_marks(self):
#         return self.marks

# s1 = Student("Karan", 98)
# s1.hello()
# print(s1.get_marks())

############# Create a student class that takes name and marks of 3 subjects as arguments in a constructor. Then create a method to print the average. ########################
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for i in self.marks:
#             sum += i
#         print("Average is:", sum/3)

# s1 = Student("Charan", [97, 82, 90])
# s1.get_avg()

############## STATIC METHODS (methods which don't use self parameter) ################
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     @staticmethod  #decorator (takes a func changes its behaviour and gives output)
#     def hello():
#         print("hellooo")

#     def get_avg(self):
#         sum = 0
#         for i in self.marks:
#             sum += i
#         print("Average is:", sum/3)

# s1 = Student("Charan", [97, 82, 90])
# s1.get_avg()
# s1.hello()

# ABSTRACTION : Hiding the implementation details of a class and only shows the essential features to the user
# ENCAPSULATION : Wrapping data and functions into a single unit (object)

############## ABSTRACTION ##################
# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.clutch = True  #these details are not shown during execution 
#         self.acc = True
#         print("car started......")

# c1 = Car()
# c1.start()

########## Create account class with 2 attributes - balance and acc no. Create methods for withdraw, deposit and checking balance ###################
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.ano = acc
        
    def withdraw(self, amount):
        self.balance -= amount
        print("Amount withdrawn:",amount)
        print("current balance:", self.get_bal())
        
    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)
        print("current balance:", self.get_bal())
        
    def get_bal(self):
        return self.balance
    
a1 = Account(10000, 123)
a1.withdraw(1500)
a1.deposit(3000)



































