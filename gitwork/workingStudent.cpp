#include "workingStudent.h"

workingStudent::workingStudent(int Average, string Institute, int Age, string name, long id, int salary, bool same_institute)
	: Student(Average, Institute, Age, name, id), Employee(salary, Age, name, id), same_institute(same_institute)
{}

workingStudent::workingStudent(workingStudent& ws):Student(ws),Employee(ws)
{
	this->same_institute = ws.same_institute;
}

workingStudent::~workingStudent()
{}



void workingStudent::WhoAmI()
{
	cout << "a working student!" << endl;
}