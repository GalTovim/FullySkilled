from employer import Employer
import sqlite3

#epmr=Employer('yoni','binyamini',304817539,'yonile2106@gmail.com','super market')

conn = sqlite3.connect('FullySkilled.db')
c = conn.cursor()

#c.execute("""CREATE TABLE employers (
#            first text,
#            last text,
#           id integer,
#            mail text,
#            business name text
#        )""")

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employers VALUES (:first, :last, :id, :mail, :business)",{'first':emp.first,'last':emp.last,'id': emp.id, 'mail':emp.mail,'business_name':emp.business_name})

def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employers WHERE last=:last", {'last': lastname})
    return c.fetchall()

def get_emps():
    c.execute("SELECT * FROM employers")
    return c.fetchall()

def remove_emp(emp):
    with conn:
        c.execute(f"DELETE from employers WHERE id={emp}")

flag = 1
print("Please Choose What to do:")
print("1. Add new Employer.")
print("2. Delete Employer.")
print("4. Exit.")

while(flag):
    choise = int(input("Enter your choise: "))
    if (choise==1):
            Fname = input("Please Enter Employer Name: ")
            Lname = input("Please Enter Employer Last Name: ")
            ID = input("Please Enter Employer ID: ")
            mail = input("Please Enter Employer mail: ")
            business = input("Please Enter Employer business name: ")
            NewEmployer = Employer(Fname,Lname,ID,mail,business)
            insert_emp(NewEmployer)
    if (choise==2):
            delete=input("Are you sure you want to delete your user name? y/n")
            if delete=='y' or delete=='yes': 
                ID = input("Please Enter Employer ID: ")
                remove_emp(ID)
            else:
                continue
    if (choise==4):
            flag = 0
print(get_emps())

conn.close()