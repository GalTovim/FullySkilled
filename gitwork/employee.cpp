#include "employee.h"
//default constructor
/*
Employee::Employee(const Employee& emp) : Person(emp)
{
	this->salary = emp.salary;
}
*/
//constructor
Employee::Employee(float Salary, int age, string name, long id) : Person(name, id, age)
{
	this->salary = salary;
}

/*
//copy constructor
Employee::Employee(const Employee& CopyEmployee) {
	salary = CopyEmployee.salary;
	Age = CopyEmployee.Age;
	Name = CopyEmployee.Name;
	ID = CopyEmployee.ID;
}
*/
Employee::~Employee(){}

void Employee::WhoAmI(){
cout << "an Employee" << endl;
}