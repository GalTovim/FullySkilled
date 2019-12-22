#include"student.h"
#pragma once
using namespace std;

class workingStudent : virtual public Student virtual public Employee
{
public:
	workingStudent(Student s1);
	~workingStudent();

private:
	bool same_institute;
};
