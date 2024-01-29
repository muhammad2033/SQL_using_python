import sqlite3

connect = sqlite3.connect('data.db')

# connect.execute("drop table if exits  costumer")
# connect .execute('''
#                  create table costumer 
#                  (ID int  primary key  not null,
#                  name text not null,
#                  age int  not null);''')

connect.execute(" INSERT  INTO COSTUMER (ID , name , age) values (1,'maaz',23)")
connect.execute(" INSERT INTO COSTUMER  (ID , name , age) values (2,'saad',25)")

all_data = connect.execute(''' SELECT * FROM COSTUMER ''')

for row in all_data:
    print(row)
connect.close()
