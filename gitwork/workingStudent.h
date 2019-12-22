#include"student.h"
#pragma once
using namespace std;

class workingStudent : virtual public Student virtual public Employee
{
public:
	workingStudent(workingStudent ws);
	workingStudent();
	~workingStudent();

private:
	bool same_institute;
};
