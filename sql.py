import sqlite3

##Connect to sqlite
connection = sqlite3.connect("student.db")

#creating a cursor
cursor=connection.cursor()
cursor.execute('''DROP TABLE IF EXISTS STUDENT''')
table_info="""
create table STUDENT(BU_ID VARCHAR(9) PRIMARY KEY,NAME VARCHAR(25), MAJOR VARCHAR(25), SUBJECT VARCHAR(25), MARKS INT
);
"""
cursor.execute(table_info)


#inserting some records
cursor.execute('''INSERT INTO STUDENT VALUES('U08184849','SAM','COMPUTER INFORMATION SYSTEMS','ARTIFICIAL INTELLIGENCE',96)''')                                                                                        
cursor.execute('''INSERT INTO STUDENT VALUES('U08184850','AARON','COMPUTER INFORMATION SYSTEMS','ARTIFICIAL INTELLIGENCE',99)''')
cursor.execute('''INSERT INTO STUDENT VALUES('U08184851','MITCH','APPLIED BUSINESS ANALYTICS','DATA SCIENCE',94)''')
cursor.execute('''INSERT INTO STUDENT VALUES('U08184852','BOB','COMPUTER SCIENCE','MACHINE LEARNING',100)''')
cursor.execute('''INSERT INTO STUDENT VALUES('U08184853','CATHERINE','COMPUTER SCINECE','DATA SCIENCE',90)''')
cursor.execute('''INSERT INTO STUDENT VALUES('U08184854','DAVE','COMPUTER INFORMATION SYSTEMS','MACHINE LEARNING',94)''')
cursor.execute('''INSERT INTO STUDENT VALUES('U08184855','JOHN','APPLIED BUSINESS ANALYTICS','ARTIFICIAL INTELLIGENCE',89)''')
cursor.execute('''INSERT INTO STUDENT VALUES('U08184856','ROB','COMPUTER SCIENCE','ARTIFICIAL INTELLIGENCE',98)''')
cursor.execute('''INSERT INTO STUDENT VALUES('U08184857','MATT','COMPUTER INFORMATION SYSTEMS','DATA SCIENCE',88)''')
cursor.execute('''INSERT INTO STUDENT VALUES('U08184858','KATY','APPLIED BUSINESS ANALYTICS','DATA SCIENCE',95)''')





#displaying all the records
print("Inserted records are as follows:")
data = cursor.execute('''SELECT * FROM STUDENT''').fetchall()


print("\nSTUDENT TABLE:")
for row in data:
    print(row)

connection.commit()
connection.close()