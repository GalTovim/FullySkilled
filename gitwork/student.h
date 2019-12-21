#pragma once
#include "person.h"

class Student : virtual public Person
{
protected:
  int Average;
  string Institute; // 10 chars max
public:
  Student(const Student &student);
  Student(int Average, string Institute, int Age, string name, long id);
  ~Student();
};
