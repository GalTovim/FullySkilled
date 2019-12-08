import sqlite3
from employee import Employee

conn = sqlite3.connect('FullySkilled.db')

c = conn.cursor()

#c.execute("""CREATE TABLE employees (
#            first text,
#            last text,
#            integer id
#        )""")

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :id)",{'first':emp.first,'last':emp.last,'id': emp.id})

def get_emps_by_id(id):
    c.execute("SELECT * FROM employees WHERE id=:id", {'id': id})
    return c.fetchall()

def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE id=:id",
                  {'id':emp.id})

emp_1 = Employee('Gal','Tovim',305484677)

insert_emp(emp_1)
emps=get_emps_by_id(emp_1)

print(emps)

conn.close()