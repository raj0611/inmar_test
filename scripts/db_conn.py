


import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="imr_test"
)

# print(mydb)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE imr_test")


# Meta data

'''
Location,Department,Category,SubCategory
Perimeter,Bakery,Bakery Bread,Bagels
Perimeter,Bakery,Bakery Bread,Baking or Breading Products
Perimeter,Bakery,Bakery Bread,English Muffins or Biscuits
Perimeter,Bakery,Bakery Bread,Flatbreads
Perimeter,Bakery,In Store Bakery,Breakfast Cake or Sweet Roll
Perimeter,Bakery,In Store Bakery,Cakes
Perimeter,Bakery,In Store Bakery,Pies
Perimeter,Bakery,In Store Bakery,Seasonal
Center,Dairy,Cheese,Cheese Sauce
Center,Dairy,Cheese,Specialty Cheese
Center,Dairy,Cream or Creamer,Dairy Alternative Creamer
Center,Frozen,Frozen Bake,Bread or Dough Products Frozen
Center,Frozen,Frozen Bake,Breakfast Cake or Sweet Roll Frozen

'''

# mycursor.execute("CREATE TABLE emp (Location VARCHAR(255), Department VARCHAR(255), Category VARCHAR(255), SubCategory VARCHAR(255))")

sql = "INSERT INTO emp (Location,Department,Category,SubCategory) VALUES (%s, %s, %s, %s)"
data = [
    ("Perimeter","Bakery","Bakery Bread","Bagels"),
    ("Perimeter","Bakery","Bakery Bread","Baking or Breading Products"),
    ("Perimeter","Bakery","Bakery Bread","English Muffins or Biscuits"),
    ("Perimeter","Bakery","Bakery Bread","Flatbreads"),
    ("Perimeter","Bakery","In Store Bakery","Breakfast Cake or Sweet Roll"),
    ("Perimeter","Bakery","In Store Bakery","Cakes"),
    ("Perimeter","Bakery","In Store Bakery","Pies"),
    ("Perimeter","Bakery","In Store Bakery","Seasonal"),
    ("Center","Dairy","Cheese","Cheese Sauce"),
    ("Center","Dairy","Cheese","Specialty Cheese"),
    ("Center","Dairy","Cream or Creamer","Dairy Alternative Creamer"),
    ("Center","Frozen","Frozen Bake","Bread or Dough Products Frozen"),
    ("Center","Frozen","Frozen Bake","Breakfast Cake or Sweet Roll Frozen")
]
# val = ("John", "Highway 21")

# for val in data:
#     mycursor.execute(sql, val)
# mydb.commit()


print(mycursor.rowcount, "record inserted.")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)