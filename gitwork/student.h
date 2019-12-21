#include <string>
#include "person.h"

using namespace std;

#ifndef STUDENT_H
#define STUDENT_H

class Student : public Person
{
protected:
  int Average;
  string Institute; // 10 chars max
public:
  Student(const Student &student);
  Student(int Average, string Institute, int Age, string name, long id);
  ~Student();
};

#endif