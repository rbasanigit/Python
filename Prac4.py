########### DICTIONARY (stores key:value pairs, mutable, no duplicate keys) ################
# info = {
#         "name" : "raasi",
#         "subject" : "python",
#         "age" : 25,
#         "marks" : 95.7,
#         "is_adult" : True
#         }
# print(info)
# print(info["name"])  #returns corresponding value to that key
# print(info["age"])
# info["name"] = "shradha"  #overwrites the previous key value
# print(info)

############## NESTED DICTIONARY #############3
# student = {
#     "name" : "rohan",
#     "subjects" : {
#         "maths" : 92,
#         "phy" : 87,
#         "chem" : 96
#         }
#     }
# print(student)
# print(student["subjects"])
# print(student["subjects"]["phy"])

############# DICTIONARY METHODS ############
# info = {
#         "name" : "raasi",
#         "subject" : "python",
#         "age" : 25,
#         "marks" : 95.7,
#         "is_adult" : True
#         }
# print(info.keys())  #returns all the keys
# print(info.values())  #returns all the values
# print(info.items())  #returns all key value pairs as "tuples"
# print(info.get("age"))  #returns value of the specified key
# info.update({"city" : "hyderabad"})  #inserts specified item to dictionary
# print(info)

############# SET (stores unordered items, each element must be unique and IMMUTABLE) #####################
# collection = {5, 8, 3, 3, 9, "hello", "world", "python", "hello"}
# print(collection)  #returns set unordered
# set ignores the duplicate values
# print(len(collection))
# info = set() #syntax for empty set

# set is mutable but elements in the set are immutable

# set1 = set()
# set1.add(25)  #adds an element
# set1.add(32)
# set1.add((1, 2, 3))  #you can add only tuple not list,dict
# print(set1)
# set1.remove(25)  #removes an element
# print(set1)
# set1.clear()  #empties the set 
# print(set1)
# info = {"hello", "world", "python", "java", "programming"}
# print(info.pop())  #removes and returns any random value
# print(info)

############### UNION AND INTERSECTION IN SETS ####################
# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# print(set1.union(set2))  #combines 2 set values and returns a new set
# print(set1.intersection(set2))  #returns a new set with common values in both sets 

############### PRACTICE #################
# data = {
#         "table" : ["a piece of furniture", "list of facts and figs"],
#         "cat" : "an animal"
#         }
# print(data)

########## WAP where given list of students, assume one classroom for 1 subject. How many classrooms are needed for all subjects ####################
# sub = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++" ,"c"}
# print(sub)
# print("classrooms needed are:",len(sub))

########### WAP to enter marks of 3 subjects from user and store them in dictionary. Start with an empty dictionary. Use subject name as key and marks as value ############################
# marks = {}
# m1 = int(input("enter maths marks:"))
# marks.update({"math" : m1})
# m2 = int(input("enter physics marks:"))
# marks.update({"phy" : m2})
# m3 = int(input("enter chemistry marks:"))
# marks.update({"chem" : m3})
# print(marks)

########### WAP to figure out a way to store 9 and 9.0 as separate values in set ###############
# values = {9, '9.0'}
# print(values)
values = {('float', 9.0), ('int', 9)}
print(values)














































