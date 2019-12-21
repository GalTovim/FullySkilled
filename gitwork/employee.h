#pragma once
#include "person.h"

class Employee : public Person{
    private:
        float salary;
    public:
    //default constructor
	Employee();
    //constructor
    Employee(float salary, int Age, string name, long id);
    //copy constructor
	Employee(const Employee& CCtor);
    //d'tor
	~Employee();
    //get functions
    inline float GetSalary() { return salary; }
};
