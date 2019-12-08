import sqlite3
from employee import Employee

conn = sqlite3.connect('FullySkilled.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS employees (
            first text,
            last text,
            id integer,
            mail text,
            cv text,
            phone integer,
            skill text
        )""")

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :id, :mail, :cv, :phone, :skill)",{'first':emp.first,'last':emp.last,'id': emp.id,
                                                                       'mail':emp.mail,
                                                                       'cv':emp.cv,'phone':emp.phone,
                                                                       'skill':emp.skill})

def update_emp(emp, first):
    with conn:
        c.execute("""UPDATE employee SET first= :first 
        WHERE first = :first AND last= :last""",
                  {'first':emp.first,'last':emp.last,'id': emp.id,
                                                 'mail':emp.mail,
                                                 'cv':emp.cv,'phone':emp.phone,
                                                 'skill':emp.skill})

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
print("3. Search Employee by Last Name.")
print("4. Exit.")

while(flag):
    choise = int(input("Enter your choise: "))
    if (choise==1):
            Fname = input("Please Enter Employee Name: ")
            Lname = input("Please Enter Employee Last Name: ")
            ID = input("Please Enter Employee ID: ")
            Mail = input("Please Enter Employee Mail: ")
            Cv = input("Please Enter Employee CV: ")
            Phone = input("Please Enter Employee Phone: ")
            Skill = input("Please Enter Employee Skill: ")
            NewEmployee = Employee(Fname,Lname,ID,Mail,Cv,Phone,Skill)
            insert_emp(NewEmployee)
    if (choise==2):
            ID = input("Please Enter Employee ID: ")
            remove_emp(ID)
    if (choise==3):
            LastName = input("Please Enter Last Name to Search: ")
            print(get_emps_by_name(LastName))
    if (choise==4):
            flag = 0
print(get_emps())

conn.close()