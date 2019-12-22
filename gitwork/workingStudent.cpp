#include "workingStudent.h"


workingStudent::workingStudent(int Average, string Institute, int Age, string name, long id, int salary)
	: Student(Average, Institute, Age,name, id),
	Employee(salary, Age, name, id)
{}

workingStudent::workingStudent(workingStudent & ws)
{
	this->Average = ws.Average;
	this->Institute = ws.Institute;
	this->Age = ws.Age;
	this->Name = ws.Name;
	this->ID = ws.ID;
	this->salary = ws.salary;
	this->same_institute = ws.same_institute;
}




workingStudent ::~workingStudent()
{
}

void workingStudent::WhoAmI()
{
	cout << "a working student!" << endl;
}
