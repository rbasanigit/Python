############ RANDOM NUMBERS ##############
# import random

# value = random.uniform(1, 10)  #displays decimal numbers
# print(value)
# value2 = random.randint(1, 20)  #displays integer numbers
# print(value2) 

# greet = ["hi", "hello", "hey", "hola", "howdy"]
# val3 = random.choice(greet)  #displays word from the list 
# print(val3) 

# colors = ["red", "green", "blue", "yellow", "purple"]
# val4 = random.choices(colors, k = 10)  #displays multiple words
# print(val4)

# deck = list(range(1, 53))
# random.shuffle(deck)  #shuffles the numbers in the list and displays
# print(deck)
 
# deck = list(range(1, 53))
# hand = random.sample(deck, k = 5)  #displays only a sample with the parameter
# print(hand)

########## PANDAS (SERIES - represented in the form of rows along with index) #############
import pandas as pd
import numpy as np
# data = ["apple", "banana", "grapes", "mango", "strawberry"]
# s = pd.Series(data)  # S should be capital 
# print(s)  #index starts from 0 

# label = ['a', 'b', 'c', 'd', 'e']  #exact no.of elements must be given otherwise error occurs
# s = pd.Series(data, index=label)  #can give your own indexes by list
# print(s)

# Series can hold numeric, text, functions, dictionary objects

############# INDEXING AND SLICING IN SERIES ################
# s1 = pd.Series([1, 2, 3, 4], index = ['a', 'b', 'c', 'd'])
# s2 = pd.Series([5, 6, 7, 8], index = ['e', 'f', 'g', 'h'])
# print(s1[0])  #corresponding value will be printed
# print(s2[3])
# print(s1[0:2])
# print(s2[1:3])

############ MERGING SERIES ###############
# s1 = pd.Series([1, 2, 3, 4], index = ['a', 'b', 'c', 'd'])
# s2 = pd.Series([5, 6, 7, 8], index = ['a', 'b', 'c', 'd'])  #should have matching index otherwise shows NaN 
# res = s1 + s2
# print(res)

############### PANDAS (DATAFRAME - represented in the form of rows and cols) ###################
# colours = ["red", "green", "yellow", "pink", "blue"]
# cols = ["color"]
# rows = [1, 2, 3, 4, 5]
# df = pd.DataFrame(data = colours, index = rows, columns = cols)  #index is row index and columns is column index, D and F should be capital
# print(df)

############### INDEXING AND SLICING IN DATAFRAMES ################
# colours = ["red", "green", "yellow", "pink", "blue"]
# cols = ["color"]
# rows = [1, 2, 3, 4, 5]
# df = pd.DataFrame(data = colours, index = rows, columns = cols)  
# print(df["color"])  #specify the column index

############## CREATING AND DELETING NEW ROW AND COLUMN ############
# colours = ["red", "green", "yellow", "pink", "blue"]
# cols = ["color"]
# rows = [1, 2, 3, 4, 5]
# df = pd.DataFrame(data = colours, index = rows, columns = cols)
# df["things"] = ["pen", "pencil", "jacket", "dress", "car"] 
# print(df)
# df = df.drop("things", axis = 1)  #default axis = 0 (for deleting row) and axis = 1 (for deleting columns)
# print(df)
# df = df.drop(4)  #you can take df= or in the (,inplace=True) to drop 
# print(df)

############ SELECTING AND INDEXING IN ROWS #################
# colours = ["red", "green", "yellow", "pink", "blue"]
# cols = ["color"]
# rows = [1, 2, 3, 4, 5]
# df = pd.DataFrame(data = colours, index = rows, columns = cols)  
# df["things"] = ["pen", "pencil", "jacket", "dress", "car"]
# print(df)
# print(df.loc[1])  #in loc it should specify the name of the index row, displays the corresponding row
# print(df.loc[[1, 5]])  #can display only specified rows
# print(df.iloc[3])  #in iloc it should specify the index 
# print(df.iloc[[2, 4]])
# print(df.loc[[2],["things"]])  #to display specific row and column

############ CHECKING BOOLEAN DATAFRAME #############
# integer = [-5, 7, -3, -8, 2]
# df = pd.DataFrame(integer, columns = ["integer"])
# df["decimal"] = [32.7, -98.5, 26.1, -19.5, 0.3]
# print(df)
# print(df>0)  #displays True or False

############# MISSING VALUES ###############3
# df = pd.DataFrame({'A' : [1, 2, np.nan], 'B' : [5, 6, np.nan], 'C' : [np.nan, 8, 9]})
# df["states"] = "CA NV AZ".split()  #it splits the given string
# df.set_index("states", inplace = True)
# print(df)
# print(df.dropna(axis = 0))  #axis = 0 is deleting row which has NaN values
# print(df.dropna(axis = 1))  #axis = 1 is deleting column which has NaN values
# print(df.fillna(value = 10))  #it fills the NaN places with the specified value

############ GROUPBY METHOD #############
# data = {'company' : ['google', 'amazon', 'amazon', 'microsoft', 'google'],
#         'person' : ['rishi', 'minnu', 'pooja', 'ani', 'sara'],
#         'salary' : [75000, 62000, 40000, 85000, 93000]}
# df = pd.DataFrame(data)
# print(df)
# bycomp = df.groupby('company')  #it displays output without any multiple values
# print(bycomp)

############ FEW OPERATIONS ###########
data = {'company' : ['google', 'amazon', 'flipkart', 'microsoft', 'facebook', 'twitter', 'instagram', 'snapchat'],
        'person' : ['rishi', 'minnu', 'pooja', 'ani', 'charan', 'sara', 'kavya', 'rahul'],
        'salary' : [75000, 62000, 40000, 85000, 64000, 32000, 28000, 95000]}
df = pd.DataFrame(data)
print(df)
# print(df.head())  #head() default displays first 5 rows 
print(df.head(2))
#print(df.tail())  #tail() default displays last 5 rows
print(df.tail(3))
print(df["person"].nunique())  #to find the no.of unique values in a specific column

















































