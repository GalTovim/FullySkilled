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
};
