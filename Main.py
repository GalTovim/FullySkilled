import sqlite3
from employee import Employee

conn = sqlite3.connect('FullySkilled.db')
c = conn.cursor()

#c.execute("""CREATE TABLE employees (
#            first text,
#            last text,
#            id integer
#        )""")

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :id)",{'first':emp.first,'last':emp.last,'id': emp.id})

def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()

def get_emps():
    c.execute("SELECT * FROM employees")
    return c.fetchall()

def remove_emp(emp):
    with conn:
        c.execute(f"DELETE from employees WHERE id={emp}")

flag = 1
print("Please Choose What to do:")
print("1. Add new Employee.")
print("2. Delete Employee.")
print("4. Exit.")

while(flag):
    choise = int(input("Enter your choise: "))
    if (choise==1):
            Fname = input("Please Enter Employee Name: ")
            Lname = input("Please Enter Employee Last Name: ")
            ID = input("Please Enter Employee ID: ")
            NewEmployee = Employee(Fname,Lname,ID)
            insert_emp(NewEmployee)
    if (choise==2):
            ID = input("Please Enter Employee ID: ")
            remove_emp(ID)
    if (choise==4):
            flag = 0
print(get_emps())

conn.close()