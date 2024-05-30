############### LISTS (can store different data types) ################
# marks = [94.4, 87.5, 95.2, 66.3, 45.1]
# print(marks)
# print(marks[0])
# print(marks[-2])
# marks[3] = 73.1
# print(marks)

# Strings are IMMUTABLE (cannot be changed)
# Lists are MUTABLE (can be changed)

############## SLICING IN LISTS (ending index not included) #############
# marks = [87, 64, 33, 95, 76]
# print(marks[1:4])
# print(marks[:4])  #same as marks[0:4]
# print(marks[1:])  #same as marks[1:len(marks)]
# print(marks[-3:-1])

############## LIST METHODS ####################
# list = [2, 1, 3]
# list.append(4)  #adds element at the end
# print(list)
# list.sort()  #sorts in ascending order
# print(list)
# list.sort(reverse = True)  #sorts in descending order
# print(list)
# list.reverse()  #reverses the list
# print(list)
# list.insert(1,5)  #inserts element at specified index (index,element)
# print(list)
# list = [2, 1, 3, 1]
# list.remove(1)  #removes 1st occurrence of the element
# print(list)
# list.pop(0)  #deletes element at particular index [pop(index)]
# print(list)

# list = ["banana", "litchi", "apple"]
# list.sort()
# print(list)
# list.sort(reverse = True)
# print(list)

################# TUPLES (can store different data types but are IMMUTABLE (cannot be changed)) #######################
# tup = (2, 1, 3, 1)
# print(tup[2])
# tup[0] = 5 (NOT POSSIBLE)
# tup1 = (56,) (correct way to create single value tuple)
# slicing is same as lists

############# TUPLE METHODS ##################
# tup = (2, 1, 3, 1, 5, 1)
# print(tup.index(3))  #returns index of 1st occurrence of that element
# print(tup.count(1))  #counts total occurrences of the element

############# WAP to ask user to enter names of 3 movies and store in list ####################
# movies = []
# m1 = input("enter 1st movie:")
# m2 = input("enter 2nd movie:")
# m3 = input("enter 3rd movie:")
# movies.append(m1)
# movies.append(m2)
# movies.append(m3)
# print(movies)

################# WAP to check if the list contains palindrome of elements ################
#list1 = [1, 2, 1]
# list2 = [1, 2, 3]
# copy_list2 = list2.copy()
# copy_list2.reverse()
# if (list2 == copy_list2):
#     print("Palindrome")
# else:
#     print("Not palindrome")    

############## WAP to count the no.of students having 'A' grade in the tuple ###############
# grade = ('C', 'D', 'A', 'A', 'B', 'B', 'A')
# print(grade.count('A'))

########### Store the above values in a list and sort them from A to D ###########
grade = ['C', 'D', 'A', 'A', 'B', 'B', 'A']
grade.sort()
print(grade)



















































