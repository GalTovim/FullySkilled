#pragma once
#include "person.h"

class Employee : virtual public Person {
protected:
	float salary;
public:
	//default constructor
	Employee();
	//constructor
	Employee(float salary, int age, string name, long id);
	/*
	//copy constructor
	Employee(const Employee& CopyEmployee);
	*/
	//d'tor
	~Employee();
	//get functions
	inline float GetSalary() { return salary; }
	virtual void WhoAmI();

};
