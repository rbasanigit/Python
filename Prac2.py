################## ESCAPE SEQUENCE CHARACTERS ##################
# str = "This is a string.\nWe are creating in python." #\n prints in new line
# #\t prints with tab space
# print(str)

################ CONCATE 2 STRINGS WITH "+" ####################
# str1 = "Hello"
# str2 = "Python"
# str = str1 + str2
# print(str)
# print(len(str))

################ INDEXING IN STRING (displays a character from string) ####################
# str = "This is a demo"
# print(str[3]) #we cannot assign new value using indexing

############## SLICING IN STRING (displays a part of string) ##################
# str = "This is a python class"
# print(str[1:6]) #1st parameter is start and 2nd parameter is stop, it display n-1 characters
# str2 = "Apple"
# print(str2[-3 : -1])

######### STRING FUNCTIONS #######################
# str = "i am a programmer"
# print(str.endswith("er")) #returns True if string ends with the substring
# print(str.capitalize()) #capitalizes the 1st character
# print(str.replace("programmer" , "coder")) #replaces all old occurrences with new
# print(str.find("pr")) #returns 1st index of 1st occurrence
# print(str.count("am")) #counts the occurrence of substring in the string

############ CONDITIONAL STATEMENTS ###############
# light = "green"
# if (light == "red"):
#     print("STOP")
# elif (light == "yellow"):
#     print("WAIT")
# else:
#     print("GO")    

################ NUMBER IS ODD OR EVEN ################
# num = int(input("enter a number:"))
# remain = num % 2
# if (remain == 0):
#     print("number is even")
# else:
#     print("number is odd")    

################ GREATEST OF 3 NUMBERS ##################
# n1 = int(input("enter 1st number:"))
# n2 = int(input("enter 2nd number:"))
# n3 = int(input("enter 3rd number:"))
# if (n1 > n2 and n1 > n3):
#     print(n1,"is greater")
# elif (n2 > n1 and n2 > n3):
#     print(n2,"is greater")
# else:
#     print(n3,"is greater")    

################ CHECK IF A NUMBER IS MULTIPLE OF 7 OR NOT ###############
n = int(input("enter a number:"))
if (n % 7 == 0):
    print(n,"multiple of 7")
else:
    print(n,"not a multiple of 7")    








































