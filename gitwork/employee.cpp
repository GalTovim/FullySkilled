#include "employee.h"

//default constructor
Employee::Employee(const Employee &emp) : Person(emp)
{
  this->salary = emp.salary;
}
//constructor
Employee::Employee(float Salary, int Age, string name, long id) : Person(name, id, Age)
{
  this->salary = salary;
}
//d'tor
Employee::~Employee()
{
  cout << "Employee C'tor" << endl;
}