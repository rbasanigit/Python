# WAP to interchange 1st and last elements of a list
# list1 = [7, 3, 9, 2, 4, 6]
# def swaplist(list1):
#     size = len(list1)
#     temp = list1[0]
#     list1[0] = list1[size - 1]
#     list1[size - 1] = temp
#     return list1
# print(swaplist(list1))

# WAP to find maximum of 2 numbers
# a = int(input("enter first number:"))
# b = int(input("enter second number:"))
# def maximum(a, b):
#     if (a > b):
#         return a
#     else:
#         return b
# print("greatest number is:",maximum(a, b))

# WAP to find minimum of 2 numbers
# a = int(input("enter first number:"))
# b = int(input("enter second number:"))
# def minimum(a, b):
#     if (a < b):
#         return a
#     else:
#         return b
# print("smallest number is:",minimum(a, b))

# WAP to check if a number is palindrome or not
# num = input("enter a number:")
# revnum = num[::-1]
# def checkPalin(num):
#     if (num == revnum):
#         print("palindrome")
#     else:
#         print("not palindrome")
# print(checkPalin(num))

# WAP to remove ith character from a string
# string = "python programming"
# newstr = string.replace('t', '', 1)
# print("string after removing ith character:", newstr)

# WAP to print even length of words from a string
string = "this is a python program"
s = string.split()
for i in s:
    if (len(i) % 2 == 0):
        print(i)
        


























