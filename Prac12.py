############## SQLITE3 ##############
import sqlite3
# conn = sqlite3.connect("customer.db")  #used to create a new database
# c = conn.cursor()  #used to create a cursor which allows us to do anything

# c.execute(""" CREATE TABLE customer (name text, cno integer, email text) """)  #used for creating table (CREATE TABLE tablename(mention categories wanted along with datatypes))
# after creating a table no need to use the CREATE TABLE syntax again

# c.execute("""INSERT INTO customer VALUES ("pooja", 8102927034, "pooja@gmail.com")""")
# after inserting records into the table no need to use INSERT INTO syntax 

# result = conn.execute("""SELECT * FROM customer""")  # '*' used to display all the records / the row(s) to be displayed by specifying the row name(s) instead of '*'
# for i  in result:
#     print(i)

# result = conn.execute("""SELECT * FROM customer WHERE name = "virat" """)  # WHERE is used to display specific row and can also use AND/OR to display with more specifications
# for i  in result:
#     print(i)
    
# c.execute("""UPDATE customer SET name = "ani" WHERE email = "virru@gmail.com" """)  #UPDATE is used to update any value using SET and a condition WHERE

# c.execute("""DELETE FROM customer WHERE name = "rishu" """)  #DELETE is used to remove any record using WHERE condition

# c.execute("""DROP TABLE customer """)  #used to delete the entire table 
# result = conn.execute("""SELECT * FROM customer""")
# for i  in result:
#     print(i)
# conn.commit()  #to commit the command
# conn.close()  #to close the connection

################ PRACTICE ################## 
db = sqlite3.connect("course.db")
db = db.cursor()
# db.execute("""CREATE TABLE courseinfo (cname text, cid integer, credits integer, teacher text)""")
db.execute("""INSERT INTO courseinfo VALUES ('python', 2021, 5, 'jyothi')""")
db.execute("""INSERT INTO courseinfo VALUES ('java', 2022, 8, 'pradeep')""")
db.execute("""INSERT INTO courseinfo VALUES ('c lang', 2023, 4, 'rekha')""")
db.execute("""INSERT INTO courseinfo VALUES ('coa', 2024, 2, 'maridasu')""")
db.execute("""INSERT INTO courseinfo VALUES ('ads', 2025, 5, 'shekar')""")
result = db.execute("""SELECT * FROM courseinfo WHERE cname = "c lang" HAVING teacher = "rekha" """)  #HAVING is used to specify a condition
for i in result:
    print(i)
db.close()

































