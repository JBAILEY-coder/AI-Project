'''
Group Members:

-J'Nelle Bailey: 2008135
-Shavar Black: 2002379
-Sassania Hibbert: 1901201
-Leondre Bronfield 2000070
'''
# creating connection

import sqlite3  # import for handling sql
from pyswip import Prolog

# package to install: mysql-connector-python

# prolog code plugin
# python plugin
# GNU Prolog Interpreter

prolog = Prolog()
prolog.consult("gpa_update.pl")

connection = sqlite3.connect("studentmaster.db")
cursor = connection.cursor()


# put each create and insert into a function
def createtables():
    # createStudents
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS studentmaster(
        studentid INTEGER PRIMARY KEY,
        studentname VARCHAR(255) NOT NULL,
        studentemail VARCHAR(255) NOT NULL,
        school VARCHAR(255) NOT NULL,
        programme VARCHAR(255) NOT NULL
     )
    """)
    # createModules
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS modulemaster(
            moduleid INTEGER PRIMARY KEY,
            module VARCHAR(255) NOT NULL,
            numberofredits INTEGER
        )
    """)
    # createDetails
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS moduledetails(
            moduleid INTEGER,
            module VARCHAR(255) NOT NULL,
            year VARCHAR(255),
            semester VARCHAR(255),
            studentid INTEGER NOT NULL,
            gradepoints iINT,
            FOREIGN KEY(studentid) REFERENCES studentmaster(studentid),
            FOREIGN KEY(moduleid) REFERENCES modulemaster(moduleid)
        )
    """)
    cursor.execute("""
        CREATE UNIQUE INDEX moduledetails_table ON moduledetails(moduleid, studentid)
                   """)
    connection.commit()

"""
# SQL query to drop a table
def DropTable():
    table_to_drop = 'moduledetails'  # Replace 'your_table_name' with the name of the table to drop
    drop_query = f"DROP TABLE IF EXISTS {table_to_drop};"
    cursor.execute(drop_query)
    connection.commit()
    connection.close()

def insertModuleDetails(Module, Year, Semester, ID, Grade_Points):
    insertDetails = (f"INSERT OR IGNORE INTO module_details (Module, Year, Semester, ID, Grade_Points) VALUES"
                     f" ('{Module}', {Year}, {Semester}, {ID}, {Grade_Points})")
    cursor.execute(insertDetails)
    connection.commit()


def insertStudentRecord(ID, First_name, Last_Name, Email, School, Programme):
    insertStudents = (
        f"INSERT OR IGNORE INTO student_master (ID, First_name, Last_Name, Email, School, Programme) VALUES"
        f"({ID},'{First_name}','{Last_Name}','{Email}','{School}','{Programme}')")
    cursor.execute(insertStudents)
    connection.commit()


def insertModuleMaster(Module, Credits):
    insertModules = (f"INSERT OR IGNORE INTO module_master (Module, Credits) VALUES"
                     f"('{Module}',{Credits})")
    cursor.execute(insertModules)
    connection.commit()

"""
# create classes for sql functions, ie: insert,delete,update etc

def select_module(year, gpa):
    # function to query database for year entered
    cursor.execute(f"SELECT * FROM module_details WHERE Year={year} AND Grade_Points={gpa}")
    results = cursor.fetchall()
    print(results)
    # calling function here to add results to kb
    add_students()
    get_modules_fromDB()
    get_module_master()
    # edit query and join with module master to get num of credits
    # separate results
    # assert to prolog, then make function call


# Adds student record to the knowledge base
def add_students_prolog(record):
    try:
        # add record to knowledge base
        prolog.assertz(
            f"student({record[0]}, '{record[1]}', '{record[2]}', '{record[3]}', '{record[4]}', '{record[5]}')")
        # check if record was added to knowledge base
        result = list(prolog.query(f"student({record[0]}, _, _, _, _, _)"))
        if not result:
            print("Student record wasn't added!")
            return None
    except Exception as e:
        print(e)
        return None


# Retrieve records from database
def add_students():
    cursor.execute("SELECT * FROM student_master")
    results = cursor.fetchall()

    for result in results:
        add_students_prolog(result)  # calls function that adds student record to the knowledge base


# Add modules to knowledge base
def add_modules_toKB(module):
    try:
        prolog.assertz(
            f"module_details('{module[0]}',{module[1]},{module[2]},{module[3]},{module[4]})")
    except Exception as e:
        print(e)
        return None


# get module details from db and then call function to assert each module
def get_modules_fromDB():
    cursor.execute("SELECT * FROM module_details")
    modules = cursor.fetchall()

    for module in modules:
        add_modules_toKB(module)


def add_masters_toKB(master):
    try:
        prolog.assertz(
            f"module('{master[0]}',{master[1]})")
    except Exception as e:
        print(e)
        return None

# get module master info from db and then call function to assert each
def get_module_master():
    cursor.execute("SELECT * FROM module_master")
    masters = cursor.fetchall()

    for master in masters:
        add_masters_toKB(master)
