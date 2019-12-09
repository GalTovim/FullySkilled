import sqlite3
from employee import Employee
from employer import Employer
conn = sqlite3.connect('FullySkilled.db')
c = conn.cursor()

#Creates tables of employees and employers
c.execute("""CREATE TABLE IF NOT EXISTS employees (
            first text,
            last text,
            id integer,
            mail text,
            cv text,
            phone integer,
            skill text
        )""")
c.execute("""CREATE TABLE IF NOT EXISTS employers (
            first text,
            last text,
            id integer,
            mail text,
            business name text
        )""")
c = conn.cursor()

#Employee Functions
def InsertEmployee(emp):
    with conn: c.execute("INSERT INTO employees VALUES (:first, :last, :id, :mail, :cv, :phone, :skill)",{'first':emp.first,'last':emp.last,'id': emp.id,
                                                                       'mail':emp.mail,
                                                                       'cv':emp.cv,'phone':emp.phone,
                                                                       'skill':emp.skill})
def UpdateEmployee(emp, id):
    with conn: c.execute("""UPDATE employee SET id= :id WHERE id = :id""",{'first':emp.first,'last':emp.last,'id': emp.id,'mail':emp.mail,'cv':emp.cv,'phone':emp.phone,'skill':emp.skill})
def GetEmployeeByID(id):
    c.execute(f"SELECT * FROM employees WHERE id={id}")
    return c.fetchall()
def CheckEmployeeByID(id):
    c.execute("SELECT id FROM employees WHERE id={id}")
def GetAllEmployees():
    c.execute("SELECT * FROM employees")
    return c.fetchall()
def RemoveEmployee(emp):
    with conn:
        c.execute(f"DELETE from employees WHERE id={emp}")

#Employer Functions
def InsertEmployer(emp):
    with conn: c.execute("INSERT INTO employers VALUES (:first, :last, :id, :mail, :business_name)",{'first':emp.first,'last':emp.last,'id': emp.id, 'mail':emp.mail,'business_name':emp.business_name})
def GetEmployerByID(id):
    c.execute(f"SELECT * FROM employers WHERE id={id}")
    return c.fetchall()
def CheckEmployerByID(id):
    c.execute("SELECT id FROM employer WHERE id={id}")
    return c.fetchall()
def GetAllEmployers():
    c.execute("SELECT * FROM employers")
    return c.fetchall()
def RemoveEmployer(emp):
    with conn:
        c.execute(f"DELETE from employers WHERE id={emp}")

#The Start of the Program
NewEmployee = Employee('Gal','Tovim',305484677,'gal2077@gmail.com','NONE',972506723042,'Engineer')
InsertEmployee(NewEmployee)
NewEmployer = Employer('David','Vovila',205484677,'david2077@gmail.com','Net4U')
InsertEmployer(NewEmployer)
flag = True
print("Welcome to FullySkilled,")
print("Website for Job Search for incapables!")
ID = input("Please Enter your ID to Log in: ")

c.execute(f"SELECT count(*) FROM employees WHERE id={ID}")
data=c.fetchone()[0]
if data == 0:
    c.execute(f"SELECT count(*) FROM employers WHERE id={ID}")
    data = c.fetchone()[0]
    if data ==0:
        print('ID doesnt Exists in Employee or Employer Tables.')
        choise = input('Would you like to Register? [1 - Yes][2 - No]:  ')
        print(choise)
        if (choise == '1'): print("Not Avaiable! [1]")
        elif (choise == '2'): print("Still Not Avaiable! [2]")
        else: print("Wrong input Insert.")
    else:
        while (flag):
            print("\nPlease Choose What to do:")
            print("1. Add new Employer.")
            print("2. Delete Employer.")
            print("3. Search Employer by ID.")
            print("4. Exit.")
            choise = int(input("Enter your choise: "))
            if (choise == 1):
                Fname = input("Please Enter Employer Name: ")
                Lname = input("Please Enter Employer Last Name: ")
                ID = input("Please Enter Employer ID: ")
                Mail = input("Please Enter Employer Mail: ")
                Buss = input("Please Enter Employer Bussness Name: ")
                NewEmployer = Employer(Fname, Lname, ID, Mail, Buss)
                InsertEmployer(NewEmployer)
            if (choise == 2):
                ID = input("Please Enter Employer ID: ")
                RemoveEmployer(ID)
            if (choise == 3):
                ID = input("Please Enter ID to Search: ")
                c.execute(f"SELECT count(*) FROM employers WHERE id={ID}")
                data = c.fetchone()[0]
                if data == 0:
                    print('Employers Table: No ID Exists.')
                else:
                    print(GetEmployerByID(ID))
            if (choise == 4):
                flag = 0
else:
    while (flag):
        print("\nPlease Choose What to do:")
        print("1. Add new Employee.")
        print("2. Delete Employee.")
        print("3. Search Employee by ID.")
        print("4. Update Employee by ID")
        print("5. Exit.")
        choise = int(input("Enter your choise: "))
        if (choise == 1):
            Fname = input("Please Enter Employee Name: ")
            Lname = input("Please Enter Employee Last Name: ")
            ID = input("Please Enter Employee ID: ")
            Mail = input("Please Enter Employee Mail: ")
            Cv = input("Please Enter Employee CV: ")
            Phone = input("Please Enter Employee Phone: ")
            Skill = input("Please Enter Employee Skill: ")
            NewEmployee = Employee(Fname, Lname, ID, Mail, Cv, Phone, Skill)
            InsertEmployee(NewEmployee)
        if (choise == 2):
            ID = input("Please Enter Employee ID: ")
            RemoveEmployee(ID)
        if (choise == 3):
            ID = input("Please Enter ID to Search: ")
            c.execute(f"SELECT count(*) FROM employees WHERE id={ID}")
            data = c.fetchone()[0]
            if data == 0:
                print('Employees Table: No ID Exists.')
            else: print(GetEmployeeByID(ID))
        if (choise == 4):
                ID = input("Enter your ID: ")
        if (choise == 5):
            flag = 0

#The End of the Program
conn.close()