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

def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE id=:id",
                  {'id':emp.id})

emp_1 = Employee('Gal','Tovim',305484677)

insert_emp(emp_1)
emps=get_emps_by_name('Tovim')
print(emps)
remove_emp(emp_1)
emps=get_emps_by_name('Tovim')

print(emps)

conn.close()