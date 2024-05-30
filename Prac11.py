############## NUMPY #############
# import numpy as np
# a = np.array([1, 2, 3, 4, 5])  # 1D array
# print(a)
# print(a.ndim)
# print(a.itemsize)  #prints the maximum index of the array
# b = np.array([[1, 2, 3], [4, 5, 6]])  #2D array
# print(b)
# print(b.ndim)  #prints the dimension
# print(b.shape)  #prints the no.of (rows, columns)
# print(a.nbytes)  #prints the no.of bytes

########## ACCESSING ELEMENTS IN ARRAY #############
# c = np.array([[1,2,3,4,5,6,7], [0,9,8,7,6,5,4]])
# print(c[1, 5])  #displays [row, column]
# print(c[0, : 2])

######### METHODS ############## 
# d = np.array([[[1,2],[3,4],[5,6],[7,8]]])
# print(d)
# print(d.ndim)
# s = np.zeros((2,3))  #displays an array of zeros (dim, no.of elements)
# print(s)
# print(s.ndim)
# p = np.ones((2, 3, 4))  #displays an array of ones
# print(p)
# print(p.ndim)

# d = np.full((2, 3), 99)  #to fill the array with one specific value ((row,col), value)
# print(d)

############# MATPLOTLIB ################
# import matplotlib.pyplot as plt
# x = [7, 3, 9]
# y = ['a', 'b', 'c']
# plt.plot(x, y)  #plt.plot is for simple line graph
# plt.title("Demo graph")  #to edit graph name
# plt.xlabel("numbers")  #to edit x axis name
# plt.ylabel("letters")  #to edit y axis name
# plt.show()  #to display the graph

# a = np.array([1, 8])
# b = np.array([3, 10])
# # plt.plot(a, b)

# plt.plot(a, b, marker = 'o', linestyle = 'dotted')  #marker parameter is used to put any symbol instead of line

# plt.plot(a, b, color = 'red', linewidth = '10.5')  #color parameter is used to change the colour of the graph
# plt.show()


################ BAR GRAPH ################
# a = ["java", "c++", "c", "python", "dotnet"]
# b = [78, 54, 32, 96, 10]
# plt.bar(a, b)  #plt.bar is for bar graph
# plt.barh(a, b)  #plt.barh is for plotting horizontal bar graph
# plt.show()

################ LEGEND FUNCTION ###############
# x = [7, 3, 9]
# y = ['a', 'b', 'c']
# b = ["java", "c++", "c", "python", "dotnet"]
# a = [78, 54, 32, 96, 10]
# plt.bar(x, y, label = "first")  #label is used to display the label each graph
# plt.bar(a, b, label = "second")
# plt.legend()  #used to display 2 graphs     
# plt.show()

############# HISTOGRAM ##############
# x = np.array([22, 45, 87, 56, 93, 12, 70])
# plt.hist(x)  #used for plotting histogram

# plt.hist(x, bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])  #bins displays the intervals to be taken
# plt.show()

############## PIE CHART ##################
# data = [300, 569, 250, 421, 834]
# info = ["pens", "shirts", "dresses", "books", "tables"]
# plt.pie(data, labels = info)  #used to display pie chart
# plt.grid(True)
# plt.show()

############## SCATTER PLOT ###########
# rooms = [5, 3, 2, 9, 1, 6]
# stand = ["10th", "11th", "8th", "5th", "6th", "12th"]
# plt.scatter(rooms, stand, color = 'green')  #used for scatter plot
# plt.xlabel("rooms allocated for each standard")
# plt.ylabel("classes")
# plt.show()



















