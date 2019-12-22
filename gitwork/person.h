#pragma once
#include <iostream>
#include <string>
#include <typeinfo>
using namespace std;
class Person
{
protected:
	string Name; //10 chars maximum
	long ID;
	int Age;
	friend class Student;
	friend class Employee;
	public:
	Person();
	Person(const Person& p1);
	Person(string Name, long ID, int Age);
	virtual void WhoAmI() = 0;
	~Person();	
};