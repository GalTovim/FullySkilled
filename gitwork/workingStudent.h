#pragma once
#include"student.h"
#include"employee.h"
using namespace std;

class workingStudent : virtual public Employee, virtual public Student
{
public:
	workingStudent(int Average, string Institute, int Age, string name, long id, int salary, bool same_institute);
	workingStudent(workingStudent& ws);
	~workingStudent();
private:
	bool same_institute;
	virtual void WhoAmI();
};