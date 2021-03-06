#include "student.h"
#include "person.h"

using namespace std;

Student::Student(const Student &student) : Person(student)
{
  this->Average = student.Average;
  this->Institute = student.Institute;
}

Student::Student(int Average, string Institute, int Age, string name, long id) : Person(name, id, Age)
{
  this->Average = Average;
  this->Institute = Institute;
}

Student::~Student()
{
  cout << "Student C'tor" << endl;
}