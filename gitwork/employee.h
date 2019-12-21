#pragma once
#include "person.h"

class Employee : public Person{
    private:
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
	virtual ~Employee();
    //get functions
    inline float GetSalary() { return salary; }
};
