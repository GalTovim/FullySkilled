#include"student.h"
#include"employee.h"
#pragma once
using namespace std;

class workingStudent : virtual public Employee , virtual public Student
{
public:
	workingStudent(int Average, string Institute, int Age, string name, long id, int salary);
	workingStudent(workingStudent& ws);
	~workingStudent();

private:
	bool same_institute;
	virtual void WhoAmI();
};
