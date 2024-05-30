########### WHILE LOOP ############
# count = 1
# while count <= 5:
#     print("hello")
#     count += 1

########### WAP to print numbers from 1 to 100 ############
# count = 1
# while count <= 100:
#     print(count)
#     count += 1
    
################ WAP to print numbers from 100 to 1 ############
# count = 100
# while count >= 1:
#     print(count)
#     count -= 1
    
############# WAP to print multiplication table of a number ############
# n = int(input("enter a number:"))
# i = 1
# while i<= 10:
#     print(n,"x",i,"=",n*i)
#     i += 1
    
########### WAP to print the elements of list using a loop ##############
# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# i = 0
# while i <= len(list)-1:
#     print(list[i])
#     i += 1

######### WAP to search for an element x in a tuple using loop ############
# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# x = int(input("enter the element to be searched:"))
# i = 0
# while i<= len(list)-1:
#     if(list[i] == x):
#         print("element found at index:",i)
#     i += 1    
    
########### BREAK STATEMENT (used to terminate the loop when encountered) #########
# i = 1
# while i <= 5:
#     print(i)
#     if (i == 3):
#         break
#     i +=1

########## CONTINUE STATEMENT (terminates execution in the current iteration and continues with next iteration) ##############
# i = 1
# while i <= 5:
#     if (i == 3):
#         i += 1
#         continue
#     print(i)  
#     i += 1
    
######### PRINTING ODD NUMBER FROM 1 TO 10 ############ 
# i = 1
# while i <= 10:
#     if (i % 2 == 0):
#         i += 1
#         continue
#     print(i)  
#     i += 1  
    
########## PRINTING EVEN NUMBER FROM 1 TO 10 #############
# i = 1
# while i <= 10:
#     if (i % 2 != 0):
#         i += 1
#         continue
#     print(i)  
#     i += 1 
    
############ FOR LOOP ####################
# list = [1, 2, 3, 4, 5]
# for i in list:
#     print(i)

# str = "python programming"
# for ch in str:
#     if (ch == "o"):
#         print("O found")
#         break
#     print(ch)
# else:
#     print("END")
        
########### PRACTICE ##############
# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# i = 0
# for i in list:
#     print(i)

# tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)  
# x = int(input("enter the element to be searched:"))
# i = 0
# for ele in tuple:
#     if (ele == x):
#         print("element found at index:",i)
#     i += 1
  
########### RANGE FUNCTION range(start, stop, step) ###############
# for i in range(10):  #range(stop)
#     print(i)

# for i in range(2,10):  #range(start, stop)
#     print(i)    

# for i in range(2, 10, 2):  #range(start, stop, step)
#     print(i)

############### PRACTICE OF FOR USING RANGE #############
# for i in range(100):
#     print(i)
    
# for i in range(100, 0, -1):
#     print(i)    

# n = int(input("enter a number:"))
# for i in range(1, 11):
#     print(n,"x",i,"=",n*i)
    
############ PASS STATEMENT ###############
# pass is a null statement that does nothing. 
# for i in range(5):
#     pass
# print("some work.....")

############### WAP to find the sum of first n numbers (using for) ##############
# n = int(input("enter a number:"))
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print("Sum of first n numbers is:",sum)

########### WAP to find factorial of first n numbers (using while) ############
n = int(input("enter a number:"))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("Factorial:",fact)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    