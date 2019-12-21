#pragma once
#include "employee.h"

//default constructor
Employee::Employee(const Employee &emp) : Person(emp)
{
  this->salary = emp.salary;
}
//constructor
Employee::Employee(float Salary, int age, string name, long id) : Person(name, id, age)
{
  this->salary = salary;
}
//d'tor
Employee::~Employee()
{
  cout << "Employee C'tor" << endl;
}